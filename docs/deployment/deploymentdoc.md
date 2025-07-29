# Despliegue de modelos (Con CLI)

## Infraestructura

- **Nombre del modelo:** Modelo para predecir nivel de addicion a redes sociales

- **Plataforma de despliegue:** La desplegaremos a traves de linea de comandos CLI, tambien tendremos una version API sostenida en Docker
- **Requisitos técnicos:** Version de librerias

|Package                            | Version |
|-----------------------------------|---------|
|kagglehub                          |   0.3.12|
|keras                              |   3.8.0 |
|mlflow                             |   3.1.4 |
|numpy                              |   2.0.2 |
|optuna                             |   4.4.0 |
|pandas                             |   2.2.2 |
|pip                                |   24.1.2| 
|pyngrok                            |   7.2.12|
|scikit-learn                       |   1.6.1 |
|seaborn                            |   0.13.2|



- **Requisitos de seguridad:** (lista de requisitos de seguridad necesarios para el despliegue, como autenticación, encriptación de datos, etc.) Es necesario autenticarse en ngrok e iniciar una sesión en mlflow. No hay otros requisitos de seguridad.
- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)
```text
┌─────────────────────┐
│    Desarrollador    │
│                     │
└────────┬────────────┘
         │
         ▼
┌────────────────────────┐
│ 1. Desarrollo de       │
│    la librería         │
│  (funciones, clases,   │
│   módulos, setup.py)   │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ 2. Publicación en      │
│    repositorio         │
│  (Ej: PyPI, GitHub)    │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────────┐
│ 3. Usuario final (cliente) │
│    quiere usar tu cod      │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────┐
│ 4. Descarga de         │
│    la librería         │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ 6. Uso de las funciones│
│    y clases            │
│                        │
└────────────────────────┘
```

## Código de despliegue

- **Archivo principal:** deploy.py
- **Rutas de acceso a los archivos:** MLDS/src/deploy.py
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:** No es necesario instalar ningún programa ni complemento, ya que el despliegue se hace a través de CLI.
- **Instrucciones de configuración:** Es necesario correr el notebook modelamiento primero para configurar el modelo, inicializar mlflow y conectar con ngrok. Ya el modelo está construido, por lo que es solo necesario correr el notebook.
- **Instrucciones de uso:** El uso del archivo es la siguiente: en la línea de comandos se debe usar python -p path_to_file.csv Es decir, se debe entregar un archivo csv en donde se haya guardado un dataframe de pandas con todas las variables necesarias para el modelo. Las variables categóricas se deben haber codificado según el método OneHot. Por favor ver el notebook deployment.ipynb ubicado en la ruta MLDS/scripts/deployment/deployment.ipynb para un ejemplo.
