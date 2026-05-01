from backend.app.services.content_service import ContentService
from backend.app.services.search_service import SearchService


def test_search_by_text(db):
    """TC-FTS-01 | Integração | Busca por texto deve retornar conteúdo indexado no FTS5."""
    svc = ContentService(db)
    svc.create(
        {
            "title": "Procedure de fechamento",
            "content": "EXEC sp_fechamento_contabil",
            "language": "SQL",
            "tags": ["procedure", "contabilidade"],
        }
    )
    search = SearchService(db)
    results = search.search("fechamento", {})
    assert len(results) >= 1
    assert any(
        "fechamento" in r.title.lower() or "fechamento" in (r.content or "").lower()
        for r in results
    )


def test_search_no_results(db):
    """TC-FTS-02 | Integração | Busca por termo inexistente deve retornar lista vazia."""
    svc = ContentService(db)
    svc.create({"title": "Outro conteúdo", "content": "texto qualquer", "tags": []})
    search = SearchService(db)
    results = search.search("termoqueNaoExiste12345", {})
    assert results == []


def test_search_with_filter(db):
    """TC-FTS-03 | Integração | Filtro por linguagem deve retornar apenas itens correspondentes."""
    svc = ContentService(db)
    svc.create(
        {
            "title": "Script Python",
            "content": "print('oi')",
            "language": "Python",
            "tags": [],
        }
    )
    svc.create(
        {"title": "Consulta SQL", "content": "SELECT 1", "language": "SQL", "tags": []}
    )
    search = SearchService(db)
    results = search.search("", {"language": "Python"})
    assert all(r.language == "Python" for r in results)


def test_fts_updated_after_content_update(db):
    """TC-FTS-04 | Integração | FTS5 deve refletir título atualizado após update."""
    svc = ContentService(db)
    item = svc.create({"title": "Título original", "content": "base", "tags": []})
    svc.update(
        item, {"title": "Título modificado", "content": "atualizado", "tags": []}
    )
    search = SearchService(db)
    results = search.search("modificado", {})
    assert any("modificado" in r.title.lower() for r in results)


def test_fts_cleared_after_delete(db):
    """TC-FTS-05 | Integração | FTS5 não deve retornar item após delete."""
    svc = ContentService(db)
    item = svc.create({"title": "ItemParaDeletar99", "content": "...", "tags": []})
    svc.delete(item)
    search = SearchService(db)
    results = search.search("ItemParaDeletar99", {})
    assert results == []


def test_search_combined_filters(db):
    """TC-SCH-05 | Integração | Filtros combinados devem retornar apenas itens que satisfazem todos."""
    svc = ContentService(db)
    svc.create(
        {
            "title": "Regra SQL",
            "content": "...",
            "language": "SQL",
            "is_business_rule": True,
            "tags": [],
        }
    )
    svc.create(
        {
            "title": "Script SQL",
            "content": "...",
            "language": "SQL",
            "is_business_rule": False,
            "tags": [],
        }
    )
    svc.create(
        {
            "title": "Regra Python",
            "content": "...",
            "language": "Python",
            "is_business_rule": True,
            "tags": [],
        }
    )
    search = SearchService(db)
    results = search.search("", {"language": "SQL", "is_business_rule": True})
    assert len(results) == 1
    assert results[0].title == "Regra SQL"
