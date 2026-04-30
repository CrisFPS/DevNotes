from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.app.config import config
from backend.app.database import get_db
from backend.app.services.content_service import ContentService
from backend.app.services.search_service import SearchService

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")


@router.get("/search")
def search_form(request: Request):
    return templates.TemplateResponse(request, "search.html", {
        "config": config,
        "results": None,
        "query": "",
        "filters": {},
    })


@router.post("/search")
def do_search(
    request: Request,
    query: str = Form(""),
    category: str = Form(""),
    language: str = Form(""),
    system: str = Form(""),
    domain: str = Form(""),
    is_business_rule: bool = Form(False),
    db: Session = Depends(get_db),
):
    filters = {}
    if category:
        filters["category"] = category
    if language:
        filters["language"] = language
    if system:
        filters["system"] = system
    if domain:
        filters["domain"] = domain
    if is_business_rule:
        filters["is_business_rule"] = True

    svc_search = SearchService(db)
    svc_content = ContentService(db)
    results = svc_search.search(query=query.strip(), filters=filters)
    for item in results:
        item._tags = svc_content.get_tags(item.id)

    return templates.TemplateResponse(request, "search.html", {
        "config": config,
        "results": results,
        "query": query,
        "filters": filters,
    })
