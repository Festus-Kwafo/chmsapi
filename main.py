import uvicorn
from path import Path

from src.chmsapi.common.logs import log
from src.chmsapi.config.registrar import register_app
from src.chmsapi.config.settings import settings

app = register_app()


@app.get("/")
async def index():
    return {"detail": "API Working "}


if __name__ == "__main__":
    try:
        log.info("Start FastAPI Application")
        uvicorn.run(f"{Path(__file__).stem}:app", host=settings.UVICORN_HOST, port=settings.UVICORN_PORT,
                    reload=settings.UVICORN_RELOAD)
    except Exception as e:
        log.error(f"❗ Application failed to start: {e}")
