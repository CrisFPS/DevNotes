from backend.app.services.content_service import ContentService
from backend.app.services.search_service import SearchService


def test_search_by_text(db):
    svc = ContentService(db)
    svc.create({
        "title": "Procedure de fechamento",
        "content": "EXEC sp_fechamento_contabil",
        "language": "SQL",
        "tags": ["procedure", "contabilidade"],
    })
    search = SearchService(db)
    results = search.search("fechamento", {})
    assert len(results) >= 1
    assert any("fechamento" in r.title.lower() or "fechamento" in (r.content or "").lower() for r in results)


def test_search_no_results(db):
    svc = ContentService(db)
    svc.create({"title": "Outro conteúdo", "content": "texto qualquer", "tags": []})
    search = SearchService(db)
    results = search.search("termoqueNaoExiste12345", {})
    assert results == []


def test_search_with_filter(db):
    svc = ContentService(db)
    svc.create({"title": "Script Python", "content": "print('oi')", "language": "Python", "tags": []})
    svc.create({"title": "Consulta SQL", "content": "SELECT 1", "language": "SQL", "tags": []})
    search = SearchService(db)
    results = search.search("", {"language": "Python"})
    assert all(r.language == "Python" for r in results)
