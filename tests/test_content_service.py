from backend.app.services.content_service import ContentService
from backend.app.models.content import UploadedFile


def test_create_content(db):
    """TC-CNT-01 | Integração | Verificar criação de conteúdo com campos obrigatórios e tags."""
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
    """TC-CNT-02 | Integração | Verificar listagem de todos os conteúdos cadastrados."""
    svc = ContentService(db)
    svc.create({"title": "Item 1", "content": "...", "tags": []})
    svc.create({"title": "Item 2", "content": "...", "tags": []})
    items = svc.list_all()
    assert len(items) == 2


def test_update_content(db):
    """TC-CNT-03 | Integração | Verificar atualização de título e conteúdo via ContentService."""
    svc = ContentService(db)
    item = svc.create({"title": "Original", "content": "texto", "tags": []})
    updated = svc.update(item, {"title": "Atualizado", "content": "novo texto", "tags": []})
    assert updated.title == "Atualizado"


def test_delete_content(db):
    """TC-CNT-04 | Integração | Verificar exclusão de conteúdo e ausência na listagem."""
    svc = ContentService(db)
    item = svc.create({"title": "Para excluir", "content": "...", "tags": []})
    svc.delete(item)
    items = svc.list_all()
    assert len(items) == 0


def test_business_rule_flag(db):
    """TC-CNT-05 | Integração | Verificar flag is_business_rule=True persiste no banco."""
    svc = ContentService(db)
    item = svc.create({
        "title": "Regra contábil",
        "content": "Regra de negócio X",
        "is_business_rule": True,
        "tags": [],
    })
    assert item.is_business_rule is True


def test_attach_file_saves_uploaded_file_record(db):
    """TC-UPF-01 | Integração | attach_file deve gravar registro na tabela uploaded_file."""
    svc = ContentService(db)
    item = svc.create({"title": "Com arquivo", "content": "SELECT 1", "tags": []})
    file_meta = {
        "original_name": "consulta.sql",
        "saved_name": "abc123.sql",
        "local_path": "/uploads/abc123.sql",
        "extension": ".sql",
        "file_type": "SQL",
        "object_type": "SQL",
        "language": "SQL",
        "file_size": 1024,
        "encoding_used": "utf-8",
    }
    svc.attach_file(item.id, file_meta)
    record = db.query(UploadedFile).filter(UploadedFile.content_id == item.id).first()
    assert record is not None
    assert record.original_name == "consulta.sql"
    assert record.file_size == 1024
    assert record.encoding_used == "utf-8"
