import logging
import logging.handlers

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import employees, health, settings, signature
from app.core.config import settings as app_settings

_log_level = logging.DEBUG if app_settings.app_debug else logging.INFO
_log_format = "%(asctime)s %(levelname)s %(name)s %(message)s"
_handlers: list[logging.Handler] = [logging.StreamHandler()]

if app_settings.log_file:
    _handlers.append(
        logging.handlers.RotatingFileHandler(
            app_settings.log_file,
            maxBytes=10 * 1024 * 1024,
            backupCount=3,
            encoding="utf-8",
        )
    )

logging.basicConfig(level=_log_level, format=_log_format, handlers=_handlers)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Gerador de Assinatura de E-mail",
    description="API interna para geração padronizada de assinaturas - BT Blue",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(health.router)
app.include_router(signature.router)
app.include_router(settings.router)
app.include_router(employees.router)


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    logger.debug("index page requested")
    return templates.TemplateResponse(request, "pages/index.html")


logger.info("Application startup complete", extra={"env": app_settings.app_env})
