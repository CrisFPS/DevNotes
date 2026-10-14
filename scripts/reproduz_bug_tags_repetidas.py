"""Reproduz o bug do DevNotes 1.0.0 com tags repetidas no POST /content/new.

"SQL, sql" grava duas tags diferentes. "sql, sql" devolve HTTP 500 e deixa o conteúdo
gravado sem nenhuma tag, porque ContentRepository.set_tags tenta inserir a mesma
ligação duas vezes em content_tag.

Usa SQLite em memória (mesma montagem do tests/conftest.py) e não abre o TestClient
como gerenciador de contexto, então o lifespan não roda e o backend/devnotes.db não
é tocado.

Uso, a partir da raiz do projeto:
    venv/Scripts/python.exe scripts/reproduz_bug_tags_repetidas.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))
# main.py monta frontend/static com caminho relativo à pasta atual.
os.chdir(ROOT_DIR)

from fastapi.testclient import TestClient  # noqa: E402
from sqlalchemy import create_engine, text  # noqa: E402
from sqlalchemy.orm import Session, sessionmaker  # noqa: E402
from sqlalchemy.pool import StaticPool  # noqa: E402

from backend.app.database import Base, get_db  # noqa: E402
from backend.app.main import app  # noqa: E402
from backend.app.models.content import Content, ContentTag, Tag  # noqa: E402


def create_memory_session() -> Session:
    """Cria uma sessão SQLite em memória com as tabelas e o índice FTS5."""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    with engine.connect() as conn:
        conn.execute(
            text(
                "CREATE VIRTUAL TABLE content_fts USING "
                "fts5(title, content, category, language, system, domain, tags)"
            )
        )
        conn.commit()
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)()


def main() -> None:
    db = create_memory_session()
    app.dependency_overrides[get_db] = lambda: db
    try:
        client = TestClient(app, raise_server_exceptions=False)
        for tags in ("SQL, sql", "sql, sql"):
            response = client.post(
                "/content/new",
                data={
                    "title": f"Consulta fictícia ({tags})",
                    "content": "SELECT 1",
                    "tags": tags,
                },
                follow_redirects=False,
            )
            db.rollback()
            print(f"tags={tags!r:12} -> HTTP {response.status_code}")

        titles = [c.title for c in db.query(Content).order_by(Content.id)]
        print("conteúdos gravados:", titles)
        print("tags gravadas:", [t.name for t in db.query(Tag).order_by(Tag.id)])
        print("ligações conteúdo-tag:", db.query(ContentTag).count())
    finally:
        app.dependency_overrides.clear()
        db.close()


if __name__ == "__main__":
    main()
