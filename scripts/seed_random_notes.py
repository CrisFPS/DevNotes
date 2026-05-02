from __future__ import annotations

import argparse
import random
import sys
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from backend.app.config import config  # noqa: E402
from backend.app.database import SessionLocal, create_tables  # noqa: E402
from backend.app.models.content import Content  # noqa: E402
from backend.app.services.content_service import ContentService  # noqa: E402


SEED_MARKER = "DEVNOTES_RANDOM_SEED_V1"
DEFAULT_COUNT = 200
DEFAULT_SEED = 20260502


@dataclass(frozen=True)
class NoteTemplate:
    category: str
    language: str
    object_type: str
    tags: tuple[str, ...]
    title_prefix: str
    body: str
    is_business_rule: bool = False


SYSTEMS = [
    "Sistema Administrativo",
    "Sistema CarPayroll",
    "Sistema Financeiro",
    "Sistema Just&Py",
    "Sistema Calypso",
    "Sistema DeVNotes",
    "Sistema LogBem",
    "Sistema RH",
    "ERP Legado",
    "Portal de Atendimento",
]

DOMAINS = [
    "Administrativo",
    "Contabil",
    "Logistica",
    "Financeiro",
    "Recursos Humanos",
    "Tecnico",
    "Fiscal",
    "Operacoes",
]

FEATURES = [
    "cadastro de clientes",
    "fechamento financeiro",
    "importacao de arquivos CNAB",
    "calculo de folha",
    "auditoria de permissao",
    "emissao de relatorio gerencial",
    "sincronizacao com API externa",
    "tratamento de excecao em lote",
    "rotina batch noturna",
    "consulta de performance",
    "conciliacao bancaria",
    "controle de estoque",
    "reprocessamento de eventos",
    "validacao de documento fiscal",
    "exportacao para data warehouse",
]

TOOLS = [
    "pytest",
    "curl",
    "git",
    "uvicorn",
    "sqlite3",
    "PowerBuilder",
    "Jenkins",
    "Docker",
    "psql",
    "VS Code",
]

TAG_POOL = [
    "sql",
    "procedure",
    "powerbuilder",
    "regra-negocio",
    "contabilidade",
    "financeiro",
    "integracao",
    "python",
    "markdown",
    "java",
    "script",
    "snippet",
    "legado",
    "erro",
    "performance",
    "batch",
    "api",
    "deploy",
    "auditoria",
    "teste-paginacao",
]

TEMPLATES = [
    NoteTemplate(
        category="SQL",
        language="SQL",
        object_type="Consulta",
        tags=("sql", "performance", "snippet"),
        title_prefix="Consulta para diagnostico",
        body="""Objetivo: localizar registros inconsistentes em {feature}.

```sql
SELECT c.id, c.status, c.updated_at, COUNT(i.id) AS itens
FROM {table_name} c
LEFT JOIN {item_table} i ON i.parent_id = c.id
WHERE c.status IN ('PENDENTE', 'ERRO')
  AND c.updated_at >= date('now', '-{days} day')
GROUP BY c.id, c.status, c.updated_at
HAVING COUNT(i.id) = 0
ORDER BY c.updated_at DESC;
```

Observacao: executar primeiro em leitura e validar plano de execucao antes de aplicar indice.""",
    ),
    NoteTemplate(
        category="Script",
        language="Python",
        object_type="Script",
        tags=("python", "script", "integracao"),
        title_prefix="Script simples de apoio",
        body="""Uso local para revisar payloads de {feature}.

```python
from pathlib import Path
import json

base = Path("samples/{slug}")
for path in base.glob("*.json"):
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("status") == "ERRO":
        print(path.name, payload.get("codigo"), payload.get("mensagem"))
```

Observacao: nao grava arquivos; serve apenas para conferencia em ambiente de desenvolvimento.""",
    ),
    NoteTemplate(
        category="Comando",
        language="Texto comum",
        object_type="Comando",
        tags=("deploy", "script", "erro"),
        title_prefix="Comando util de verificacao",
        body="""Comando usado durante manutencao de {feature}.

```bash
{command}
```

Resultado esperado: retorno sem erro e log contendo a referencia {ticket}.
Se falhar, comparar variaveis de ambiente e credenciais locais antes de abrir incidente.""",
    ),
    NoteTemplate(
        category="Regra de Negocio",
        language="Markdown",
        object_type="Regra",
        tags=("regra-negocio", "auditoria"),
        title_prefix="Regra de validacao",
        body="""Regra aplicada em {feature}.

- Entrada deve possuir identificador externo unico.
- Registros com status CANCELADO nao entram no calculo.
- Divergencias abaixo de R$ {amount} podem seguir para conciliacao automatica.
- Divergencias acima do limite exigem aprovacao do perfil Supervisor.

Ponto de atencao: regra herdada do modulo legado e confirmada com a area de negocio.""",
        is_business_rule=True,
    ),
    NoteTemplate(
        category="Anotacao Tecnica",
        language="PowerBuilder",
        object_type="Legado",
        tags=("powerbuilder", "legado", "erro"),
        title_prefix="Observacao sobre rotina legada",
        body="""Anotacao sobre comportamento observado em {feature}.

Objeto: {pb_object}
Evento: ue_processar

O fluxo altera a variavel global antes da chamada remota. Em execucoes paralelas,
o valor pode ser sobrescrito e gerar mensagem generica de falha.

Sugestao: isolar estado por janela ou passar contexto por argumento antes de refatorar.""",
    ),
    NoteTemplate(
        category="Exemplo",
        language="Java",
        object_type="Snippet",
        tags=("java", "api", "snippet"),
        title_prefix="Exemplo de chamada de servico",
        body="""Exemplo reduzido para {feature}.

```java
var request = new ConsultaRequest("{ticket}", LocalDate.now().minusDays({days}));
var response = cliente.consultar(request);

if (!response.isSucesso()) {{
    log.warn("Falha na consulta: {{}}", response.getMensagem());
}}
```

Observacao: manter timeout baixo no ambiente local para evidenciar indisponibilidade cedo.""",
    ),
    NoteTemplate(
        category="Erro e Solucao",
        language="Markdown",
        object_type="Anotacao",
        tags=("erro", "legado", "performance"),
        title_prefix="Erro conhecido e contorno",
        body="""Sintoma em {feature}: tela demora para carregar ou retorna lista vazia.

Causa provavel: filtro opcional enviado como string vazia, forçando comparacao direta no banco.

Contorno local:
1. Reproduzir com massa pequena.
2. Conferir parametros no log.
3. Remover filtros vazios antes de executar a consulta.

Observacao: registrar evidencia com o ticket {ticket}.""",
    ),
    NoteTemplate(
        category="Procedure",
        language="SQL",
        object_type="Procedure",
        tags=("sql", "procedure", "batch"),
        title_prefix="Procedure de reprocessamento",
        body="""Modelo de procedure para reprocessar {feature}.

```sql
CREATE PROCEDURE sp_reprocessa_{slug}
AS
BEGIN
    UPDATE fila_processamento
       SET status = 'PENDENTE',
           tentativas = 0
     WHERE status = 'ERRO'
       AND origem = '{system_code}';
END;
```

Observacao: usar somente em base local ou homologacao com autorizacao.""",
    ),
]


def _choices(name: str, fallback: list[str]) -> list[str]:
    values = config.get(name) or []
    return values if values else fallback


def _slug(value: str) -> str:
    return (
        value.lower()
        .replace("&", "e")
        .replace(" ", "_")
        .replace("-", "_")
        .replace("/", "_")
    )


def _sample_tags(rng: random.Random, base_tags: tuple[str, ...]) -> list[str]:
    extra = rng.sample(TAG_POOL, k=rng.randint(1, 3))
    tags = [*base_tags, *extra, "seed-devnotes", "teste-paginacao"]
    return sorted(set(tags))


def _render_body(
    template: NoteTemplate,
    index: int,
    feature: str,
    system: str,
    domain: str,
    rng: random.Random,
) -> str:
    ticket = f"DEV-{1000 + index}"
    slug = _slug(feature)
    system_code = "".join(part[0] for part in system.split() if part).upper()[:5]
    command = rng.choice(
        [
            "python -m pytest tests/test_search_fts.py -v",
            "curl -s http://localhost:8000/content | python -m json.tool",
            "sqlite3 backend/devnotes.db \"SELECT COUNT(*) FROM content;\"",
            "git status --short",
            "uvicorn backend.app.main:app --reload",
        ]
    )
    body = template.body.format(
        amount=rng.choice(["0,50", "1,00", "5,00", "10,00"]),
        command=command,
        days=rng.randint(3, 90),
        domain=domain,
        feature=feature,
        item_table=f"{slug}_item",
        pb_object=f"w_{slug[:24]}",
        slug=slug[:32],
        system=system,
        system_code=system_code or "LOCAL",
        table_name=f"{slug}_cabecalho",
        ticket=ticket,
    )
    footer = (
        f"\n\nMetadados da massa: {SEED_MARKER}; indice={index:03d}; "
        f"sistema={system}; dominio={domain}."
    )
    return body + footer


def _build_content(index: int, rng: random.Random) -> dict:
    template = rng.choice(TEMPLATES)
    feature = rng.choice(FEATURES)
    systems = _choices("sistemas", SYSTEMS)
    domains = _choices("dominios", DOMAINS)
    categories = _choices("categorias", [template.category])
    languages = _choices("linguagens", [template.language])
    system = rng.choice(systems)
    domain = rng.choice(domains)
    category = template.category if template.category in categories else rng.choice(categories)
    language = template.language if template.language in languages else rng.choice(languages)
    created_at = datetime.now(UTC) - timedelta(
        days=rng.randint(0, 180),
        hours=rng.randint(0, 23),
        minutes=rng.randint(0, 59),
    )
    updated_at = created_at + timedelta(days=rng.randint(0, 14), minutes=rng.randint(0, 180))

    return {
        "title": f"{template.title_prefix} #{index:03d} - {feature}",
        "content": _render_body(template, index, feature, system, domain, rng),
        "category": category,
        "language": language,
        "system": system,
        "domain": domain,
        "object_type": template.object_type,
        "is_business_rule": template.is_business_rule or rng.random() < 0.18,
        "created_at": created_at,
        "updated_at": updated_at,
        "tags": _sample_tags(rng, template.tags),
    }


def _delete_existing_seed(service: ContentService) -> int:
    existing = (
        service.repo.db.query(Content)
        .filter(Content.content.like(f"%{SEED_MARKER}%"))
        .all()
    )
    for item in existing:
        service.delete(item)
    return len(existing)


def seed_random_notes(
    count: int = DEFAULT_COUNT,
    seed: int = DEFAULT_SEED,
    replace_seed: bool = True,
) -> tuple[int, int]:
    rng = random.Random(seed)
    create_tables()

    db = SessionLocal()
    try:
        service = ContentService(db)
        removed = _delete_existing_seed(service) if replace_seed else 0
        for index in range(1, count + 1):
            service.create(_build_content(index, rng))
        return count, removed
    finally:
        db.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Insere anotacoes tecnicas aleatorias na base local do DevNotes."
    )
    parser.add_argument(
        "--count",
        type=int,
        default=DEFAULT_COUNT,
        help=f"Quantidade de anotacoes a inserir. Padrao: {DEFAULT_COUNT}.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help="Semente para gerar dados variados e reproduziveis.",
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Nao remove registros anteriores desta massa antes de inserir.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.count < 1:
        raise SystemExit("--count deve ser maior que zero.")

    inserted, removed = seed_random_notes(
        count=args.count,
        seed=args.seed,
        replace_seed=not args.append,
    )
    print(f"Registros inseridos: {inserted}")
    print(f"Registros removidos da massa anterior: {removed}")
    print("Erro: nenhum")
    print("Base local: backend/devnotes.db")
    print(
        "Tipos gerados: SQL, Python, Java, Markdown, PowerBuilder, comandos, "
        "procedures, regras de negocio, notas de legado e observacoes tecnicas."
    )


if __name__ == "__main__":
    main()
