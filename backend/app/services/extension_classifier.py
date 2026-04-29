from backend.app.config import config

_TIPO_MAP: dict[str, str] = config.get("mapeamento_extensao_tipo", {})
_LANG_MAP: dict[str, str] = config.get("mapeamento_extensao_linguagem", {})


def classify(extension: str) -> dict:
    """Retorna linguagem e tipo de objeto com base na extensão do arquivo."""
    ext = extension.lower()
    return {
        "language": _LANG_MAP.get(ext, "Outro"),
        "object_type": _TIPO_MAP.get(ext, ""),
    }
