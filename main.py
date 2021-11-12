from fastapi import FastAPI, Path
from sqlalchemy import select
from config.db import conn
from models.location import locations
from models.location_observation import location_observations
from models.system import systems
from models.system_observation import system_observations
from models.ml_model import ml_models
from models.prediction import predictions
from models.metric import metrics
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def index():
    return "Este es el servidor de PV Forecasting App. " + \
        "Aplicación: " + "https://google.com" + \
        " Documentación del servidor: " + ""


@app.get("/listar-ubicaciones")
def listar_ubicaciones():
    # stmt = select(locations, systems).join_from(locations, systems, locations.c.location_id==systems.c.location_id)

    # stmt = conn.query(locations, systems)

    # stmt = select(ml_models, systems).join_from(
    #     ml_models, systems,
    #     ml_models.c.system_id == systems.c.system_id)

    # stmt2 = select(ml_models.c.model_name, locations.c.label).join_from(stmt,
    #

    # stmt = '''
    #     SELECT m.ml_model_id as id_ubicacion_modelo, CONCAT(l.label," - ",l.city,", ", l.region, " (",s.technology,")") as texto_ubicacion,
    #              m.model_name, m.description, m.image_path, m.is_trasfered, m.origin_system, s.technology, l.label, l.full_name, l.region, l.city
    #     FROM DBTesis.ml_models as m
    #     JOIN DBTesis.systems as s
    #     ON m.system_id = s.system_id
    #     JOIN DBTesis.locations as l
    #     ON l.location_id = s.location_id;
    # '''
    stmt = '''
        SELECT m.ml_model_id as id_ubicacion_modelo, CONCAT(l.label," - ",l.city,", ", l.region, " (",s.technology,")") as texto_ubicacion,
                 m.model_name, CONCAT("Este modelo fue entrenado con datos recolectado en las instalaciones de la ", l.full_name, " en ",l.city,", ", l.region, ".") as description,
                 m.image_path, m.is_trasfered, m.origin_system, s.technology, l.label, l.full_name, l.region, l.city 
        FROM DBTesis.ml_models as m
        JOIN DBTesis.systems as s
        ON m.system_id = s.system_id
        JOIN DBTesis.locations as l
        ON l.location_id = s.location_id;
    '''
    data = conn.execute(stmt).fetchall()
    return data
    # return list(map(lambda x: x['label']+" - "+x['technology'], data))

# @app.get("/imagen-ubicacion/{id_ubicacion_modelo}")
# def get_imagen_ubicacion(id_ubicacion_modelo: int):
#     if not isinstance(id_ubicacion_modelo, int): return None

#     stmt = f'SELECT m.image FROM DBTesis.ml_models as m WHERE m.ml_model_id = {id_ubicacion_modelo};'
#     print(stmt)
#     image =  conn.execute(stmt).fetchall()
#     print(type(image[0][0]))
#     return image


@app.get("/fechas-limite")
def get_fechas_limite():
    fecha_min = datetime.date(2020, 2, 24)
    now = datetime.datetime.now()
    now = datetime.date(2020, 10, 20)
    
    fecha_max = now.date() if now.hour < 17 else now.date() + \
        datetime.timedelta(days=1)
    return {"min_date": fecha_min, "max_date": fecha_max}


@app.get("/listar-graficos-metricas")
def listar_graficos_metricas():

    stmt = '''
        SELECT mo.ml_model_id as id_ubicacion_modelo, me.metric_id, me.metric_name,me.date, me.value, me.metric_image_path
        FROM DBTesis.ml_models as mo
        JOIN DBTesis.metrics as me
        ON mo.ml_model_id = me.ml_model_id;
    '''
    data = conn.execute(stmt).fetchall()
    return data


@ app.get("/locations")
def get_locations():
    return conn.execute(locations.select()).fetchall()


@ app.get("/systems")
def get_systems():
    return conn.execute(systems.select()).fetchall()


@ app.get("/location_observations")
def get_location_observations():
    return conn.execute(location_observations.select()).fetchall()


@ app.get("/system_observations")
def get_system_observations():
    return conn.execute(system_observations.select()).fetchall()


@ app.get("/ml_models")
def get_ml_models():
    return conn.execute(ml_models.select()).fetchall()


@ app.get("/predictions")
def get_predictions():
    return conn.execute(predictions.select()).fetchall()


@ app.get("/metrics")
def get_metrics():
    return conn.execute(metrics.select()).fetchall()


# students = {
#     1: {
#         "name": "john",
#         "age": 17,
#         "year": "year 12"
#     }
# }


# class Student(BaseModel):
#     name: str
#     age: int
#     year: str


# class UpdateStudent(BaseModel):
#     name: Optional[str] = None
#     age: Optional[int] = None
#     year: Optional[str] = None


# @app.get("/")
# def index():
#     return {"name": "First Data"}


# @ app.get("/get-student/{student_id}")
# def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=3)):
#     return students[student_id]


# @ app.get("/get-by-name/{student_id}")
# def get_student(*, student_id: int, name: Optional[str] = None, test: int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data": "Not found"}

# @app.post("/create-student/{student_id}")
# def create_student(student_id : int, student : Student):
#     if student_id in students:
#         return {"Error": "Student exists"}

#     students[student_id] = student
#     return students[student_id]

# @app.put("/update-student/{student_id}")
# def update_student(student_id: int, student: UpdateStudent):
#     if student_id not in students:
#         return {"Error": "Student does not exist"}

#     if student.name != None:
#         students[student_id].name = student.name

#     if student.age != None:
#         students[student_id].age = student.age

#     if student.year != None:
#         students[student_id].year = student.year

#     return students[student_id]

# @app.delete("/delete-student/{student_id}")
# def delete_student(student_id: int):
#     if student_id not in students:
#         return {"Error": "Student does not exist"}

#     del students[student_id]
#     return {"Message": " Student deleted successfully"}
