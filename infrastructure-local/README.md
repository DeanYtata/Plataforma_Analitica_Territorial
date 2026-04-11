# Infrastructure Local

## Descripción
Configuración de Docker Compose para ejecutar el proyecto territorial de manera integrada.

## Servicios
- **frontend-web**: Interfaz web en React (puerto 3000)
- **bff-gateway**: Backend for Frontend (puerto 8000)
- **ms-ingestion**: Microservicio de ingesta de datos (puerto 8001)
- **ms-transformation**: Microservicio de transformación (puerto 8002)
- **ms-analytics-scoring**: Microservicio de analytics y scoring (puerto 8003)
- **ms-ml**: Microservicio de machine learning (puerto 8004)
- **ms-recommendations**: Microservicio de recomendaciones (puerto 8005)
- **ms-configuration**: Microservicio de configuración (puerto 8006)
- **ms-audit-trace**: Microservicio de auditoría (puerto 8007)

## Ejecución
1. Asegurarse de tener Docker y Docker Compose instalados.
2. Ejecutar `docker-compose up --build` desde esta carpeta.
3. Acceder al frontend en http://localhost:3000

## Variables de Entorno
Ver archivo .env para configuración de puertos.