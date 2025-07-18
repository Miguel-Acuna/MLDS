# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores.

Como modelo base se eligió un bosque aleatorio. Inicialmente se hizo una búsqueda en rejilla y se encontró que un bosque con 69 árboles, una profundidad máxima de 11 capas y una función de pérdida de impureza gini daba los mejores resultados.

## Variables de entrada

Lista de las variables de entrada utilizadas en el modelo.

Se utilizaron todas las variables, excepto 'Student_id'. Las variables categóricas se codificaron con la técnica One Hot, incluyendo la variable 'Country'. La variable 'Academic_Level' se convirtió a ordinal, asignando el valor 1 a High School, 2 a Undergraduate y 3 a Graduate. A las variables numéricas no se les hizo preprocesamiento. La lista de variables usadas es:
_Age_, _Gender_, _Academic_Level_, _Country_, _Avg_Daily_Usage_Hours_, _Most_Used_Platform_, _Affects_Academic_Performance_, _Sleep_Hours_Per_Night_, _Mental_Health_Score_, _Relationship_Status_ y _Conflicts_Over_Social_Media_.

## Variable objetivo

Nombre de la variable objetivo utilizada en el modelo.

La varible objetivo utilizada fue 'Addicted_Score', ordinal. En principio 10 valores son posibles, valores enteros del 0 al 9. Sin embargo, los datos reales mostraron que solo asumió valores enteros entre el 3 y el 9, incluidos.

## Evaluación del modelo

### Métricas de evaluación

Descripción de las métricas utilizadas para evaluar el rendimiento del modelo.

Dado que el nuestro era un problema de clasificación, se decidió utilizar las métricas _precission_, _recall_ y _f1 score_. Dado que son 7 categorías distintas en las que es posible clasificar una observación, y que las categorías 7 y 5 de _Addicted Score_ tenían muchísimas más observaciones que el resto, se toman los promedios ponderados de dichas métricas.

### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

|           | precision|   recall| f1-score|  support|
|-----------|----------|---------|---------|---------|
|          3|      1.00|     0.67|     0.80|        3|
|          4|      0.90|     1.00|     0.95|       18|
|          5|      0.92|     1.00|     0.96|       23|
|          6|      1.00|     0.80|     0.89|       10|
|          7|      0.97|     1.00|     0.98|       31|
|          8|      1.00|     0.93|     0.96|       14|
|          9|      1.00|     1.00|     1.00|        6|
|   accuracy|          |         |     0.95|      106|
|  macro avg|      0.85|     0.80|     0.82|      106|
|weighted avg|     0.95|     0.95|     0.95|      106|

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

Se puede ver que en general el modelo se desempeña muy bien, logrando 95% de éxito en cada métrica. Es claro que cuando hay menos muestras en una categoría, como por ejemplo en la 3, no tiene muchas oportunidades de clasificar y un error es mucho más costoso, por lo que produce peores resultados en esa categoría. Por el contrario, cuando tiene muchísimas muestras (como en las categorías 7 y 5), se comporta mucho mejor.

## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora.

Este modelo es bastante apropiado dado el tipo de datos tabular. Sin embargo, un área de mejora del modelo es que es posible tomar más ventaja de la alta correlación entre algunas de las variables de entrada y la variable objetivo. Será interesante explorar un modelo de regresión multilineal adaptada a un problema categórico. También se explorará una red neuronal sencilla.

## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Espero que te sea útil esta plantilla. Recuerda que puedes adaptarla a las necesidades específicas de tu proyecto.
