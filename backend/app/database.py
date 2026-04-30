from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_PATH = Path(__file__).parent.parent / "devnotes.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    from backend.app.models import content  # noqa: F401 — registra os modelos
    Base.metadata.create_all(bind=engine)
    _create_fts_table()


def _create_fts_table():
    with engine.connect() as conn:
        row = conn.execute(
            text("SELECT sql FROM sqlite_master WHERE name = 'content_fts'")
        ).fetchone()

        needs_rebuild = row is None or "content=" in (row[0] or "")

        if needs_rebuild:
            conn.execute(text("DROP TABLE IF EXISTS content_fts"))
            conn.execute(text("""
                CREATE VIRTUAL TABLE content_fts
                USING fts5(title, content, category, language, system, domain, tags)
            """))
            # Reindexar registros existentes
            conn.execute(text("""
                INSERT INTO content_fts(rowid, title, content, category, language, system, domain, tags)
                SELECT c.id, c.title, c.content, c.category, c.language, c.system, c.domain,
                       COALESCE((
                           SELECT GROUP_CONCAT(t.name, ' ')
                           FROM tag t
                           JOIN content_tag ct ON ct.tag_id = t.id
                           WHERE ct.content_id = c.id
                       ), '')
                FROM content c
            """))
        conn.commit()
