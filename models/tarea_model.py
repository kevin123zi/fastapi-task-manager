from pydantic import BaseModel

class Tarea(BaseModel):
    descripcion: str
    completada: bool = False