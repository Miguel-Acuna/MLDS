# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

En esta sección se presenta un resumen general de los datos. Se describe el número total de observaciones, variables, el tipo de variables, la presencia de valores faltantes y la distribución de las variables.

El conjunto de datos consta de 705 observaciones y 13 características. Se corroboró que no hay valores faltantes, duplicados, corruptos ni en formatos distintos. Se descartó una variable y de las 12 restantes, 6 fueron numéricas y 6 categóricas. La variable objetivo, 'addicted score', es también de tipo numérico discreto, asumiendo valores enteros entre el 1 y el 10. La distribución de las variables numéricas es normal en general, excepto por la variable objetivo que presenta un sesgo a la izquierda.

## Resumen de calidad de los datos

En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problemas.

Se corroboró que no hay valores duplicados, faltantes ni erróneos. También se evidencia que entre las variables categóricas no hay valores fuera de los esperados en cada categoría. Esto es, no hay errores de tipeo ni nada por el estilo. Se decidió conservar los valores extremos ya que eran plausibles, consistentes con la distribución y se consideró que aportaban información valiosa.

## Variable objetivo

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

La variable objetivo se podría modelar con una distribución Beta con parámetros alfa=8 y beta=4, de modo que se modela una distribución sesgada a la izquierda. El valor máximo de addicted score es 9 y el más repetido es 8, seguido del 5. El valor 2 solamente se presenta solamente un puñado de veces. 

## Variables individuales

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

Entre las variables numéricas, todas excepto la variable objetivo tienen practicamente una distribución normal y sin valores extremos. Las variables categóricas son en general balanceadas, aunque la del nivel educativo presenta un desbalanceo muy significativo en los estudiantes de secundaria respecto de los de pregrado y posgrado. Así mismo, la variable estado civil presenta un desbalanceo significativo de la categoría "complicado" respecto de las otras dos. También la variable de la plataforma más usada favorece a instagram, tik tok, facebook y whatsapp muy por encima de las demás, como cabría esperar. En esta variable en particular, se pueden dejar solo estas 4 categorías y eliminar el resto, ya que aportan ruido solamente.

## Ranking de variables

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

En el gráfico de correlaciones de variables numéricas con la variable objetivo, es claro que las variables más explicativas son los conflictos en redes sociales y las horas de uso diarias promedio. Así mismo, está muy correlacionada negativamente con el puntaje de salud mental.

En cuanto a las variables categóricas, la relación con la variable objetivo será objeto de investigación y modelamiento, ya que en este momento no es clara. Se hará una codificación one hot y se hará un modelo de regresión multilineal.

