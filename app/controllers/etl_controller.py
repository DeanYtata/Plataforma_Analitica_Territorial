from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.responses import Response

from app.database.connection import get_db
from app.services.etl_service import procesar_csv, generar_csv

router = APIRouter(prefix="/etl")


# 📌 Modelo para procesar archivos locales
class ProcessLocalRequest(BaseModel):
    path: str


# ✅ SUBIR CSV DESDE POSTMAN
@router.post("/upload")
def upload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        datos = procesar_csv(file, db)
        return {
            "mensaje": "✅ CSV procesado correctamente",
            "archivo": file.filename,
            "registros_procesados": len(datos)
        }
    except Exception as e:
        return {"error": str(e)}


# ✅ VER DATOS LIMPIOS
@router.get("/data")
def ver_datos():
    from app.services.etl_service import datos_limpios
    return datos_limpios


# ⚠️ OPCIONAL (MEJOR ELIMINAR SI NO LO NECESITAS)
@router.post("/process-local")
def process_local(request: ProcessLocalRequest):
    return {
        "mensaje": "⚠️ Este endpoint no está implementado completamente",
        "ruta_recibida": request.path
    }


# ✅ DESCARGAR CSV
@router.get("/download")
def download():
    csv_data = generar_csv()
    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=datos_limpios.csv"
        }
    )