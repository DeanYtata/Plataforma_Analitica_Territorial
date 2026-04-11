# 🔄 Procesos ETL - Data Ingestion Service

## ✅ 6 Puntos del Proceso de Limpieza

### 1️⃣ **CARGAR ARCHIVO CSV DESDE LOCAL**
📍 **Ubicación en el código:** `app/services/etl_service.py` línea ~27
- Lee el archivo CSV línea por línea
- Salta el encabezado (primera fila)
- Extrae ciudad, ingresos y población

**Cómo verlo:**
- Sube un CSV en Postman: `POST http://127.0.0.1:8000/etl/upload`
- O carga desde archivo local: `POST http://127.0.0.1:8000/etl/process-local`
  ```json
  {"path": "C:/ruta/al/archivo.csv"}
  ```

---

### 2️⃣ **ELIMINAR NULOS (filas con campos vacíos)**
📍 **Ubicación en el código:** `app/services/etl_service.py` línea ~47
- Valida que ciudad, ingresos y población no estén vacíos
- Si falta alguno, imprime aviso: `⚠️ FILA IGNORADA (nulo)`

**Cómo verlo:**
- Mira la consola/terminal del servidor
- Verás líneas como: `⚠️ FILA IGNORADA (nulo): ['', '1200', '1300000']`

---

### 3️⃣ **ELIMINAR DUPLICADOS**
📍 **Ubicación en el código:** `app/services/etl_service.py` línea ~54
- Crea una clave única: `ciudad+ingresos+poblacion`
- Si ya existe, no la guarda e imprime: `⚠️ FILA IGNORADA (duplicado)`

**Cómo verlo:**
- Nuevamente en la consola/terminal
- Verás: `⚠️ FILA IGNORADA (duplicado): bogota, 1000, 8000000`

---

### 4️⃣ **NORMALIZAR DATOS**
📍 **Ubicación en el código:** `app/services/etl_service.py` línea ~38-45
Hace 3 cosas:
- **Quita espacios:** `" bogota "` → `"bogota"`
- **Convierte a minúsculas:** `"BOGOTA"` → `"bogota"`
- **Conversión de tipos:** 
  - `ingresos` (string) → float
  - `poblacion` (string) → int

**Cómo verlo:**
- Compara antes y después en los endpoints:
  - `GET /api/data` (datos procesados)

---

### 5️⃣ **IMPRIMIR RESULTADO LIMPIO**
📍 **Ubicación en el código:** `app/services/etl_service.py` línea ~72-87
- Imprime en la consola/terminal del servidor
- Formato bonito:
```
============================================================
✅ DATOS LIMPIOS (guardados en PostgreSQL):
============================================================
  • BOGOTA              | Ingresos: $   1000.0 | Población:    8000000
  • MEDELLIN            | Ingresos: $   2000.0 | Población:    2500000
  • CALI                | Ingresos: $   1500.0 | Población:    2200000
============================================================
```

**Cómo verlo:**
- Mira la terminal/consola del servidor después de subir el CSV

---

### 6️⃣ **GUARDAR RESULTADO (archivo o variable)**
📍 **Ubicaciones en el código:**
- **En PostgreSQL (base de datos):** `app/repositories/dataset_repository.py`
- **En memoria (variable global):** `app/services/etl_service.py` línea ~70
- **Descargar como archivo CSV:** `/download-csv` endpoint

**Cómo verlo:**

#### Opción A: Ver en PostgreSQL (tabla web)
```
GET http://127.0.0.1:8000/view-data
```
Abre en navegador → Tabla HTML con todos los datos

#### Opción B: Ver en JSON (Postman)
```
GET http://127.0.0.1:8000/api/data
```
Devuelve:
```json
[
  {"id": 1, "ciudad": "bogota", "ingresos": 1000.0, "poblacion": 8000000},
  {"id": 2, "ciudad": "medellin", "ingresos": 2000.0, "poblacion": 2500000},
  ...
]
```

#### Opción C: Descargar como CSV
```
GET http://127.0.0.1:8000/download-csv
```
Descarga un archivo: `datos_limpios.csv`

---

## 📊 Flujo Completo

```
CSV (entrada)
    ↓
[1] Se carga en memoria (CARGAR)
    ↓
[2] Se filtran filas vacías (ELIMINAR NULOS)
    ↓
[3] Se eliminan duplicados (ELIMINAR DUPLICADOS)
    ↓
[4] Se normalizan los datos (NORMALIZAR)
    ↓
[5] Se imprime en consola el resultado limpio (IMPRIMIR)
    ↓
[6] Se guarda en PostgreSQL + en variable global (GUARDAR)
    ↓
[CSV descargable / API JSON / Página HTML] (salida)
```

---

## 🚀 Endpoints Disponibles

| Método | URL | Descripción |
|--------|-----|-------------|
| POST | `/etl/upload` | Subir CSV desde Postman (form-data) |
| POST | `/etl/process-local` | Procesar CSV desde ruta local (JSON) |
| GET | `/view-data` | Ver tabla HTML en navegador |
| GET | `/api/data` | Ver datos en JSON (Postman) |
| GET | `/download-csv` | Descargar CSV limpio |

---

## 🔧 Cómo Usar en Postman

### Subir CSV (form-data)
```
POST http://127.0.0.1:8000/etl/upload

Body → form-data:
  Key: file
  Value: (selecciona tu archivo .csv)

Response: {"mensaje": "CSV procesado correctamente"}
```

### Procesar desde archivo local
```
POST http://127.0.0.1:8000/etl/process-local

Body → raw JSON:
{
  "path": "C:/Users/wilfr/Desktop/datos.csv"
}

Response: {"mensaje": "CSV local procesado correctamente"}
```

### Ver datos limpios
```
GET http://127.0.0.1:8000/api/data

Response: [
  {"id": 1, "ciudad": "bogota", ...},
  ...
]
```

### Descargar CSV
```
GET http://127.0.0.1:8000/download-csv

Response: archivo CSV descargable
```

---

## 📝 Resumen

✅ **Cargar CSV:** `/etl/upload` o `/etl/process-local`  
✅ **Eliminar nulos:** Automático (ve los avisos en la consola)  
✅ **Eliminar duplicados:** Automático (ve los avisos en la consola)  
✅ **Normalizar datos:** Automático (ciudad minúsculas, conversión de tipos)  
✅ **Imprimir limpio:** Consola/terminal del servidor  
✅ **Guardar:** PostgreSQL + JSON `/api/data` + CSV `/download-csv` + HTML `/view-data`
