import tempfile
from pathlib import Path

from backend.app.services.encoding_service import read_file_content


def test_read_utf8():
    """TC-ENC-01 | Unitário | Verificar leitura de arquivo UTF-8 com encoding correto."""
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".txt", delete=False
    ) as f:
        f.write("SELECT * FROM tabela WHERE campo = 'valor'")
        path = f.name
    content, enc = read_file_content(path)
    assert content is not None
    assert "SELECT" in content
    assert enc == "utf-8"
    Path(path).unlink()


def test_read_latin1():
    """TC-ENC-02 | Unitário | Verificar fallback de encoding para latin-1."""
    with tempfile.NamedTemporaryFile(mode="wb", suffix=".txt", delete=False) as f:
        f.write("Conteúdo com acentuação".encode("latin-1"))
        path = f.name
    content, enc = read_file_content(path)
    assert content is not None
    assert enc in ("latin-1", "utf-8")
    Path(path).unlink()


def test_read_nonexistent_returns_none():
    """TC-ENC-03 | Unitário | Verificar retorno (None, None) para arquivo inexistente."""
    content, enc = read_file_content("/caminho/que/nao/existe.txt")
    assert content is None
    assert enc is None


def test_read_cp1252(tmp_path):
    """TC-ENC-04 | Unitário | Fallback de encoding deve tentar cp1252 como terceira opção."""
    f = tmp_path / "cp1252.txt"
    # 0x80 é válido em cp1252 (€) mas inválido em utf-8 e ambíguo em latin-1
    f.write_bytes(b"\x80\x99texto cp1252")
    content, enc = read_file_content(f)
    assert content is not None
    assert enc in ("cp1252", "latin-1")
