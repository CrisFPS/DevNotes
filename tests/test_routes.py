def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_list_returns_200(client):
    response = client.get("/content")
    assert response.status_code == 200


def test_new_form_returns_200(client):
    response = client.get("/content/new")
    assert response.status_code == 200


def test_search_form_returns_200(client):
    response = client.get("/search")
    assert response.status_code == 200


def test_upload_form_returns_200(client):
    response = client.get("/upload")
    assert response.status_code == 200


def test_create_and_view(client):
    response = client.post("/content/new", data={
        "title": "Teste via rota",
        "content": "SELECT 1",
        "category": "SQL",
        "language": "SQL",
        "system": "",
        "domain": "",
        "tags": "",
        "is_business_rule": "",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Teste via rota" in response.text
