from fastapi import APIRouter
from models.tarea_model import Tarea
from services.tareas_service import (
    obtener_tareas,
    agregar_tarea,
    completar_tarea,
    eliminar_tarea
)

router = APIRouter()

@router.get("/tareas")
def ver_tareas():
    return obtener_tareas()

@router.post("/tareas")
def crear_tarea(tarea: Tarea):
    nueva = tarea.model_dump()
    agregar_tarea(nueva)
    return {"mensaje": "tarea agregada"}

@router.put("/tareas/{tarea_id}")
def completar(tarea_id: int):
    completar_tarea(tarea_id)
    return {"mensaje": "tarea completada"}

@router.delete("/tareas/{tarea_id}")
def eliminar(tarea_id: int):
    tarea = eliminar_tarea(tarea_id)
    return {"mensaje": "tarea eliminada", "tarea": tarea}