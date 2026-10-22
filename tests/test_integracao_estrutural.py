"""Casos produzidos pelo prompt estrutural v2.

Papel: especialista em cobertura de decisões. Contexto: código das rotas
de upload, conteúdo e busca. Cada caso mira um desvio real da integração,
não um código HTTP genérico de API JSON.
"""

from backend.app.services.content_service import ContentService


def _cadastro(**extras):
    dados = {
        "title": "Nota estrutural",
        "content": "SELECT 1",
        "category": "",
        "language": "",
        "system": "",
        "domain": "",
        "tags": "",
        "is_business_rule": "",
    }
    dados.update(extras)
    return dados


def test_upload_com_sucesso_redireciona_303(client, upload_dir):
    """TC-IES-01 | Integração | Upload sem exceção responde 303 para o detalhe."""
    resposta = client.post(
        "/upload",
        data={"title": "Arquivo ok", "category": "", "tags": ""},
        files={"file": ("ok.sql", b"SELECT 1", "text/plain")},
        follow_redirects=False,
    )
    assert resposta.status_code == 303
    assert "/content/" in resposta.headers["location"]


def test_upload_com_extensao_invalida_devolve_400(client, upload_dir):
    """TC-IES-02 | Integração | Extensão inválida cai no except e responde 400."""
    resposta = client.post(
        "/upload",
        data={"title": "Ruim", "category": "", "tags": ""},
        files={"file": ("ruim.exe", b"MZ", "application/octet-stream")},
        follow_redirects=False,
    )
    assert resposta.status_code == 400
    assert "não permitida" in resposta.text.lower()


def test_upload_no_limite_passa_e_um_byte_acima_falha(client, upload_dir, monkeypatch):
    """TC-IES-03 | Integração | No limite o upload passa; um byte acima responde 400."""
    import backend.app.services.upload_service as upload_service

    monkeypatch.setattr(upload_service, "MAX_SIZE_BYTES", 8)

    no_limite = client.post(
        "/upload",
        data={"title": "No limite", "category": "", "tags": ""},
        files={"file": ("limite.txt", b"12345678", "text/plain")},
        follow_redirects=False,
    )
    assert no_limite.status_code == 303

    acima = client.post(
        "/upload",
        data={"title": "Acima do limite", "category": "", "tags": ""},
        files={"file": ("acima.txt", b"123456789", "text/plain")},
        follow_redirects=False,
    )
    assert acima.status_code == 400
    assert "excede" in acima.text.lower()


def test_upload_sem_titulo_usa_nome_do_arquivo(client, upload_dir):
    """TC-IES-04 | Integração | Título em branco no upload usa o nome do arquivo."""
    resposta = client.post(
        "/upload",
        data={"title": "   ", "category": "", "tags": ""},
        files={"file": ("nome_original.md", b"# nota", "text/plain")},
        follow_redirects=True,
    )
    assert resposta.status_code == 200
    assert "<h1>nome_original.md</h1>" in resposta.text


def test_upload_com_titulo_preserva_o_titulo_informado(client, upload_dir):
    """TC-IES-05 | Integração | Título informado permanece, e o nome do arquivo fica nos metadados."""
    resposta = client.post(
        "/upload",
        data={"title": "Titulo informado", "category": "", "tags": ""},
        files={"file": ("outro.md", b"# nota", "text/plain")},
        follow_redirects=True,
    )
    assert "<h1>Titulo informado</h1>" in resposta.text
    assert "outro.md" in resposta.text


def test_detalhe_inexistente_renderiza_404(client):
    """TC-IES-06 | Integração | Detalhe sem item renderiza 404."""
    resposta = client.get("/content/99999")
    assert resposta.status_code == 404
    assert "404" in resposta.text


def test_detalhe_existente_renderiza_codigo(client, db):
    """TC-IES-07 | Integração | Detalhe com item renderiza o bloco de código."""
    item = ContentService(db).create(
        {"title": "Visivel", "content": "SELECT 42", "tags": []}
    )
    resposta = client.get(f"/content/{item.id}")
    assert resposta.status_code == 200
    assert "<pre><code" in resposta.text
    assert "SELECT 42" in resposta.text


def test_excluir_id_inexistente_redireciona_para_lista(client):
    """TC-IES-08 | Integração | Exclusão de id inexistente redireciona para a lista."""
    resposta = client.post("/content/99999/delete", follow_redirects=False)
    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith("/content")


def test_excluir_id_existente_sai_do_indice(client, db):
    """TC-IES-09 | Integração | Exclusão de item existente tira o texto da busca."""
    item = ContentService(db).create(
        {"title": "Indexado", "content": "palavraunica", "tags": []}
    )
    resposta = client.post(f"/content/{item.id}/delete", follow_redirects=False)
    assert resposta.status_code == 303
    busca = client.post(
        "/search",
        data={
            "query": "palavraunica",
            "category": "",
            "language": "",
            "system": "",
            "domain": "",
            "is_business_rule": "",
        },
    )
    assert "Indexado" not in busca.text


def test_falha_ao_excluir_renderiza_erro_500(client, db, monkeypatch):
    """TC-IES-10 | Integração | Falha ao excluir renderiza a página de erro 500."""

    item = ContentService(db).create({"title": "Fragil", "content": "x", "tags": []})

    def falha(self, content):
        raise RuntimeError("falha simulada")

    monkeypatch.setattr(ContentService, "delete", falha)
    resposta = client.post(f"/content/{item.id}/delete")
    assert resposta.status_code == 500
    assert "Não foi possível excluir" in resposta.text


def test_editar_id_inexistente_redireciona(client):
    """TC-IES-11 | Integração | Edição de id inexistente redireciona para a lista."""
    resposta = client.post(
        "/content/99999/edit",
        data=_cadastro(),
        follow_redirects=False,
    )
    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith("/content")


def test_pagina_abaixo_de_um_ainda_lista(client, db):
    """TC-IES-12 | Integração | Página menor que 1 e página acima do total ainda listam o item."""
    ContentService(db).create({"title": "Unica nota", "content": "a", "tags": []})
    abaixo = client.get("/content?page=0")
    acima = client.get("/content?page=99")
    assert abaixo.status_code == 200
    assert acima.status_code == 200
    assert "Unica nota" in abaixo.text
    assert "Unica nota" in acima.text


def test_busca_sem_texto_aplica_so_filtro_de_regra(client, db):
    """TC-IES-13 | Integração | Busca sem texto e com regra de negócio devolve só a regra."""
    ContentService(db).create(
        {
            "title": "Regra de negocio",
            "content": "desconto",
            "is_business_rule": True,
            "tags": [],
        }
    )
    ContentService(db).create(
        {
            "title": "Snippet comum",
            "content": "desconto",
            "is_business_rule": False,
            "tags": [],
        }
    )
    resposta = client.post(
        "/search",
        data={
            "query": "",
            "category": "",
            "language": "",
            "system": "",
            "domain": "",
            "is_business_rule": "true",
        },
    )
    assert resposta.status_code == 200
    assert "Regra de negocio" in resposta.text
    assert "Snippet comum" not in resposta.text


def test_busca_com_filtros_preenchidos_monta_o_dicionario(client, db):
    """TC-IES-14 | Integração | Filtros de categoria, linguagem, sistema e domínio atuam juntos."""
    ContentService(db).create(
        {
            "title": "Alvo",
            "content": "alpha",
            "category": "SQL",
            "language": "SQL",
            "system": "ERP",
            "domain": "Fiscal",
            "tags": [],
        }
    )
    ContentService(db).create(
        {
            "title": "Outro",
            "content": "alpha",
            "category": "Script",
            "language": "Python",
            "system": "CRM",
            "domain": "Vendas",
            "tags": [],
        }
    )
    resposta = client.post(
        "/search",
        data={
            "query": "alpha",
            "category": "SQL",
            "language": "SQL",
            "system": "ERP",
            "domain": "Fiscal",
            "is_business_rule": "",
        },
    )
    assert "Alvo" in resposta.text
    assert "Outro" not in resposta.text
