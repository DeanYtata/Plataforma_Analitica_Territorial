from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, Response
from sqlalchemy.orm import Session
import jinja2
import traceback

from app.controllers.etl_controller import router
from app.database.connection import Base, engine, get_db
from app.models.dataset import Dataset, EliminatedData  # 🔥 AGREGADO

# Crear tablas en PostgreSQL
Base.metadata.create_all(bind=engine)

# Configuración de templates
template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"),
    cache_size=0
)

app = FastAPI()

app.include_router(router)

# ============================================================
# ROOT (INFO GENERAL)
# ============================================================
@app.get("/")
def root():
    return {
        "nombre": "🔄 Data Ingestion Service - ETL",
        "endpoints": {
            "upload": "POST /etl/upload",
            "ver_tabla": "GET /view-data",
            "ver_json": "GET /api/data",
            "descargar": "GET /download-csv"
        }
    }

# ============================================================
# VER DATOS EN HTML (🔥 AHORA CON ELIMINADOS)
# ============================================================
@app.get("/view-data")
def view_data(request: Request, db: Session = Depends(get_db)):
    try:
        datasets = db.query(Dataset).filter(Dataset.ciudad != "").all()

        # 🔥 NUEVO: TRAER DATOS ELIMINADOS
        eliminated = db.query(EliminatedData).all()

        template = template_env.get_template("view_data.html")

        content = template.render(
            request=request,
            datasets=datasets,
            eliminated=eliminated  # 🔥 SE ENVÍA AL HTML
        )

        return HTMLResponse(content)

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}

# ============================================================
# VER DATOS EN JSON
# ============================================================
@app.get("/api/data")
def get_data(db: Session = Depends(get_db)):
    datasets = db.query(Dataset).filter(Dataset.ciudad != "").all()

    return [
        {
            "id": d.id,
            "ciudad": d.ciudad,
            "ingresos": d.ingresos,
            "poblacion": d.poblacion
        }
        for d in datasets
    ]

# ============================================================
# DESCARGAR CSV DESDE BD
# ============================================================
@app.get("/download-csv")
def download_csv(db: Session = Depends(get_db)):

    datasets = db.query(Dataset).filter(Dataset.ciudad != "").all()

    csv_data = "ciudad,ingresos,poblacion\n"

    for d in datasets:
        csv_data += f"{d.ciudad},{d.ingresos},{d.poblacion}\n"

    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=datos_limpios.csv"
        }
    )