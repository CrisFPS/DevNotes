from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.app.database import create_tables
from backend.app.routes import content_routes, upload_routes, search_routes

app = FastAPI(title="DevNotes Local", version="0.1.0")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

app.include_router(content_routes.router)
app.include_router(upload_routes.router)
app.include_router(search_routes.router)


@app.on_event("startup")
def startup():
    create_tables()
