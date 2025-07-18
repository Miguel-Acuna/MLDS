# Reporte del Modelo Final

## Resumen Ejecutivo

En esta sección se presentará un resumen de los resultados obtenidos del modelo final. Es importante incluir los resultados de las métricas de evaluación y la interpretación de los mismos.

Como modelo final se eligió el modelo base. Una búsqueda de hiperparámetros en una rejilla más fina arrojó las mismas métricas sobre el conjunto de evaluación y el modelo de red neuronal, que también se desempeñó bien, no lo superó.

Las métricas de _precission_, _recall_ y _f1 score_ dieron al 95%, es decir, el modelo tiene una gran capacidad de predecir correctamente positivos y negativos. Sin embargo, en el conjunto de test, que tenía 103 registros, predijo mal 5%, es decir, aproximadamente 6 registros. Para nuestro tipo de datos, en donde no es una situación grave clasificar mal un registro, esto es un buen resultado. Si, adicionalmente, se considera que la incorrecta clasificación es gradual (si el resultado correcto es 9, no es lo mismo predecir un 8 que un 3), se encuentra que el bosque aleatorio hace un gran trabajo.

## Descripción del Problema

En esta sección se describirá el problema que se buscó resolver con el modelo final. Se debe incluir una descripción detallada del problema, el contexto en el que se desarrolla, los objetivos que se persiguen y la justificación del modelo.

El contexto del problema es la actual utilización de redes sociales entre estudiantes de secundaria y universidad. Dadas variables autoreportadas como horas de sueño, horas de uso, puntuación de salud mental, país de residencia, y conflictos en redes sociales, entre otras, el problema consistió en predecir el puntaje de adicción a las redes, medido según la escala de Bergen de adicción a redes sociales.

## Descripción del Modelo

En esta sección se describirá el modelo final que se desarrolló para resolver el problema planteado. Se debe incluir una descripción detallada del modelo, la metodología utilizada y las técnicas empleadas.

Luego de realizar experimentos con el framework optuna, se determinó que el mejor modelo fue un bosque de 69 árboles aleatorios, optimizados según el criterio de impureza de Gini y con una profundidad máxima de 11. Se registró este modelo en el framework mlflow y se procedió a probar una rejilla más detallada, donde se buscó si un bosque con el número de árboles entre 60 y 80 se desempeñaría mejor, pero no. 

Finalmente, se probó una red neuronal con una capa intermedia de 128 neuronas con activación relu y una capa de salida de 7 neuronas con activación softmax. Se entrenó el modelo durante 100 epochs y se observó que ni las métricas ni la función de pérdida mejoraron, indicando que este modelo estaba tan optimizado como se podía. El resultado final en las tres métricas fue cercano al 92%, que sin embargo se consideró bueno, aunque inferior al modelo base. 

## Evaluación del Modelo

En esta sección se presentará una evaluación detallada del modelo final. Se deben incluir las métricas de evaluación que se utilizaron y una interpretación detallada de los resultados.

El modelo final presenta métrica de precission, recall y f1 cercanas al 98% para el conjunto de validación y al 95% para el conjunto de evaluación. El modelo se dempeña bien en las categorías donde hay amplia cantidad de registros (como la 5 y la 7 de Addicted Score) y no tan bien en donde hay menor cantidad (como la 3). Esto puede indicar que el modelo necesita gran cantidad de datos, que pueden no siempre estar disponibles. Sin embargo, con la cantidad actual, clasificó correctamente 98 de los 105 registros en el conjunto de evaluación. Para el contexto de este trabajo, es un número aceptable ya que siendo un problema multiclase de 7 categorías, se está ganando 80% de precisión sobre un modelo que clasifique aleatoriamente y que cada mala clasificación no tiene repercusiones graves sobre los sujetos de estudio.

## Conclusiones y Recomendaciones

En esta sección se presentarán las conclusiones y recomendaciones a partir de los resultados obtenidos. Se deben incluir los puntos fuertes y débiles del modelo, las limitaciones y los posibles escenarios de aplicación.

Se recomiienda usar el modelo base para predicción de registros de adicción a redes sociales entre estudiantes. El modelo logró predecir correctamente el 95% de los casos, aunque flaqueó en situaciones en que hubo pocos datos. Esta limitación podría corregirse sacando mayor ventaja de la correlación entre las variables de entrada y la objetivo, por ejemplo, usando un regresor multilineal. 

Posibles escenarios de aplicación incluyen toma de decisiones en políticas educativas y regulatorias de contenido multimedia, diseño de políticas públicas en escuelas y universidades y mayor consciencia de los estudiantes sobre cómo usan sus redes sociales, llevándoles a ser más independietes y sanos.

## Referencias

En esta sección se deben incluir las referencias bibliográficas y fuentes de información utilizadas en el desarrollo del modelo.
