"""Injeção de defeitos em backend/app/services/tag_normalizer.py.

Aplica um defeito por vez, roda tests/test_tag_normalizer.py e conta quantos testes
reagem. D1 a D11 violam o contrato do cartão da tarefa e precisam ser pegos. G1 a G4
resolvem lacunas (ou fazem algo fora do escopo) em silêncio: como não estão no
contrato, os testes não têm como pegá-los.

Uso, a partir da raiz do projeto:
    venv/Scripts/python.exe scripts/injetar_defeitos_tag_normalizer.py

Para rodar numa cópia do projeto, passe --root <pasta da cópia>.

O arquivo original é restaurado byte a byte no final, mesmo se algo falhar, e o
script confere a restauração.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = Path("backend") / "app" / "services" / "tag_normalizer.py"
TESTS = "tests/test_tag_normalizer.py"

LINE_TAG = '        tag = _INNER_WHITESPACE.sub("-", piece.strip().lower())\n'
DEDUP = "        if tag and tag not in tags:\n"

# (código, descrição, [(trecho original, trecho com defeito), ...])
MUTANTS = [
    ("D1", "sem .lower()", [("piece.strip().lower()", "piece.strip()")]),
    (
        "D2",
        "deduplica antes de normalizar",
        [
            ("for piece in raw.split(", "for piece in dict.fromkeys(raw.split("),
            ("_TAG_SEPARATOR):\n", "_TAG_SEPARATOR)):\n"),
            (DEDUP, "        if tag:\n"),
        ],
    ),
    (
        "D3",
        'troca só o espaço simples (replace(" ", "-"))',
        [(LINE_TAG, '        tag = piece.strip().lower().replace(" ", "-")\n')],
    ),
    ("D4", r"\s sem o + (um hífen por caractere)", [(r'r"\s+"', r'r"\s"')]),
    ("D5", r"[ \t]+ no lugar de \s+", [(r'r"\s+"', r'r"[ \t]+"')]),
    (
        "D6",
        "troca espaços antes de tirar as pontas",
        [
            (
                LINE_TAG,
                '        tag = _INNER_WHITESPACE.sub("-", piece.lower()).strip()\n',
            )
        ],
    ),
    ("D7", "sem deduplicação", [(DEDUP, "        if tag:\n")]),
    (
        "D8",
        "deduplica com set e ordena",
        [("    return tags\n", "    return sorted(set(tags))\n")],
    ),
    ("D9", "não descarta vazios", [(DEDUP, "        if tag not in tags:\n")]),
    (
        "D10",
        "sem checagem de tipo",
        [("    if not isinstance(raw, str):\n", "    if False:\n")],
    ),
    ("D11", "underscore no lugar do hífen", [('.sub("-", ', '.sub("_", ')]),
    (
        "G1",
        "resolve LAC-02 calado: colapsa hífens",
        [
            (
                LINE_TAG,
                '        tag = re.sub("-+", "-", '
                '_INNER_WHITESPACE.sub("-", piece.strip().lower()))\n',
            )
        ],
    ),
    (
        "G2",
        'resolve LAC-01 calado: ";" também separa',
        [("raw.split(_TAG_SEPARATOR)", 're.split("[,;]", raw)')],
    ),
    (
        "G3",
        "resolve LAC-03 calado: tira símbolos",
        [
            (
                LINE_TAG,
                '        tag = re.sub("[^a-z0-9-]", "", '
                '_INNER_WHITESPACE.sub("-", piece.strip().lower()))\n',
            )
        ],
    ),
    (
        "G4",
        "remove acentos (fora do escopo)",
        [
            ("import re\n", "import re\nimport unicodedata\n"),
            (
                LINE_TAG,
                LINE_TAG + '        tag = "".join(c for c in unicodedata.normalize('
                '"NFKD", tag) if not unicodedata.combining(c))\n',
            ),
        ],
    ),
]

EXAMPLE_TESTS = {
    "test_converts_tags_to_lowercase",
    "test_inner_space_becomes_hyphen",
    "test_removes_duplicates_after_normalizing",
    "test_keeps_order_of_first_occurrence",
    "test_spaced_and_hyphenated_forms_become_one_tag",
    "test_empty_text_returns_empty_list",
    "test_empty_pieces_between_commas_are_dropped",
    "test_edge_whitespace_is_removed_not_hyphenated",
    "test_run_of_spaces_and_tab_becomes_single_hyphen",
    "test_non_breaking_space_becomes_hyphen",
    "test_non_string_input_raises_type_error",
}


def run_tests(root: Path, python: str) -> tuple[int, int, list[str]]:
    """Roda os testes de normalize_tags e devolve falhas, aprovados e testes que falharam."""
    proc = subprocess.run(
        [
            python,
            "-m",
            "pytest",
            TESTS,
            "-q",
            "-rf",
            "--tb=no",
            "-p",
            "no:cacheprovider",
        ],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"},
    )
    out = proc.stdout + proc.stderr
    failed = int(m.group(1)) if (m := re.search(r"(\d+) failed", out)) else 0
    passed = int(m.group(1)) if (m := re.search(r"(\d+) passed", out)) else 0
    if failed == 0 and passed == 0:
        raise RuntimeError(f"pytest não rodou nenhum teste:\n{out}")
    return failed, passed, re.findall(r"FAILED \S+::(\w+)", out)


def apply_mutation(source: str, code: str, replacements: list[tuple[str, str]]) -> str:
    """Aplica as trocas de um mutante e falha se algum trecho não existir."""
    for old, new in replacements:
        if old not in source:
            raise ValueError(f"{code}: trecho não encontrado: {old!r}")
        source = source.replace(old, new, 1)
    return source


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Injeta defeitos em tag_normalizer.py e conta os testes que reagem."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT_DIR,
        help="Raiz do projeto (padrão: a pasta acima de scripts/).",
    )
    parser.add_argument(
        "--python",
        default=sys.executable,
        help="Interpretador usado para rodar o pytest (padrão: o atual).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    module = root / MODULE_PATH
    original_bytes = module.read_bytes()
    # Os trechos dos mutantes usam "\n"; no Windows o arquivo pode estar em CRLF.
    newline = "\r\n" if b"\r\n" in original_bytes else "\n"
    original = original_bytes.decode("utf-8").replace("\r\n", "\n")
    try:
        base_failed, base_passed, _ = run_tests(root, args.python)
        print(f"Sem defeito: {base_passed} passed, {base_failed} failed\n")
        print(f"{'Mutante':7} {'Descrição':48} {'Falhas':>6}  Exemplos  Propriedades")
        for code, description, replacements in MUTANTS:
            mutated = apply_mutation(original, code, replacements)
            module.write_bytes(mutated.replace("\n", newline).encode("utf-8"))
            failed, _, names = run_tests(root, args.python)
            kinds = Counter("ex" if n in EXAMPLE_TESTS else "prop" for n in names)
            verdict = "morto" if failed else "SOBREVIVEU"
            print(
                f"{code:7} {description:48} {failed:>6}  {kinds['ex']:>8}"
                f"  {kinds['prop']:>12}  {verdict}"
            )
            for name in sorted({n for n in names if n in EXAMPLE_TESTS}):
                print(f"{'':58}- {name}")
    finally:
        module.write_bytes(original_bytes)
        restored = module.read_bytes() == original_bytes
        print("\nArquivo original restaurado byte a byte:", restored)


if __name__ == "__main__":
    main()
