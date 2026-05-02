from datetime import UTC, datetime

from sqlalchemy.orm import Session

from backend.app.models.content import Content, UploadedFile
from backend.app.repositories.content_repository import ContentRepository

CONTENT_PAGE_SIZE = 20


class ContentService:

    def __init__(self, db: Session):
        self.repo = ContentRepository(db)

    def list_all(self) -> list[Content]:
        return self.repo.get_all()

    def list_page(self, page: int = 1, per_page: int = CONTENT_PAGE_SIZE) -> dict:
        page = max(page, 1)
        per_page = max(per_page, 1)
        total_items = self.repo.count_all()
        total_pages = (total_items + per_page - 1) // per_page

        if total_pages == 0:
            current_page = 1
            items = []
        else:
            current_page = min(page, total_pages)
            offset = (current_page - 1) * per_page
            items = self.repo.get_page(per_page, offset)

        return {
            "items": items,
            "total_items": total_items,
            "total_pages": total_pages,
            "current_page": current_page,
            "per_page": per_page,
            "previous_page": current_page - 1 if total_pages and current_page > 1 else None,
            "next_page": current_page + 1 if current_page < total_pages else None,
        }

    def get(self, content_id: int) -> Content | None:
        return self.repo.get_by_id(content_id)

    def create(self, data: dict) -> Content:
        tags = data.pop("tags", [])
        content = Content(**data)
        content = self.repo.create(content)
        if tags:
            self.repo.set_tags(content, tags)
            self.repo._update_fts(content)
        return content

    def update(self, content: Content, data: dict) -> Content:
        tags = data.pop("tags", [])
        for key, value in data.items():
            setattr(content, key, value)
        content.updated_at = datetime.now(UTC)
        content = self.repo.update(content)
        self.repo.set_tags(content, tags)
        self.repo._update_fts(content)
        return content

    def delete(self, content: Content) -> None:
        self.repo.delete(content)

    def get_tags(self, content_id: int) -> list[str]:
        return self.repo.get_tags_for_content(content_id)

    def attach_file(self, content_id: int, file_meta: dict) -> None:
        record = UploadedFile(
            content_id=content_id,
            original_name=file_meta["original_name"],
            saved_name=file_meta["saved_name"],
            local_path=file_meta["local_path"],
            extension=file_meta["extension"],
            file_type=file_meta["file_type"],
            object_type=file_meta["object_type"],
            file_size=file_meta["file_size"],
            encoding_used=file_meta["encoding_used"],
        )
        self.repo.save_uploaded_file(record)
