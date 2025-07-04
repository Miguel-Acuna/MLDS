# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Análisis de la adicción a los teléfonos inteligentes en estudiantes.

## Objetivo del Proyecto

El objetivo del proyecto es desarrollar un modelo de aprendizaje de máquina (Machine Learning) que sea capaz de predecir si un
estudiante es adicto a su teléfono inteligente o no, dadas variables como horas de sueño, auto percepción del rendimiento académico y
horas de uso diarias promedio.

El uso compulsivo de los teléfonos inteligente no está lejos de ninguna de las personas en el mundo moderno. En particular, como lo 
señalan Freitas et al.[^fn1], el número de estudios del uso de teléfonos inteligentes en adolescentes creció en aproximadamente 32\% 
por año entre 2009 y 2019, lo que demuestra el creciente interés en esta población. Sin embargo, Kumar [^fn2] recuerda que no es un panorama tan sencillo, ya que el teléfono inteligente
es realmente una herramienta de productividad en los estudiantes, rendición de cuentas y presencia social. La situación, dice el mismo,
se complica al involucrar la salud mental de los usuarios.

En conclusión, estudios cuantitativos del asunto son necesarios y pertinentes. Un modelo que sea capaz de predecir y alertar con anticipación
si un estudiante está en riesgo de sufrir adicción y, por lo tanto, de empeorar su salud mental y perjudicar sus rendimiento académico,
será una herramienta muy útil en el cuidado de una población que, de por sí, ya es vulnerable.

## Alcance del Proyecto

### Incluye:


Los datos que se usarán provienen de la plataforma Kaggle, el dataset *Students' social media Adiction*. Es un conjunto de datos bien documentado,
cuya fuente fue una encuesta de auto-percepción publicada en redes sociales. Esto aseguró que la muestra fuera diversa en niveles de 
escolaridad, económicos y ubicación geográfica. Se recolectaron datos de estudiantes entre los 16 y los 25 años.

Las variables recolectadas, sus tipos y descripciones se encuentran en la siguiente tabla. 

|Variable 			| Type		|Description				|
|--------- 			|-----------	|------------				|
|Student_ID			|Integer  	|Unique respondent identifier		|
|Age 	   			|Integer   	|Age in years				|
|Gender    			|Categorical	|“Male” or “Female”			|
|Academic_Level 		|Categorical	|High School / Undergraduate / Graduate	|
|Country   			|Categorical 	|Country of residence			|
|Avg_Daily_Usage_Hours		|Float 		|Average hours per day on social media	|
|Most_Used_Platform 		|Categorical 	|Instagram, Facebook, TikTok, etc.	|
|Affects_Academic_Performance 	|Boolean 	|Self‐reported impact on academics (Yes/No)|
|Sleep_Hours_Per_Night 		|Float 		|Average nightly sleep hours		|
|Mental_Health_Score 		|Integer 	|Self‐rated mental health (1 = poor to 10 = excellent)|
|Relationship_Status 		|Categorical 	|Single / In Relationship / Complicated	|
|Conflicts_Over_Social_Media 	|Integer 	|Number of relationship conflicts due to social media|
|Addicted_Score 		|Integer 	|Social Media Addiction Score (1 = low to 10 = high)|

La variable objetivo será *Addicted_Score*. Es decir, este se puede ver como un problema multiclase con 10 clases.


El resultado esperado es un modelo que prediga con precisión la variable objetivo. En ese sentido, se utilizarán las métricas de *accuracy*,
*precision* y *f1 score* para evaluar el modelo. Estos serán los criterios de éxito. Se espera poder implementar un modelo clásico de ML
como un bosque de decisión y un modelo basado en redes neuronales.

### Excluye:

En el proyecto no se incluye la etapa de visualización de datos ni análisis de correlaciones, ya que el objetivo es producir y evaluar el modelo.
No se explorarán soluciones basadas en otras arquitecturas además de una red neuronal simple y un modelo de ML clásico. Es decir, no se
explorarán modelos pre entrenados, transformers, ni redes neuronales convolucionales ni recurrentes.

## Metodología

Se utilizará una metodología CRISP-DM. Es decir, se seguirán recurrentemente las etapas de entendimiento del negocio, entendimiento de los
datos, preparación de los datos, modelado, evaluación y despliegue. Este directorio corresponde a la primera etapa, entendimiento del negocio,
y será revisitada y actualizada en futuras fases del proyecto.


## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 26 de junio al 3 de julio|
| Análisis exploratorio, preprocesamiento y transformación | 1 semana | del 3 de julio al 10 de julio |
| Construcción y experimentación con modelos y evaluación | 1 semana | del 7 de julio al 17 de julio |
| Despliegue y entrega final | 2 semanas | del 10 de julio al 25 de julio |


## Equipo del Proyecto

- Uber Florez Quiroga: Líder del proyecto
- Johan Sneider Albarracín: Director de desarrollo
- Miguel Angel Acuña: Director de operaciones

## Presupuesto

Se planea un presupuesto de 100.000 pesos colombianos, destinados a la posible compra de Colab Pro.

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones



Uber Florez Quiroga, Director de Proyecto
3 de julio de 2025

## Referencias
[^fn1]: Avances en Psicología Latinoamericana. (2016). Avances En Psicología Latinoamericana. https://doi.org/10.12804/apl
[^fn2]: Kumar, A. R. (2023). Smartphone Addiction: A Growing Concern Among the Student Community. Educational Administration: Theory and Practice, 29(1). https://doi.org/10.53555/kuey.v29i1.9910
