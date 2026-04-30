import asyncio

import pytest
from fastapi import HTTPException

from backend.app.services.upload_service import validate_extension, save_upload
from tests.conftest import make_upload_file


def test_valid_extension_py():
    """TC-UPL-01 | Unitário | Aceitar extensão .py como válida."""
    ext = validate_extension("script.py")
    assert ext == ".py"


def test_valid_extension_sql():
    """TC-UPL-02 | Unitário | Aceitar extensão .sql como válida."""
    ext = validate_extension("consulta.sql")
    assert ext == ".sql"


def test_valid_extension_srw():
    """TC-UPL-03 | Unitário | Aceitar extensão .srw (PowerBuilder) como válida."""
    ext = validate_extension("janela.srw")
    assert ext == ".srw"


def test_invalid_extension_raises():
    """TC-UPL-ERR-01 | Unitário | Rejeitar extensão .exe com HTTPException 400."""
    with pytest.raises(HTTPException) as exc_info:
        validate_extension("arquivo.exe")
    assert exc_info.value.status_code == 400
    assert "não permitida" in exc_info.value.detail


def test_invalid_extension_docx():
    """TC-UPL-ERR-02 | Unitário | Rejeitar extensão .docx com HTTPException."""
    with pytest.raises(HTTPException):
        validate_extension("documento.docx")


def test_upload_rejects_oversized_file(oversized_content, upload_dir):
    """TC-UPL-04 | Unitário | Rejeitar arquivo acima de 12 MB com HTTPException 400."""
    mock_file = make_upload_file("grande.sql", oversized_content)
    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(save_upload(mock_file))
    assert exc_info.value.status_code == 400
    assert "12" in exc_info.value.detail or "limite" in exc_info.value.detail.lower()


def test_validate_extension_no_ext():
    """TC-EXT-06 | Unitário | Rejeitar filename sem extensão com HTTPException 400."""
    with pytest.raises(HTTPException) as exc_info:
        validate_extension("arquivo_sem_extensao")
    assert exc_info.value.status_code == 400
