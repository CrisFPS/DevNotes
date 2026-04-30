from sqlalchemy.orm import Session
from sqlalchemy import text

from backend.app.models.content import Content, Tag, ContentTag, UploadedFile


class ContentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Content]:
        return self.db.query(Content).order_by(Content.updated_at.desc()).all()

    def get_by_id(self, content_id: int) -> Content | None:
        return self.db.query(Content).filter(Content.id == content_id).first()

    def create(self, content: Content) -> Content:
        self.db.add(content)
        self.db.commit()
        self.db.refresh(content)
        self._index_fts(content)
        return content

    def update(self, content: Content) -> Content:
        self.db.commit()
        self.db.refresh(content)
        return content

    def delete(self, content: Content) -> None:
        self._delete_fts(content.id)
        self.db.delete(content)
        self.db.commit()

    def get_or_create_tag(self, name: str) -> Tag:
        tag = self.db.query(Tag).filter(Tag.name == name).first()
        if not tag:
            tag = Tag(name=name)
            self.db.add(tag)
            self.db.flush()
        return tag

    def set_tags(self, content: Content, tag_names: list[str]) -> None:
        self.db.query(ContentTag).filter(ContentTag.content_id == content.id).delete()
        for name in tag_names:
            if name.strip():
                tag = self.get_or_create_tag(name.strip())
                self.db.add(ContentTag(content_id=content.id, tag_id=tag.id))
        self.db.commit()

    def get_tags_for_content(self, content_id: int) -> list[str]:
        rows = (
            self.db.query(Tag.name)
            .join(ContentTag, Tag.id == ContentTag.tag_id)
            .filter(ContentTag.content_id == content_id)
            .all()
        )
        return [r.name for r in rows]

    def save_uploaded_file(self, file_meta: UploadedFile) -> UploadedFile:
        self.db.add(file_meta)
        self.db.commit()
        self.db.refresh(file_meta)
        return file_meta

    def search_fts(self, query: str, filters: dict) -> list[Content]:
        if query:
            rows = self.db.execute(
                text("SELECT rowid FROM content_fts WHERE content_fts MATCH :q ORDER BY rank"),
                {"q": query},
            ).fetchall()
            ids = [r[0] for r in rows]
            if not ids:
                return []
            q = self.db.query(Content).filter(Content.id.in_(ids))
        else:
            q = self.db.query(Content)

        if filters.get("category"):
            q = q.filter(Content.category == filters["category"])
        if filters.get("language"):
            q = q.filter(Content.language == filters["language"])
        if filters.get("system"):
            q = q.filter(Content.system == filters["system"])
        if filters.get("domain"):
            q = q.filter(Content.domain == filters["domain"])
        if filters.get("is_business_rule"):
            q = q.filter(Content.is_business_rule == True)  # noqa: E712

        return q.order_by(Content.updated_at.desc()).all()

    def _tags_as_string(self, content_id: int) -> str:
        return " ".join(self.get_tags_for_content(content_id))

    def _index_fts(self, content: Content) -> None:
        tags_str = self._tags_as_string(content.id)
        self.db.execute(
            text("""
                INSERT INTO content_fts(rowid, title, content, category, language, system, domain, tags)
                VALUES (:id, :title, :body, :category, :language, :system, :domain, :tags)
            """),
            {
                "id": content.id,
                "title": content.title or "",
                "body": content.content or "",
                "category": content.category or "",
                "language": content.language or "",
                "system": content.system or "",
                "domain": content.domain or "",
                "tags": tags_str,
            },
        )
        self.db.commit()

    def _update_fts(self, content: Content) -> None:
        self._delete_fts(content.id)
        self._index_fts(content)

    def _delete_fts(self, content_id: int) -> None:
        self.db.execute(
            text("DELETE FROM content_fts WHERE rowid = :id"),
            {"id": content_id},
        )
        self.db.commit()
