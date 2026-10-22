"""Casos produzidos pelo prompt estrutural v1.

O prompt pedia cobertura de decisões, mas copiava o formato do ebook
(REST Assured e códigos JSON). As rotas reais foram acertadas; os oráculos, não.
"""


def _formulario(**extras):
    dados = {
        "title": "Nota",
        "content": "SELECT 1",
        "category": "SQL",
        "language": "SQL",
        "system": "",
        "domain": "",
        "tags": "",
        "is_business_rule": "",
    }
    dados.update(extras)
    return dados


def test_cadastro_retorna_201_json(client):
    resposta = client.post("/content/new", data=_formulario())
    assert resposta.status_code == 201
    assert resposta.headers["content-type"].startswith("application/json")
    assert resposta.json()["title"] == "Nota"


def test_extensao_invalida_retorna_406(client):
    resposta = client.post(
        "/upload",
        data={"title": "Planilha"},
        files={"file": ("planilha.xlsx", b"conteudo", "application/octet-stream")},
    )
    assert resposta.status_code == 406


def test_id_inexistente_retorna_json_404(client):
    resposta = client.get("/content/99999")
    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Not Found"


def test_exclusao_retorna_204(client, db):
    from backend.app.services.content_service import ContentService

    item = ContentService(db).create({"title": "Apagar", "content": "x", "tags": []})
    resposta = client.post(f"/content/{item.id}/delete")
    assert resposta.status_code == 204
