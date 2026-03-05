import json

tareas = []

def cargar_tareas():
    global tareas
    try:
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)
    except FileNotFoundError:
        tareas = []

def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo, indent=4)

def obtener_tareas():
    return tareas

def agregar_tarea(tarea):
    tareas.append(tarea)
    guardar_tareas()

def completar_tarea(id):
    tareas[id]["completada"] = True
    guardar_tareas()

def eliminar_tarea(id):
    tarea = tareas.pop(id)
    guardar_tareas()
    return tarea