from pathlib import Path

_ENCODINGS = ["utf-8", "latin-1", "cp1252"]


def read_file_content(path: str | Path) -> tuple[str | None, str | None]:
    """
    Tenta ler o arquivo com utf-8, latin-1 e cp1252.
    Retorna (conteudo, encoding_usado) ou (None, None) se falhar.
    """
    for enc in _ENCODINGS:
        try:
            text = Path(path).read_text(encoding=enc)
            return text, enc
        except (UnicodeDecodeError, LookupError):
            continue
        except (FileNotFoundError, OSError):
            return None, None
    return None, None
