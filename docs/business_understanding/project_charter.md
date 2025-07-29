# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Análisis de la adicción a las redes sociales en estudiantes.

## Objetivo del Proyecto

El objetivo del proyecto es desarrollar un modelo de aprendizaje de máquina (Machine Learning) que sea capaz de predecir si un
estudiante es adicto a su teléfono inteligente o no, dadas variables como horas de sueño, auto percepción del rendimiento académico y
horas de uso diarias promedio.

El uso compulsivo de los teléfonos inteligentes no está lejos de ninguna de las personas en el mundo moderno. En particular, como lo 
señalan Freitas et al.[^fn1], el número de estudios del uso de teléfonos inteligentes en adolescentes creció en aproximadamente 32% 
por año entre 2009 y 2019, lo que demuestra el creciente interés en esta población. Sin embargo, Kumar [^fn2] recuerda que no es un panorama tan sencillo, ya que el teléfono inteligente
es realmente una herramienta de productividad en los estudiantes, rendición de cuentas y presencia social. La situación, dice el mismo,
se complica al involucrar la salud mental de los usuarios.

Además, diversos estudios sugieren que el uso excesivo del teléfono puede estar asociado con trastornos del sueño, ansiedad, depresión y bajo rendimiento académico. Dado el papel central que juega el bienestar emocional y el rendimiento en el éxito estudiantil, contar con herramientas predictivas que anticipen patrones de riesgo representa una oportunidad valiosa para instituciones educativas, psicólogos y responsables de políticas públicas.

En conclusión, estudios cuantitativos del asunto son necesarios y pertinentes. Un modelo que sea capaz de predecir y alertar con anticipación
si un estudiante está en riesgo de sufrir adicción y, por lo tanto, de empeorar su salud mental y perjudicar su rendimiento académico,
será una herramienta muy útil en el cuidado de una población que, de por sí, ya es vulnerable.

## Alcance del Proyecto

### Incluye:

Los datos que se usarán provienen de la plataforma Kaggle, el dataset *Students' Social Media Addiction*. Es un conjunto de datos bien documentado,
cuya fuente fue una encuesta de auto-percepción publicada en redes sociales. Esto aseguró que la muestra fuera diversa en niveles de 
escolaridad, económicos y ubicación geográfica. Se recolectaron datos de estudiantes entre los 16 y los 25 años.

Las variables recolectadas, sus tipos y descripciones se encuentran en la siguiente tabla: 

| Variable | Tipo | Descripción |
|---------|-----------|------------|
| Student_ID | Integer | Identificador único del encuestado |
| Age | Integer | Edad en años |
| Gender | Categórica | “Male” o “Female” |
| Academic_Level | Categórica | High School / Undergraduate / Graduate |
| Country | Categórica | País de residencia |
| Avg_Daily_Usage_Hours | Float | Horas promedio por día en redes sociales |
| Most_Used_Platform | Categórica | Instagram, Facebook, TikTok, etc. |
| Affects_Academic_Performance | Booleana | Impacto percibido en lo académico (Sí/No) |
| Sleep_Hours_Per_Night | Float | Horas promedio de sueño nocturno |
| Mental_Health_Score | Integer | Salud mental autoevaluada (1 = pobre, 10 = excelente) |
| Relationship_Status | Categórica | Soltero/a, En una relación, Complicado |
| Conflicts_Over_Social_Media | Integer | Número de conflictos por redes sociales |
| Addicted_Score | Integer | Puntuación de adicción a redes sociales (1 = baja, 10 = alta) |

La variable objetivo será *Addicted_Score*. Es decir, este se puede ver como un problema multiclase con 10 clases. Representa un valor auto-reportado de adicción, en una escala del 1 (muy baja) al 10 (muy alta). Inicialmente se tratará como un problema de clasificación multiclase, pero también se evaluará la opción de agrupar los niveles en categorías (bajo, medio, alto) para facilitar la interpretación del modelo.

El resultado esperado es un modelo que prediga con precisión la variable objetivo. En ese sentido, se utilizarán las métricas de *accuracy*,
*precision* y *f1 score* para evaluar el modelo. Estos serán los criterios de éxito. El modelo se considerará exitoso si alcanza al menos un 80% de *accuracy* y un F1-score superior a 0.75 en un conjunto de validación estratificado. Se dará prioridad al *F1-score* si se decide agrupar los niveles de adicción en categorías dicotómicas.

Se espera poder implementar un modelo clásico de ML como un bosque de decisión (*Random Forest*) y un modelo basado en redes neuronales.

### Excluye:

En el proyecto no se incluye la etapa de visualización de datos ni análisis de correlaciones, ya que el objetivo es producir y evaluar el modelo.
No se explorarán soluciones basadas en otras arquitecturas además de una red neuronal simple y un modelo de ML clásico. Es decir, no se
explorarán modelos preentrenados, transformers, ni redes neuronales convolucionales ni recurrentes.

## Metodología

Se utilizará una metodología CRISP-DM. Es decir, se seguirán recurrentemente las etapas de entendimiento del negocio, entendimiento de los
datos, preparación de los datos, modelado, evaluación y despliegue. Este directorio corresponde a la primera etapa, entendimiento del negocio,
y será revisitado y actualizado en futuras fases del proyecto.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|--------------------|--------|
| Entendimiento del negocio y carga de datos | 1 semana | del 26 de junio al 3 de julio |
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

| Nombre | Rol | Interés |
|--------|-----|---------|
| Dirección de Bienestar Estudiantil | Usuario final del modelo | Identificar estudiantes en riesgo |
| Psicólogo/a institucional | Asesor de interpretación | Validar la pertinencia de los factores utilizados |
| Comité académico | Evaluador de impacto | Entender el efecto en el rendimiento académico |

## Riesgos y Supuestos

**Supuestos:**

- Las respuestas de la encuesta reflejan fielmente los hábitos de los estudiantes.
- La muestra es lo suficientemente representativa para generalizar los resultados.

**Riesgos:**

- Posible sesgo en la muestra debido a la autoparticipación vía redes sociales.
- Subjetividad en la medición de adicción (auto-percepción).
- Inestabilidad del modelo al extrapolar a otras poblaciones.

## Aprobaciones

| Nombre | Cargo | Firma | Fecha |
|--------|-------|-------|-------|
| Uber Florez Quiroga | Director de Proyecto | ___________ | 3 de julio de 2025 |

## Referencias

[^fn1]: Avances en Psicología Latinoamericana. (2016). Avances En Psicología Latinoamericana. https://doi.org/10.12804/apl  
[^fn2]: Kumar, A. R. (2023). Smartphone Addiction: A Growing Concern Among the Student Community. Educational Administration: Theory and Practice, 29(1). https://doi.org/10.53555/kuey.v29i1.9910
