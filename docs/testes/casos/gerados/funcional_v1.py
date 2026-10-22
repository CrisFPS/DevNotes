"""Casos produzidos pelo prompt funcional v1 (zero-shot, sem contrato).

O prompt pediu apenas "testes de integração da API". A resposta assumiu
recursos JSON no estilo REST genérico, que o DevNotes não expõe.
"""


def test_cria_conteudo_json(client):
    resposta = client.post(
        "/api/contents",
        json={"title": "Nota de integracao", "content": "SELECT 1"},
    )
    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["title"] == "Nota de integracao"
    assert corpo["id"] > 0


def test_lista_conteudos_json(client):
    resposta = client.get("/api/contents")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)


def test_upload_retorna_metadados_json(client):
    resposta = client.post(
        "/api/uploads",
        files={"file": ("consulta.sql", b"SELECT id FROM cliente", "text/plain")},
    )
    assert resposta.status_code == 201
    assert resposta.json()["language"] == "SQL"


def test_busca_retorna_json(client):
    client.post("/api/contents", json={"title": "Cliente", "content": "SELECT id FROM cliente"})
    resposta = client.get("/api/search", params={"q": "cliente"})
    assert resposta.status_code == 200
    assert resposta.json()[0]["title"] == "Cliente"
