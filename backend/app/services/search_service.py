from sqlalchemy.orm import Session

from backend.app.models.content import Content
from backend.app.repositories.content_repository import ContentRepository


class SearchService:

    def __init__(self, db: Session):
        self.repo = ContentRepository(db)

    def search(self, query: str, filters: dict) -> list[Content]:
        return self.repo.search_fts(query=query, filters=filters)
