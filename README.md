# Proyecto Territorial

Arquitectura de microservicios para análisis territorial utilizando tecnologías modernas.

## Estructura del Proyecto

- **frontend-web/**: Interfaz de usuario desarrollada en React.
- **bff-gateway/**: Backend for Frontend que orquesta las llamadas a microservicios.
- **ms-ingestion/**: Microservicio para ingesta de datos.
- **ms-transformation/**: Microservicio para transformación de datos.
- **ms-analytics-scoring/**: Microservicio para análisis y scoring.
- **ms-ml/**: Microservicio de machine learning.
- **ms-recommendations/**: Microservicio de recomendaciones.
- **ms-configuration/**: Microservicio de configuración.
- **ms-audit-trace/**: Microservicio de auditoría y trazabilidad.
- **infrastructure-local/**: Configuración Docker Compose para desarrollo local.

## Requisitos

- Docker y Docker Compose
- Node.js (para desarrollo frontend)
- Python 3.11+ (para desarrollo backend)

## Ejecución Local

1. Clona el repositorio.
2. Navega a `infrastructure-local/`.
3. Ejecuta `docker-compose up --build`.
4. Accede al frontend en http://localhost:3000.

## Desarrollo

Cada microservicio tiene su propio `requirements.txt` y Dockerfile. Para desarrollo individual:

- Backend: `uvicorn app.main:app --reload`
- Frontend: `npm start`

## Arquitectura

La aplicación sigue una arquitectura de microservicios con:
- Frontend en React consumiendo un BFF.
- BFF en FastAPI agregando datos de múltiples MS.
- MS independientes en FastAPI.
- Comunicación vía HTTP.
- Contenerización con Docker.

## Contribución

1. Crea una rama para tu feature.
2. Desarrolla y prueba.
3. Haz commit y push.
4. Crea un Pull Request.

## Licencia

[Especifica la licencia aquí]
