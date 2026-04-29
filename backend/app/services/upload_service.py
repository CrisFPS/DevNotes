import uuid
from pathlib import Path

from fastapi import UploadFile, HTTPException

from backend.app.config import config
from backend.app.services.encoding_service import read_file_content
from backend.app.services.extension_classifier import classify

UPLOADS_DIR = Path(__file__).parent.parent.parent.parent / "uploads"
MAX_SIZE_BYTES = config.get("upload", {}).get("tamanho_maximo_mb", 12) * 1024 * 1024
ALLOWED_EXTENSIONS: set[str] = set(config.get("extensoes_aceitas", []))


def validate_extension(filename: str) -> str:
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Extensão '{ext}' não permitida. Aceitas: {', '.join(sorted(ALLOWED_EXTENSIONS))}",
        )
    return ext


async def save_upload(file: UploadFile) -> dict:
    """
    Valida, salva e processa o arquivo enviado.
    Retorna dicionário com metadados e conteúdo extraído.
    """
    ext = validate_extension(file.filename)

    raw = await file.read()
    if len(raw) > MAX_SIZE_BYTES:
        raise HTTPException(
            status_code=400,
            detail=f"Arquivo excede o limite de {MAX_SIZE_BYTES // (1024 * 1024)} MB.",
        )

    saved_name = f"{uuid.uuid4().hex}{ext}"
    dest = UPLOADS_DIR / saved_name
    dest.write_bytes(raw)

    classification = classify(ext)
    text_content, encoding_used = read_file_content(dest)

    return {
        "original_name": file.filename,
        "saved_name": saved_name,
        "local_path": str(dest),
        "extension": ext,
        "file_type": classification["object_type"] or classification["language"],
        "object_type": classification["object_type"],
        "language": classification["language"],
        "file_size": len(raw),
        "encoding_used": encoding_used,
        "text_content": text_content,
    }
