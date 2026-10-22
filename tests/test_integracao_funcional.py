"""Casos produzidos pelo prompt funcional v2.

Contrato da interface HTTP do DevNotes, critério funcional
(partição de equivalência, valor limite, semântica HTTP e erros).
Sem código-fonte das rotas. O limite de 12 MB é o da especificação.
"""

def _cadastro(**extras):
    dados = {
        "title": "Nota funcional",
        "content": "SELECT id FROM cliente",
        "category": "SQL",
        "language": "SQL",
        "system": "Sistema Financeiro",
        "domain": "Financeiro",
        "tags": "sql, snippet",
        "is_business_rule": "",
    }
    dados.update(extras)
    return dados


def test_cadastro_valido_redireciona_e_fica_pesquisavel(client):
    """TC-IFN-01 | Integração | Cadastro válido redireciona, mostra o detalhe e entra na busca."""
    resposta = client.post("/content/new", data=_cadastro(), follow_redirects=False)
    assert resposta.status_code == 303
    assert "/content/" in resposta.headers["location"]

    detalhe = client.get(resposta.headers["location"])
    assert detalhe.status_code == 200
    assert "Nota funcional" in detalhe.text
    assert "<pre><code" in detalhe.text
    assert "sql" in detalhe.text

    busca = client.post(
        "/search",
        data={
            "query": "cliente",
            "category": "",
            "language": "SQL",
            "system": "",
            "domain": "",
            "is_business_rule": "",
        },
    )
    assert busca.status_code == 200
    assert "Nota funcional" in busca.text


def test_cadastro_sem_titulo_nao_persiste(client):
    """TC-IFN-02 | Integração | Campo title ausente responde 4xx e não grava o conteúdo."""
    dados = _cadastro()
    dados.pop("title")
    resposta = client.post("/content/new", data=dados, follow_redirects=False)
    assert 400 <= resposta.status_code < 500
    listagem = client.get("/content")
    assert "SELECT id FROM cliente" not in listagem.text


def test_campos_opcionais_vazios_ainda_cadastram(client):
    """TC-IFN-03 | Integração | Só o título preenchido ainda cadastra o conteúdo."""
    resposta = client.post(
        "/content/new",
        data=_cadastro(
            title="Somente titulo",
            content="",
            category="",
            language="",
            system="",
            domain="",
            tags="",
        ),
        follow_redirects=False,
    )
    assert resposta.status_code == 303
    detalhe = client.get(resposta.headers["location"])
    assert "Somente titulo" in detalhe.text


def test_detalhe_de_id_inexistente_exibe_pagina_404(client):
    """TC-IFN-04 | Integração | Id inexistente devolve a página 404."""
    resposta = client.get("/content/99999")
    assert resposta.status_code == 404
    assert "não encontrado" in resposta.text.lower()


def test_upload_sql_integra_arquivo_classificacao_e_busca(client, upload_dir):
    """TC-IFN-05 | Integração | Upload .sql grava o texto, a linguagem SQL e a busca."""
    resposta = client.post(
        "/upload",
        data={
            "title": "Consulta de clientes",
            "category": "SQL",
            "system": "",
            "domain": "",
            "tags": "sql",
            "is_business_rule": "",
        },
        files={"file": ("consulta.sql", b"SELECT id FROM cliente", "text/plain")},
        follow_redirects=False,
    )
    assert resposta.status_code == 303
    detalhe = client.get(resposta.headers["location"])
    assert "Consulta de clientes" in detalhe.text
    assert "SELECT id FROM cliente" in detalhe.text
    assert "SQL" in detalhe.text

    busca = client.post(
        "/search",
        data={
            "query": "cliente",
            "category": "",
            "language": "",
            "system": "",
            "domain": "",
            "is_business_rule": "",
        },
    )
    assert "Consulta de clientes" in busca.text


def test_upload_powerbuilder_classifica_linguagem(client, upload_dir):
    """TC-IFN-06 | Integração | Upload .srw classifica a linguagem como PowerBuilder."""
    resposta = client.post(
        "/upload",
        data={"title": "Janela principal", "category": "", "tags": ""},
        files={"file": ("w_principal.srw", b"$PBExportHeader$w_principal.srw", "text/plain")},
        follow_redirects=False,
    )
    assert resposta.status_code == 303
    detalhe = client.get(resposta.headers["location"])
    assert "PowerBuilder" in detalhe.text


def test_upload_extensao_recusada_permanece_no_formulario(client, upload_dir):
    """TC-IFN-07 | Integração | Extensão recusada responde 400 e não entra na listagem."""
    resposta = client.post(
        "/upload",
        data={"title": "Planilha", "category": "", "tags": ""},
        files={"file": ("planilha.xlsx", b"conteudo", "application/octet-stream")},
        follow_redirects=False,
    )
    assert resposta.status_code == 400
    assert "não permitida" in resposta.text.lower() or "nao permitida" in resposta.text.lower()
    assert "Upload de arquivo" in resposta.text
    listagem = client.get("/content")
    assert "Planilha" not in listagem.text


def test_upload_latin1_preserva_texto(client, upload_dir):
    """TC-IFN-08 | Integração | Arquivo latin-1 preserva o acento no detalhe."""
    conteudo = "Regra com acentuação: alíquota".encode("latin-1")
    resposta = client.post(
        "/upload",
        data={"title": "Regra latin1", "category": "", "tags": ""},
        files={"file": ("regra.txt", conteudo, "text/plain")},
        follow_redirects=False,
    )
    assert resposta.status_code == 303
    detalhe = client.get(resposta.headers["location"])
    assert "alíquota" in detalhe.text


def test_upload_acima_de_12_mb_e_recusado(client, upload_dir):
    """TC-IFN-09 | Integração | Arquivo de 12 MB + 1 byte é recusado."""
    resposta = client.post(
        "/upload",
        data={"title": "Grande demais", "category": "", "tags": ""},
        files={
            "file": (
                "grande.sql",
                b"x" * (12 * 1024 * 1024 + 1),
                "text/plain",
            )
        },
        follow_redirects=False,
    )
    assert resposta.status_code == 400
    assert "excede" in resposta.text.lower()


def test_busca_sem_resultado_nao_mostra_outro_titulo(client):
    """TC-IFN-10 | Integração | Termo inexistente não mostra outra nota."""
    client.post("/content/new", data=_cadastro(title="Nota presente"), follow_redirects=True)
    busca = client.post(
        "/search",
        data={
            "query": "termoinexistente",
            "category": "",
            "language": "",
            "system": "",
            "domain": "",
            "is_business_rule": "",
        },
    )
    assert busca.status_code == 200
    assert "Nota presente" not in busca.text


def test_filtro_de_linguagem_exclui_outra_particao(client):
    """TC-IFN-11 | Integração | Filtro de linguagem exclui a outra partição."""
    client.post(
        "/content/new",
        data=_cadastro(title="Nota SQL", content="SELECT 1", language="SQL"),
        follow_redirects=True,
    )
    client.post(
        "/content/new",
        data=_cadastro(title="Nota Python", content="print(1)", language="Python", category="Script"),
        follow_redirects=True,
    )
    busca = client.post(
        "/search",
        data={
            "query": "",
            "category": "",
            "language": "SQL",
            "system": "",
            "domain": "",
            "is_business_rule": "",
        },
    )
    assert "Nota SQL" in busca.text
    assert "Nota Python" not in busca.text


def test_editar_atualiza_o_que_a_busca_encontra(client):
    """TC-IFN-12 | Integração | Edição atualiza o texto encontrado pela busca."""
    criado = client.post(
        "/content/new",
        data=_cadastro(title="Titulo antigo", content="texto antigo"),
        follow_redirects=False,
    )
    destino = criado.headers["location"]
    editado = client.post(
        f"{destino}/edit",
        data=_cadastro(title="Titulo novo", content="texto revisado"),
        follow_redirects=False,
    )
    assert editado.status_code == 303
    busca = client.post(
        "/search",
        data={
            "query": "revisado",
            "category": "",
            "language": "",
            "system": "",
            "domain": "",
            "is_business_rule": "",
        },
    )
    assert "Titulo novo" in busca.text


def test_excluir_remove_da_busca(client):
    """TC-IFN-13 | Integração | Exclusão tira o conteúdo da busca."""
    criado = client.post(
        "/content/new",
        data=_cadastro(title="Sera excluida", content="conteudo exclusivo zz"),
        follow_redirects=False,
    )
    conteudo_id = criado.headers["location"].rsplit("/", 1)[-1]
    exclusao = client.post(f"/content/{conteudo_id}/delete", follow_redirects=False)
    assert exclusao.status_code == 303
    assert exclusao.headers["location"].endswith("/content")
    busca = client.post(
        "/search",
        data={
            "query": "exclusivo",
            "category": "",
            "language": "",
            "system": "",
            "domain": "",
            "is_business_rule": "",
        },
    )
    assert "Sera excluida" not in busca.text
