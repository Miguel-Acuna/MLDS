# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

Se desarrolló un modelo de clasificación de Machine Learning multiclase, capaz de predecir el puntaje de adicción a redes sociales en la escala de Bergen. Se logró un _accuracy_ de 95% y el modelo final seleccionado fue el modelo base, un bosque aleatorio de 69 árboles y profundidad 11. Se concluye que para este tipo de datos tabulares, abudantes y completos, el desempeño de un modelo clásico de ML supera al de una red neuronal, que logró un 92%. También, queda como lección experimentar primero con modelos de la estadística clásica como la regresión multilineal o la regresión logística y luego con modelos de ML o redes neuronales, ya que los primeros pueden hacer uso extensivo de correlaciones ya presentes en los datos, mientras que en los segundos no se hace tan claro el uso de esa relación. 

## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.
- Evaluación del modelo final y comparación con el modelo base.
- Descripción de los resultados y su relevancia para el negocio.

- Se entregaron códigos para la carga, exploración, transformación, modelamiento y despliegue de los datos. Se logró corroborar que los datos entregados al modelos estuvieran limpios y fueran funcionales y consistentes, y que el modelo predijera correctamente la clase el 95% de las veces.
- En nuestro caso, el modelo final fue el modelo base, ya que el modelo alternativo se desempeñó ligeramente peor. Así, la evaluación del modelo final es bastante positiva, con un 95% de precisión. La desventaja es el procesamiento de los datos, que no es obvio y requiere bastantes pasos para entregar un formato consistente con el modelo. Para siguientes iteraciones, se trabajará en la implementación con datos más sencillos o incompletos.
- En cuanto a los resultados, se encuentra que la mayoría de estudiantes se autoreportan con un puntaje de adicción mayor a 6 en una escala de 10, y cercca de un 10% se reportan en el nivel máximo de adicción. El modelo así lo confirma. Esto indica que tanto escuelas como gobiernos como compañías de redes sociales deben usar modelos tales como el nuestro para tomar decisiones drásticas respecto del acceso y consumo de los estudiantes a redes sociales.
Adicionalmente, nuestro modelo muestra que un puntaje mayor de adicción se correlaciona altamente con un deterioro en la salud mental y física, medida en horas de sueño de los estudiantes, y con mayores conflictos en redes sociales. Por lo tanto, refuerza la idea de que una exposición prolongada a redes sociales es nociva para los estudiantes y, por lo tanto, para la sociedad en general. 

## Lecciones aprendidas

La transformacion de columnas categoricas tiene que revisarse muy bien ya que existe varias formas de lograrlo 
El despliegue es una etapa muy importante en el desarrollo del ciclo de desarrollo de software , mas en esta area de Machine Learning
El usuario final no esta acostumbrado a manejar estas herramientas, por lo tanto, un buen front puede alivianar el proceso de cambio tecnologico en el que estan todas las empresas actualmente 

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.

- En contextos médicos, el modelo podrá ser usado para ayudar en el diagnóstico de las causas de enfermedades mentales, desempeño académico disminuido o mayores dificultades en relaciones interpersonales, ya que todas estas son variables altamente correlacionadas con una adicción a redes sociales. Si el profesional de la salud logra cuantificar o categorizar dichas circunstancias, podrá obtener de nuestro modelo una visión más clara de la adicción a redes sociales.
Por otro lado, nuestro modelo impacta en el área de legislación educativa. Al procesar grandes cantidades de datos y mostrar que el modelo también tiene un sesgo a la izquierda, se aporta evidencia cuantitativa para demostrar que las adicción a redes sociales es una epidemia creciente en la población estudiantil con consecuencias para la salud. Por lo tanto, es necesario tomar acciones que corrijan dichas tendecias.

- En las áreas de mejora, se buscará desarrollar un modelo al que se le pueda proporcionar información incompleta (es decir, no todas las variables sino solo unas cuantas)  y aún así sea capaz de predecir el puntaje de adicción. También en relación con eso, se buscará que el despliegue del modelo sea más intuitivo para el usuario final, de modo que no tenga que preprocesar todos los datos él mismo. Finalmente, se buscará explotar más las altas correlaciones intrínsecas a los datos de entrada explorando otros tipos de modelos, más afines a la estadística clásica.

## Conclusiones

Al contar con pocos datos, se debe explorar la valides de este score a nivel mundial, ya que la mayoria de los participantes provienen de partes especificas. Ademas, la adicion de nuevas variables puede hacer mas robusto la deteccion de 
esta addicion. Un algorirtmo de arboles de decision mostro mejores resultados que una red neuronal, lo cual se adecua mas para el tipo de problema que estamos solucionando aqui.
La forma de despliegue es algo nuevo para todos los integrantes el equipo, lo cual nos ha costado consolidar una solucion usable para las empresas del hoy, esta es la version del API

## Agradecimientos

Miguel Angel Acuna Silva maacunas@unal.edu.co
Johan Sneider Albarracin Gomez joalbarracing@unal.edu.co
Uber Florez Quiroga uflorezq@unal.edu.co
