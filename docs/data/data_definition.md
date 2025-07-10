# Definición de los datos

## Origen de los datos

- [ ] Especificar la fuente de los datos y la forma en que se obtuvieron.

Los datos se obtuvieron de la plataforma Kaggle. Fueron recopilados de una encuesta realizada y publicada por el usuario adilshamim8. Según el mismo, la encuesta se publicó en redes sociales, permitiendo eliminar sesgos de ubicación y edad. Sin embargo, existe el sesgo de auto reporte y la forma en que fueron coleccionados los datos introduce el sesgo de que los estudiantes con acceso restringido a internet se vean sub representados.

## Especificación de los scripts para la carga de datos

- [ ] Especificar los scripts utilizados para la carga de los datos. 

El código para la carga de datos es estándar de descarga de datasets de kaggle:

```python
!pip install kagglehub[pandas-dataset]
import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "Students Social Media Addiction.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "adilshamim8/social-media-addiction-vs-relationships",
  file_path,
  # Provide any additional arguments like
  # sql_query or pandas_kwargs. See the
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())

```

## Referencias a rutas o bases de datos origen y destino

- [ ] Especificar las rutas o bases de datos de origen y destino para los datos.
Los datos se encontraban almacenados en un archivo csv y el destino es un dataframe de pandas contenido en el notebook. La ruta para encontrar los datos es /kaggle/input/social-media-addiction-vs-relationships/Students Social Media Addiction.csv. El dataframe de pandas en el notebook es siempre accesible con el comando df.

### Rutas de origen de datos

- [ ] Especificar la ubicación de los archivos de origen de los datos.
- [ ] Especificar la estructura de los archivos de origen de los datos.
- [ ] Describir los procedimientos de transformación y limpieza de los datos.

Se verificó que no hay datos faltantes, duplicados ni con diferentes formatos en el dataset. También que las variables numéricas están, en su mayoría, distribuidas normalmente, exceptuando la variable addicted_score que está sesgada a la derecha. Por otro lado, las variables categóricas sí están desequilibradas. La variable de ubicación presenta un sesgo hacia los países de norteamérica, comparado con el resto del mundo. En contraste, África escasamente presenta algunos registros. Las demás variables presentan fuertes sesgos hacia la educación superior, plataformas como tik tok, instagram y facebook y personas solteras. 

Se puede considerar hacer un balanceo de los datos y también, para variables como el nivel educativo, la eliminación por completo de la categoría 'high school'.

### Base de datos de destino

- [ ] Especificar la base de datos de destino para los datos.
- [ ] Especificar la estructura de la base de datos de destino.
- [ ] Describir los procedimientos de carga y transformación de los datos en la base de datos de destino.
