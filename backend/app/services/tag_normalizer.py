import re

_TAG_SEPARATOR = ","
# Em str, \s cobre espaço, tab, quebra de linha e espaço não separável (cartão, item 4).
_INNER_WHITESPACE = re.compile(r"\s+")


def normalize_tags(raw: str) -> list[str]:
    """Separa o texto por vírgula e devolve as tags normalizadas, sem repetição."""
    if not isinstance(raw, str):
        raise TypeError(f"As tags devem ser texto (str), não {type(raw).__name__}.")
    tags: list[str] = []
    for piece in raw.split(_TAG_SEPARATOR):
        tag = _INNER_WHITESPACE.sub("-", piece.strip().lower())
        # A repetição é verificada depois de normalizar: "SQL" e "sql" são a mesma tag.
        if tag and tag not in tags:
            tags.append(tag)
    return tags
