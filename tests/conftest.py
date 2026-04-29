import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.app.database import Base, get_db
from backend.app.main import app

DATABASE_URL_TEST = "sqlite:///:memory:"

engine_test = create_engine(
    DATABASE_URL_TEST,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # garante que todas as conexões usem o mesmo banco em memória
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def _setup_test_db():
    from backend.app.models import content  # noqa: F401 — registra os modelos
    Base.metadata.create_all(bind=engine_test)
    with engine_test.connect() as conn:
        conn.execute(text("""
            CREATE VIRTUAL TABLE IF NOT EXISTS content_fts
            USING fts5(title, content, category, language, system, domain, tags)
        """))
        conn.commit()


@pytest.fixture(scope="function")
def db():
    _setup_test_db()
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine_test)
        with engine_test.connect() as conn:
            conn.execute(text("DROP TABLE IF EXISTS content_fts"))
            conn.commit()


@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
