from datetime import UTC, datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from backend.app.database import Base


def _now() -> datetime:
    return datetime.now(UTC)


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text)
    category = Column(String)
    language = Column(String)
    system = Column(String)
    domain = Column(String)
    object_type = Column(String)
    is_business_rule = Column(Boolean, default=False)
    created_at = Column(DateTime, default=_now)
    updated_at = Column(DateTime, default=_now, onupdate=_now)

    tags = relationship(
        "ContentTag", back_populates="content", cascade="all, delete-orphan"
    )
    uploaded_file = relationship(
        "UploadedFile",
        back_populates="content",
        uselist=False,
        cascade="all, delete-orphan",
    )


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    contents = relationship("ContentTag", back_populates="tag")


class ContentTag(Base):
    __tablename__ = "content_tag"

    content_id = Column(Integer, ForeignKey("content.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tag.id"), primary_key=True)

    content = relationship("Content", back_populates="tags")
    tag = relationship("Tag", back_populates="contents")


class UploadedFile(Base):
    __tablename__ = "uploaded_file"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("content.id"), nullable=False)
    original_name = Column(String, nullable=False)
    saved_name = Column(String, nullable=False)
    local_path = Column(String, nullable=False)
    extension = Column(String)
    file_type = Column(String)
    object_type = Column(String)
    file_size = Column(Integer)
    encoding_used = Column(String)
    uploaded_at = Column(DateTime, default=_now)

    content = relationship("Content", back_populates="uploaded_file")
