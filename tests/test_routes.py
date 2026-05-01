from backend.app.services.content_service import ContentService


def test_home_returns_200(client):
    """TC-RTE-01 | Rota | GET / deve retornar status 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_list_returns_200(client):
    """TC-RTE-02 | Rota | GET /content deve retornar status 200."""
    response = client.get("/content")
    assert response.status_code == 200


def test_new_form_returns_200(client):
    """TC-RTE-03 | Rota | GET /content/new deve retornar formulário com status 200."""
    response = client.get("/content/new")
    assert response.status_code == 200


def test_search_form_returns_200(client):
    """TC-RTE-04 | Rota | GET /search deve retornar formulário de pesquisa com status 200."""
    response = client.get("/search")
    assert response.status_code == 200


def test_upload_form_returns_200(client):
    """TC-RTE-05 | Rota | GET /upload deve retornar formulário de upload com status 200."""
    response = client.get("/upload")
    assert response.status_code == 200


def test_detail_nonexistent_returns_404(client):
    """TC-RTE-06 | Rota | GET /content/{id} com ID inexistente deve retornar 404 amigável."""
    response = client.get("/content/99999")
    assert response.status_code == 404
    assert "não encontrado" in response.text.lower()


def test_create_and_view(client):
    """TC-RTE-07 | Rota | POST /content/new deve criar conteúdo e redirecionar para detalhe."""
    response = client.post(
        "/content/new",
        data={
            "title": "Teste via rota",
            "content": "SELECT 1",
            "category": "SQL",
            "language": "SQL",
            "system": "",
            "domain": "",
            "tags": "",
            "is_business_rule": "",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Teste via rota" in response.text


def test_edit_content_via_route(client, db):
    """TC-CNT-06 | Rota | Editar conteúdo via POST /content/{id}/edit."""
    svc = ContentService(db)
    item = svc.create({"title": "Original", "content": "texto", "tags": []})
    response = client.post(
        f"/content/{item.id}/edit",
        data={
            "title": "Editado",
            "content": "novo texto",
            "category": "",
            "language": "",
            "system": "",
            "domain": "",
            "tags": "",
            "is_business_rule": "",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Editado" in response.text


def test_delete_content_via_route(client, db):
    """TC-CNT-07 | Rota | Excluir conteúdo via POST /content/{id}/delete."""
    svc = ContentService(db)
    item = svc.create({"title": "Para excluir", "content": "...", "tags": []})
    item_id = item.id
    response = client.post(f"/content/{item_id}/delete", follow_redirects=True)
    assert response.status_code == 200
    list_response = client.get("/content")
    assert "Para excluir" not in list_response.text


def test_detail_renders_pre_code_block(client, db):
    """TC-RND-01 | Rota | Template detail.html deve conter bloco <pre><code>."""
    svc = ContentService(db)
    item = svc.create(
        {
            "title": "Código SQL",
            "content": "SELECT * FROM clientes",
            "language": "SQL",
            "tags": [],
        }
    )
    response = client.get(f"/content/{item.id}")
    assert response.status_code == 200
    assert "<pre><code" in response.text
    assert "SELECT * FROM clientes" in response.text


def test_detail_renders_title(client, db):
    """TC-RND-02 | Rota | Template detail.html deve exibir o título do conteúdo."""
    svc = ContentService(db)
    item = svc.create({"title": "Título Único 12345", "content": "...", "tags": []})
    response = client.get(f"/content/{item.id}")
    assert response.status_code == 200
    assert "Título Único 12345" in response.text


def test_search_route_returns_results(client, db):
    """TC-SCH-04 | Rota | POST /search deve retornar HTML com título do resultado."""
    svc = ContentService(db)
    svc.create(
        {"title": "Procedure contábil", "content": "EXEC sp_contabil", "tags": []}
    )
    response = client.post(
        "/search",
        data={
            "query": "contábil",
            "category": "",
            "language": "",
            "system": "",
            "domain": "",
        },
    )
    assert response.status_code == 200
    assert "Procedure contábil" in response.text


def test_upload_via_route(client, db, upload_dir):
    """TC-UPL-05 | Rota | Upload completo via POST /upload deve criar Content e redirecionar."""
    sql_content = b"SELECT 1 FROM dual"
    response = client.post(
        "/upload",
        data={"title": "Consulta via Upload"},
        files={"file": ("teste.sql", sql_content, "text/plain")},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Consulta via Upload" in response.text
