from fastapi import APIRouter, Depends, File, Form, Request, UploadFile
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.app.config import config
from backend.app.database import get_db
from backend.app.services.content_service import ContentService
from backend.app.services.upload_service import save_upload

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")


@router.get("/upload")
def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {
        "request": request,
        "config": config,
        "error": None,
    })


@router.post("/upload")
async def process_upload(
    request: Request,
    file: UploadFile = File(...),
    title: str = Form(""),
    category: str = Form(""),
    system: str = Form(""),
    domain: str = Form(""),
    is_business_rule: bool = Form(False),
    tags: str = Form(""),
    db: Session = Depends(get_db),
):
    try:
        file_meta = await save_upload(file)
    except Exception as exc:
        return templates.TemplateResponse("upload.html", {
            "request": request,
            "config": config,
            "error": str(exc),
        }, status_code=400)

    effective_title = title.strip() or file_meta["original_name"]
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]

    svc = ContentService(db)
    new_item = svc.create({
        "title": effective_title,
        "content": file_meta["text_content"] or "",
        "category": category,
        "language": file_meta["language"],
        "system": system,
        "domain": domain,
        "object_type": file_meta["object_type"],
        "is_business_rule": is_business_rule,
        "tags": tag_list,
    })
    svc.attach_file(new_item.id, file_meta)

    return RedirectResponse(f"/content/{new_item.id}", status_code=303)
