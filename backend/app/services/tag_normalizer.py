"""Normaliza o texto do campo "Tags (separadas por vírgula)".

Contrato: cartão normalize_tags, em
prompts/08.02_Prompt_de_Agente_Desenvolvedor_Cartao_Tarefa.md.
Lacunas abertas (LAC-01 a LAC-04) no fim de tests/test_tag_normalizer.py: mudar o
separador, os símbolos aceitos ou o que conta como espaço resolve uma delas.
"""

import re

_TAG_SEPARATOR = ","
# Em str, \s é o mesmo conjunto de str.strip() e str.isspace(): os quatro do cartão
# (item 4) e outros 25, como \r e U+2003. Se a lista do cartão é fechada: LAC-04.
_INNER_WHITESPACE = re.compile(r"\s+")


def normalize_tags(raw: str) -> list[str]:
    """Separa o texto por vírgula e devolve as tags normalizadas, sem repetição."""
    if not isinstance(raw, str):
        raise TypeError(f"As tags devem ser texto (str), não {type(raw).__name__}.")
    tags: list[str] = []
    for piece in raw.split(_TAG_SEPARATOR):
        # Cartão, itens 2 a 4. O strip() vem antes do sub() para o espaço das pontas
        # sumir em vez de virar hífen (TC-TAG-08).
        tag = _INNER_WHITESPACE.sub("-", piece.strip().lower())
        # Cartão, itens 2 e 5: descarta o pedaço vazio e compara a repetição depois
        # de normalizar ("SQL" e "sql" são a mesma tag).
        if tag and tag not in tags:
            tags.append(tag)
    return tags
