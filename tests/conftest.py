import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from unittest.mock import AsyncMock, MagicMock

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


@pytest.fixture
def txt_file(tmp_path):
    """TC-ENC-01 | Arquivo .txt UTF-8 para testes de encoding."""
    f = tmp_path / "nota.txt"
    f.write_text("Conteúdo simples em texto", encoding="utf-8")
    return f


@pytest.fixture
def sql_file(tmp_path):
    """Arquivo .sql UTF-8 para testes de upload e extensão."""
    f = tmp_path / "consulta.sql"
    f.write_text("SELECT id, nome FROM cliente WHERE ativo = 1", encoding="utf-8")
    return f


@pytest.fixture
def srw_file(tmp_path):
    """Arquivo .srw para testes de classificação PowerBuilder."""
    f = tmp_path / "w_principal.srw"
    f.write_text("$PBExportHeader$w_principal.srw", encoding="utf-8")
    return f


@pytest.fixture
def latin1_file(tmp_path):
    """Arquivo com encoding latin-1 para testes de fallback."""
    f = tmp_path / "legado.txt"
    f.write_bytes("Conteúdo com acentuação em latin-1".encode("latin-1"))
    return f


@pytest.fixture
def invalid_ext_file(tmp_path):
    """Arquivo .xlsx para testar rejeição de extensão inválida."""
    f = tmp_path / "planilha.xlsx"
    f.write_bytes(b"conteudo qualquer")
    return f


@pytest.fixture
def oversized_content():
    """Bytes que excedem 12 MB para testar validação de tamanho."""
    return b"x" * (13 * 1024 * 1024)


def make_upload_file(filename: str, content: bytes) -> MagicMock:
    """Cria um UploadFile mock com .filename e .read() async."""
    mock = MagicMock()
    mock.filename = filename
    mock.read = AsyncMock(return_value=content)
    return mock


@pytest.fixture
def upload_dir(tmp_path, monkeypatch):
    """Redireciona UPLOADS_DIR para diretório temporário durante o teste."""
    import backend.app.services.upload_service as us
    monkeypatch.setattr(us, "UPLOADS_DIR", tmp_path)
    return tmp_path
