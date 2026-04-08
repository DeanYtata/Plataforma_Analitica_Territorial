# Plataforma Analítica Territorial

Sistema de análisis territorial integrado con arquitectura microservicios.

## 📋 Requisitos

- Docker 20.10+
- Docker Compose 2.0+
- Python 3.13+ (para desarrollo local)

## 🚀 Inicio rápido

### Con Docker Compose

```bash
docker-compose up -d
```

Servicios disponibles:
- **Frontend**: http://localhost
- **Backend**: http://localhost:5000
- **Health Check**: http://localhost:5000/api/health

### Desarrollo Local

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
cd backend
pip install -r requirements.txt

# Ejecutar backend
python app.py
```

## 📁 Estructura del Proyecto

```
.
├── backend/
│   ├── app.py                 # Aplicación Flask principal
│   ├── requirements.txt       # Dependencias Python
│   ├── Dockerfile             # Configuración Docker
│   ├── controllers/           # Controladores de rutas
│   ├── services/              # Lógica de negocio
│   └── interfaces/            # Interfaces de respuesta
├── frontend/
│   ├── index.html             # Página principal
│   └── Dockerfile             # Configuración Docker
├── docker-compose.yml         # Orquestación de servicios
└── README.md                  # Este archivo
```

## 🔧 Configuración

### Variables de Entorno (Backend)

```env
FLASK_ENV=production
PORT=5000
```

## 📊 API Endpoints

### Health Check
```http
GET /api/health
```

### Datasets
```http
GET /api/datasets
POST /api/datasets
```

Ejemplo de inserción:
```json
{
  "name": "Censo territorial",
  "description": "Dataset cargado manualmente para prueba",
  "source": "manual",
  "payload": {
    "municipio": "Ejemplo",
    "valor": 123
  }
}
```

Para una prueba manual contra la base SQLite local, ejecutar:
```bash
cd backend
/usr/bin/python3 scripts/seed_dataset.py
```

Respuesta:
```json
{
  "message": "Health check response",
  "data": {
    "status": "healthy",
    "version": "1.0.0"
  }
}
```

## 🐛 Solución de Problemas

### Los contenedores no inician
```bash
# Ver logs
docker-compose logs -f

# Reiniciar servicios
docker-compose restart
```

### Puerto en uso
```bash
# Si el puerto 80 o 5000 está en uso
docker-compose down
# Modificar puertos en docker-compose.yml
docker-compose up -d
```

## 📝 Licencia

Todos los derechos reservados.

## 👥 Contacto

Para más información, contactar al equipo de desarrollo.
