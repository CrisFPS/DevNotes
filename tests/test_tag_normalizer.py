"""Testes de normalize_tags, escritos a partir do cartão da tarefa.

Nos testes de exemplo, o valor esperado é literal copiado da tabela do cartão.
"""

import pytest

from backend.app.services.tag_normalizer import normalize_tags


def test_converts_tags_to_lowercase():
    """TC-TAG-01 | Unitário | Tags com maiúsculas viram minúsculas."""
    assert normalize_tags("SQL, Snippet") == ["sql", "snippet"]


def test_inner_space_becomes_hyphen():
    """TC-TAG-02 | Unitário | Espaço dentro da tag vira hífen."""
    assert normalize_tags("regra de negocio, legado") == ["regra-de-negocio", "legado"]


def test_removes_duplicates_after_normalizing():
    """TC-TAG-03 | Unitário | Tags que só diferem em caixa ou espaço viram uma só."""
    assert normalize_tags("sql, SQL , sql") == ["sql"]


def test_keeps_order_of_first_occurrence():
    """TC-TAG-04 | Unitário | A ordem segue a primeira ocorrência de cada tag."""
    assert normalize_tags("legado, sql, Legado, java") == ["legado", "sql", "java"]


def test_typed_form_matches_preregistered_tag():
    """TC-TAG-05 | Unitário | 'Regra Negocio' e 'regra-negocio' viram a mesma tag."""
    assert normalize_tags("regra-negocio, Regra Negocio") == ["regra-negocio"]


def test_empty_text_returns_empty_list():
    """TC-TAG-06 | Unitário | Campo vazio não gera tag."""
    assert normalize_tags("") == []


def test_empty_pieces_between_commas_are_dropped():
    """TC-TAG-07 | Unitário | Só vírgulas e espaços devolve lista vazia."""
    assert normalize_tags(" , ,, ") == []


def test_edge_whitespace_is_removed_not_hyphenated():
    """TC-TAG-08 | Unitário | Espaço nas pontas é removido, não vira hífen."""
    assert normalize_tags("  powerbuilder  ") == ["powerbuilder"]


def test_run_of_spaces_and_tab_becomes_single_hyphen():
    """TC-TAG-09 | Unitário | Espaços e tab seguidos viram um único hífen."""
    assert normalize_tags("regra   \t negocio") == ["regra-negocio"]


def test_non_breaking_space_becomes_hyphen():
    """TC-TAG-10 | Unitário | Espaço não separável (colado do Word) vira hífen."""
    assert normalize_tags("regra\u00a0negocio") == ["regra-negocio"]


@pytest.mark.parametrize("raw", [None, ["sql"], 10])
def test_non_string_input_raises_type_error(raw):
    """TC-TAG-11 | Unitário | Entrada que não é str levanta TypeError."""
    with pytest.raises(TypeError):
        normalize_tags(raw)


# Entradas das propriedades P1 e P2 do cartão: as válidas da tabela e outras que
# misturam caixa, tab, quebra de linha, espaço não separável e símbolos.
PROPERTY_INPUTS = [
    "SQL, Snippet",
    "regra de negocio, legado",
    "sql, SQL , sql",
    "legado, sql, Legado, java",
    "regra-negocio, Regra Negocio",
    "",
    " , ,, ",
    "  powerbuilder  ",
    "regra   \t negocio",
    "regra\u00a0negocio",
    "  Java ,JAVA,  java script ,Java\tScript",
    "sql\nlegado, SQL",
    "regra\u00a0de\u00a0negocio, regra de negocio",
    "C#, c#, .NET , Node.js",
]


@pytest.mark.parametrize("raw", PROPERTY_INPUTS)
def test_normalizing_the_result_again_changes_nothing(raw):
    """TC-TAG-12 | Unitário | P1: normalizar de novo o resultado não o altera."""
    result = normalize_tags(raw)
    assert normalize_tags(", ".join(result)) == result


@pytest.mark.parametrize("raw", PROPERTY_INPUTS)
def test_result_has_only_valid_unique_tags(raw):
    """TC-TAG-13 | Unitário | P2: tags não vazias, minúsculas, sem espaço e únicas."""
    result = normalize_tags(raw)
    assert len(result) == len(set(result))
    for tag in result:
        assert tag != ""
        assert tag == tag.lower()
        assert not any(char.isspace() for char in tag)


# LACUNAS: o cartão não decide estes casos. Nenhum teste congela o resultado.
# LAC-01 "sql; legado"     -> ";" também separa tags? Pelo cartão sai ["sql;-legado"].
# LAC-02 "regra - negocio" -> hífens seguidos viram um só? "_" vira "-"?
#                             Pelo cartão sai ["regra---negocio"]; "regra_negocio"
#                             fica como está.
# LAC-03 "C#, C++, .NET"   -> que símbolos uma tag pode ter? Uma limpeza que aceite
#                             só letras, números e hífen junta "c#" e "c++" em "c".
