# Despliegue de modelos (Con FastApi)

## Infraestructura

- **Nombre del modelo:** Modelo para predecir nivel de addicion a redes sociales

- **Plataforma de despliegue:** Despliegue realizado con FastAPI y Docker en la plataforma Railway, permitiendo exponer una API REST que consume un modelo de Machine Learning entrenado con Scikit-learn.
- **Requisitos técnicos:** Version de librerias

|Package                            |  Version |
|-----------------------------------|----------|
|fastapi                            |   0.110.1|
|uvicorn                            |   0.29.0 |
|joblib                             |   1.4.2  |
|jinja2                             |   3.1.4  |
|pandas                             |   2.2.2  |
|python-multipart                   |   0.0.9  | 
|scikit-learn                       |   1.6.1  |

- **Diagrama de arquitectura:** 

+---------------------+
|    Usuario final    |
| (navegador o cURL)  |
+---------+-----------+
          |
          v
+---------------------+
|    Railway Platform |
|    (Infraestructura)|
+---------------------+
          |
          v
+---------------------+
|    Docker container |
|   ----------------  |
|   | FastAPI app   | |
|   | sklearn model | |
+---------------------+
          |
          v
+---------------------+
|     Modelo ML       |
| (Scikit-learn .pkl) |
+---------------------+

## Código de despliegue

- **Archivo principal:** deploy.py
- **Rutas de acceso a los archivos:** MLDS/src/app/__init__.py

## Documentación del despliegue

## Documentación del despliegue

### Instrucciones de instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Miguel-Acuna/MLDS.git
   cd tu-repo
   ```

2. **Construir la imagen Docker:**

   ```bash
   docker build -t addicted-model-app .
   ```

3. **Ejecutar el contenedor localmente:**

   ```bash
   docker run -d --name addicted-app-container -p 8000:8000 addicted-model-app
   ```

   Esto levantará el API en: [http://localhost:8000](http://localhost:8000)

---

### ⚙️ Instrucciones de configuración

* **Dockerfile base:**

  ```dockerfile
  FROM python:3.11-slim

  WORKDIR /app

  COPY . .

  RUN pip install --no-cache-dir -r requirements.txt

  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

* **Variables de entorno necesarias (opcional):**

  ```env
  PORT=8000 (Para despliegue local)
  ```

  Railway puede autogestionar el puerto (`PORT`) sin necesidad de definirlo explícitamente.

---

### 🚀 Instrucciones de uso

#### Acceso local:

Una vez ejecutado el contenedor con Docker, abre tu navegador en:

```
http://localhost:8000
```

* Accede a la interfaz de usuario para ingresar los datos del formulario.
* También puedes probar la API directamente en:

  ```
  http://localhost:8000/docs
  ```

  (Swagger UI para probar endpoints)

#### Acceso en Railway:

1. Crea un nuevo proyecto en [https://railway.app](https://railway.app).
2. Selecciona **Deploy from GitHub repo** y conecta tu repositorio.
3. Railway detectará el `Dockerfile` y construirá la imagen automáticamente.
4. Una vez desplegado, se te asignará un dominio público, por ejemplo:

   ```
   https://addicted-model-app.up.railway.app
   ```
5. El sistema estará accesible vía navegador o herramientas como `curl`, `Postman`, etc.


