Visualización de Datos con FastAPI, Svelte y eCharts
Descripción
Aplicación FullStack que permite visualizar datos en gráficos utilizando FastAPI para el backend y Svelte para el frontend.

La aplicación consume datos desde un archivo data.json y los representa en un gráfico circular (pie chart) y un gráfico de barras (bar plot) utilizando la librería eCharts.

Tecnologías usadas
Backend: FastAPI
Frontend: Svelte, Javascript
Visualización de datos: eCharts.js
Servidor web: Uvicorn
Docker: Despliegue

Instalación y Ejecución
1. Clonar el Repositorio
git clone <https://github.com/jonasnisni/appfull.git >
cd <proyectofull>

2. Ejecución con Docker
Con Docker y Docker Compose instalados. Luego, ejecuta:
docker-compose up --build

3. Acceder
El backend servirá los datos(data.json) desde:

http://localhost:8000/data

Puedes visualizar el frontend desde : 

http://localhost:5173

API
Endpoint Disponible
GET /data - Retorna los datos almacenados en data.json.
{
  "piechart": {
    "labels": ["Producto A", "Producto B", "Producto C", "Producto D"],
    "values": [25, 30, 20, 25]
  },
  "barplot": {
    "categories": ["Enero", "Febrero", "Marzo", "Abril"],
    "values": [150, 200, 180, 220]
  }
}

Construcción y Despliegue Manual

1. Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

3. Frontend
cd frontend
npm install
npm run build

Autor : Nisnievich Jonas. 


