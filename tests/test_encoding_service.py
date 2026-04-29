import tempfile
from pathlib import Path

from backend.app.services.encoding_service import read_file_content


def test_read_utf8():
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".txt", delete=False) as f:
        f.write("SELECT * FROM tabela WHERE campo = 'valor'")
        path = f.name
    content, enc = read_file_content(path)
    assert content is not None
    assert "SELECT" in content
    assert enc == "utf-8"
    Path(path).unlink()


def test_read_latin1():
    with tempfile.NamedTemporaryFile(mode="wb", suffix=".txt", delete=False) as f:
        f.write("Conteúdo com acentuação".encode("latin-1"))
        path = f.name
    content, enc = read_file_content(path)
    assert content is not None
    assert enc in ("latin-1", "utf-8")
    Path(path).unlink()


def test_read_nonexistent_returns_none():
    content, enc = read_file_content("/caminho/que/nao/existe.txt")
    assert content is None
    assert enc is None
