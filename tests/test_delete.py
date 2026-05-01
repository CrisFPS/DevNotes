"""Suite de testes para a funcionalidade de exclusão de conteúdo."""

import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy import text

from backend.app.services.content_service import ContentService
from backend.app.repositories.content_repository import ContentRepository
from backend.app.models.content import Content, ContentTag, UploadedFile


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _create(db, title="Conteúdo teste", content="SELECT 1", tags=None, **kwargs):
    svc = ContentService(db)
    return svc.create(
        {"title": title, "content": content, "tags": tags or [], **kwargs}
    )


def _fts_count(db, content_id: int) -> int:
    result = db.execute(
        text("SELECT COUNT(*) FROM content_fts WHERE rowid = :id"),
        {"id": content_id},
    )
    return result.scalar()


# ---------------------------------------------------------------------------
# TC-DEL-01  Serviço | Exclusão remove o registro do banco
# ---------------------------------------------------------------------------


def test_delete_removes_from_db(db):
    """TC-DEL-01 | Serviço | Exclusão deve remover o registro de Content do banco."""
    item = _create(db)
    item_id = item.id

    svc = ContentService(db)
    svc.delete(item)

    remaining = db.query(Content).filter(Content.id == item_id).first()
    assert remaining is None


# ---------------------------------------------------------------------------
# TC-DEL-02  Serviço | Listagem não retorna item excluído
# ---------------------------------------------------------------------------


def test_delete_item_absent_from_list(db):
    """TC-DEL-02 | Serviço | list_all() não deve retornar conteúdo após exclusão."""
    svc = ContentService(db)
    _create(db, title="Manter")
    item = _create(db, title="Excluir")

    svc.delete(item)

    titles = [c.title for c in svc.list_all()]
    assert "Excluir" not in titles
    assert "Manter" in titles


# ---------------------------------------------------------------------------
# TC-DEL-03  Serviço | Exclusão em cascata remove tags associadas
# ---------------------------------------------------------------------------


def test_delete_cascades_to_tags(db):
    """TC-DEL-03 | Serviço | Exclusão deve remover em cascata as tags associadas."""
    item = _create(db, tags=["python", "sql"])
    item_id = item.id

    svc = ContentService(db)
    svc.delete(item)

    orphan_tags = db.query(ContentTag).filter(ContentTag.content_id == item_id).all()
    assert orphan_tags == []


# ---------------------------------------------------------------------------
# TC-DEL-04  Serviço | Exclusão em cascata remove arquivo anexado
# ---------------------------------------------------------------------------


def test_delete_cascades_to_uploaded_file(db):
    """TC-DEL-04 | Serviço | Exclusão deve remover em cascata o UploadedFile associado."""
    svc = ContentService(db)
    item = _create(db)
    svc.attach_file(
        item.id,
        {
            "original_name": "arq.sql",
            "saved_name": "xyz.sql",
            "local_path": "/uploads/xyz.sql",
            "extension": ".sql",
            "file_type": "SQL",
            "object_type": "SQL",
            "language": "SQL",
            "file_size": 512,
            "encoding_used": "utf-8",
        },
    )

    svc.delete(item)

    record = db.query(UploadedFile).filter(UploadedFile.content_id == item.id).first()
    assert record is None


# ---------------------------------------------------------------------------
# TC-DEL-05  Repositório | Exclusão limpa o índice FTS5
# ---------------------------------------------------------------------------


def test_delete_clears_fts_index(db):
    """TC-DEL-05 | Repositório | Exclusão deve remover a entrada correspondente do índice FTS5."""
    item = _create(db, title="ItemFTS_exclusao")
    item_id = item.id

    assert _fts_count(db, item_id) == 1

    svc = ContentService(db)
    svc.delete(item)

    assert _fts_count(db, item_id) == 0


# ---------------------------------------------------------------------------
# TC-DEL-06  Repositório | Exclusão de ID inexistente no FTS não levanta exceção
# ---------------------------------------------------------------------------


def test_delete_fts_nonexistent_id_is_silent(db):
    """TC-DEL-06 | Repositório | _delete_fts com ID inexistente não deve levantar exceção."""
    repo = ContentRepository(db)
    # não deve lançar
    repo._delete_fts(999999)


# ---------------------------------------------------------------------------
# TC-DEL-07  Rota | DELETE via POST retorna redirect 303 para /content
# ---------------------------------------------------------------------------


def test_delete_route_redirects_to_list(client, db):
    """TC-DEL-07 | Rota | POST /content/{id}/delete deve redirecionar para /content (303)."""
    item = _create(db)
    response = client.post(f"/content/{item.id}/delete")
    assert response.status_code in (200, 303)
    # follow_redirects=False → verifica redirect diretamente
    no_follow = client.post(
        f"/content/{_create(db, title='X2').id}/delete", follow_redirects=False
    )
    assert no_follow.status_code == 303
    assert no_follow.headers["location"] in ("/content", "http://testserver/content")


# ---------------------------------------------------------------------------
# TC-DEL-08  Rota | Item excluído não aparece na listagem HTML
# ---------------------------------------------------------------------------


def test_delete_route_item_removed_from_html_list(client, db):
    """TC-DEL-08 | Rota | Após exclusão via rota, título não deve aparecer em GET /content."""
    item = _create(db, title="TítuloParaExcluir_8")
    client.post(f"/content/{item.id}/delete", follow_redirects=True)

    list_html = client.get("/content").text
    assert "TítuloParaExcluir_8" not in list_html


# ---------------------------------------------------------------------------
# TC-DEL-09  Rota | DELETE de ID inexistente redireciona sem erro
# ---------------------------------------------------------------------------


def test_delete_nonexistent_id_redirects(client):
    """TC-DEL-09 | Rota | POST /content/99999/delete com ID inexistente deve redirecionar (303)."""
    response = client.post("/content/99999/delete", follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] in ("/content", "http://testserver/content")


# ---------------------------------------------------------------------------
# TC-DEL-10  Rota | Falha no serviço retorna erro 500 com mensagem amigável
# ---------------------------------------------------------------------------


def test_delete_service_failure_returns_500(client, db):
    """TC-DEL-10 | Rota | Exceção no serviço deve retornar HTTP 500 com mensagem amigável."""
    item = _create(db, title="FalhaDelete")

    with patch(
        "backend.app.routes.content_routes.ContentService.delete",
        side_effect=RuntimeError("falha simulada"),
    ):
        response = client.post(f"/content/{item.id}/delete", follow_redirects=True)

    assert response.status_code == 500
    assert "excluir" in response.text.lower()


# ---------------------------------------------------------------------------
# TC-DEL-11  Rota | Exclusão a partir da página de detalhe
# ---------------------------------------------------------------------------


def test_delete_from_detail_page_redirects_to_list(client, db):
    """TC-DEL-11 | Rota | Exclusão disparada pela página de detalhe redireciona para lista."""
    item = _create(db, title="DetalheDelete")
    response = client.post(f"/content/{item.id}/delete", follow_redirects=True)
    assert response.status_code == 200
    assert "DetalheDelete" not in response.text


# ---------------------------------------------------------------------------
# TC-DEL-12  Serviço | Múltiplas exclusões independentes não afetam outros registros
# ---------------------------------------------------------------------------


def test_delete_multiple_items_independently(db):
    """TC-DEL-12 | Serviço | Excluir múltiplos itens não deve afetar os registros restantes."""
    svc = ContentService(db)
    a = _create(db, title="Alpha")
    b = _create(db, title="Beta")
    c = _create(db, title="Gamma")

    svc.delete(a)
    svc.delete(b)

    remaining = svc.list_all()
    titles = [r.title for r in remaining]
    assert "Alpha" not in titles
    assert "Beta" not in titles
    assert "Gamma" in titles


# ---------------------------------------------------------------------------
# TC-DEL-13  Repositório | get() retorna None após exclusão
# ---------------------------------------------------------------------------


def test_get_returns_none_after_delete(db):
    """TC-DEL-13 | Repositório | svc.get(id) deve retornar None após exclusão."""
    svc = ContentService(db)
    item = _create(db)
    item_id = item.id

    svc.delete(item)

    assert svc.get(item_id) is None
