import pytest
from fastapi import HTTPException
from backend.app.services.upload_service import validate_extension


def test_valid_extension_py():
    ext = validate_extension("script.py")
    assert ext == ".py"


def test_valid_extension_sql():
    ext = validate_extension("consulta.sql")
    assert ext == ".sql"


def test_valid_extension_srw():
    ext = validate_extension("janela.srw")
    assert ext == ".srw"


def test_invalid_extension_raises():
    with pytest.raises(HTTPException) as exc_info:
        validate_extension("arquivo.exe")
    assert exc_info.value.status_code == 400
    assert "não permitida" in exc_info.value.detail


def test_invalid_extension_docx():
    with pytest.raises(HTTPException):
        validate_extension("documento.docx")
