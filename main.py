from fastapi import FastAPI
from routes.tareas_routes import router
from services.tareas_service import cargar_tareas

app = FastAPI()

cargar_tareas()

app.include_router(router)