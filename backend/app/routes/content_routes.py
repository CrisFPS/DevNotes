from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.app.config import config
from backend.app.database import get_db
from backend.app.services.content_service import ContentService

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")


@router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    svc = ContentService(db)
    recent = svc.list_all()[:5]
    return templates.TemplateResponse(request, "index.html", {"recent": recent})


@router.get("/content")
def list_content(request: Request, db: Session = Depends(get_db)):
    svc = ContentService(db)
    items = svc.list_all()
    for item in items:
        item._tags = svc.get_tags(item.id)
    return templates.TemplateResponse(request, "list.html", {"items": items})


@router.get("/content/new")
def new_form(request: Request):
    return templates.TemplateResponse(request, "form.html", {
        "item": None,
        "config": config,
        "tags_str": "",
    })


@router.post("/content/new")
def create_content(
    request: Request,
    title: str = Form(...),
    content: str = Form(""),
    category: str = Form(""),
    language: str = Form(""),
    system: str = Form(""),
    domain: str = Form(""),
    is_business_rule: bool = Form(False),
    tags: str = Form(""),
    db: Session = Depends(get_db),
):
    svc = ContentService(db)
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    new_item = svc.create({
        "title": title,
        "content": content,
        "category": category,
        "language": language,
        "system": system,
        "domain": domain,
        "is_business_rule": is_business_rule,
        "tags": tag_list,
    })
    return RedirectResponse(f"/content/{new_item.id}", status_code=303)


@router.get("/content/{content_id}")
def detail(content_id: int, request: Request, db: Session = Depends(get_db)):
    svc = ContentService(db)
    item = svc.get(content_id)
    if not item:
        return templates.TemplateResponse(request, "404.html", status_code=404)
    tags = svc.get_tags(content_id)
    return templates.TemplateResponse(request, "detail.html", {
        "item": item,
        "tags": tags,
    })


@router.get("/content/{content_id}/edit")
def edit_form(content_id: int, request: Request, db: Session = Depends(get_db)):
    svc = ContentService(db)
    item = svc.get(content_id)
    if not item:
        return RedirectResponse("/content", status_code=303)
    tags = svc.get_tags(content_id)
    return templates.TemplateResponse(request, "form.html", {
        "item": item,
        "config": config,
        "tags_str": ", ".join(tags),
    })


@router.post("/content/{content_id}/edit")
def update_content(
    content_id: int,
    title: str = Form(...),
    content: str = Form(""),
    category: str = Form(""),
    language: str = Form(""),
    system: str = Form(""),
    domain: str = Form(""),
    is_business_rule: bool = Form(False),
    tags: str = Form(""),
    db: Session = Depends(get_db),
):
    svc = ContentService(db)
    item = svc.get(content_id)
    if not item:
        return RedirectResponse("/content", status_code=303)
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    svc.update(item, {
        "title": title,
        "content": content,
        "category": category,
        "language": language,
        "system": system,
        "domain": domain,
        "is_business_rule": is_business_rule,
        "tags": tag_list,
    })
    return RedirectResponse(f"/content/{content_id}", status_code=303)


@router.post("/content/{content_id}/delete")
def delete_content(content_id: int, db: Session = Depends(get_db)):
    svc = ContentService(db)
    item = svc.get(content_id)
    if item:
        svc.delete(item)
    return RedirectResponse("/content", status_code=303)
