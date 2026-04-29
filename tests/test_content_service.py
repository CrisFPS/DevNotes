from backend.app.services.content_service import ContentService


def test_create_content(db):
    svc = ContentService(db)
    item = svc.create({
        "title": "Teste de cadastro",
        "content": "SELECT 1",
        "category": "SQL",
        "language": "SQL",
        "system": "",
        "domain": "",
        "is_business_rule": False,
        "tags": ["sql", "teste"],
    })
    assert item.id is not None
    assert item.title == "Teste de cadastro"


def test_list_content(db):
    svc = ContentService(db)
    svc.create({"title": "Item 1", "content": "...", "tags": []})
    svc.create({"title": "Item 2", "content": "...", "tags": []})
    items = svc.list_all()
    assert len(items) == 2


def test_update_content(db):
    svc = ContentService(db)
    item = svc.create({"title": "Original", "content": "texto", "tags": []})
    updated = svc.update(item, {"title": "Atualizado", "content": "novo texto", "tags": []})
    assert updated.title == "Atualizado"


def test_delete_content(db):
    svc = ContentService(db)
    item = svc.create({"title": "Para excluir", "content": "...", "tags": []})
    svc.delete(item)
    items = svc.list_all()
    assert len(items) == 0


def test_business_rule_flag(db):
    svc = ContentService(db)
    item = svc.create({
        "title": "Regra contábil",
        "content": "Regra de negócio X",
        "is_business_rule": True,
        "tags": [],
    })
    assert item.is_business_rule is True
