# Reporte Integral del Modelo de Predicción de Adicción a Redes Sociales

## 1. Resumen Ejecutivo

Este documento presenta el desarrollo y evaluación de un modelo de aprendizaje automático orientado a predecir el **nivel de adicción a redes sociales** en estudiantes, utilizando datos autoreportados. Se compararon múltiples modelos, incluyendo un modelo *baseline* (bosque aleatorio) y una red neuronal multicapa, usando técnicas de ajuste de hiperparámetros como búsqueda en rejilla y Optuna.  

El modelo final seleccionado fue un **bosque aleatorio con 69 árboles**, profundidad máxima de 11, optimizado con el criterio  Gini. Este modelo obtuvo resultados sobresalientes, con métricas de _precision_, _recall_ y _f1-score_ superiores al 95% en el conjunto de evaluación. Aunque el modelo neuronal mostró un rendimiento competitivo (~92%), no logró superar al modelo basado en árboles.

## 2. Descripción del Problema

El problema abordado se enmarca en el creciente uso de redes sociales por parte de estudiantes de secundaria y universidad. El objetivo del proyecto es predecir el puntaje de adicción a redes sociales según la **Escala de Bergen**, utilizando variables como:

- Tiempo de uso diario
- Horas de sueño
- Nivel educativo
- Conflictos en redes sociales
- Salud mental (autoevaluada)
- Otros datos demográficos

Esta predicción permite anticipar niveles de riesgo y diseñar estrategias de intervención académica o psicológica.

## 3. Preparación y Procesamiento de Datos

### 3.1 Variables de Entrada

Se utilizaron todas las variables disponibles, excepto `Student_id`. Las transformaciones realizadas incluyen:

- **Categóricas**: Codificadas con _One-Hot Encoding_ (`Gender`, `Country`, `Most_Used_Platform`, `Affects_Academic_Performance`, `Relationship_Status`, `Conflicts_Over_Social_Media`).
- **Ordinales**: `Academic_Level` se transformó asignando valores (1=High School, 2=Undergraduate, 3=Graduate).
- **Numéricas**: `Age`, `Avg_Daily_Usage_Hours`, `Sleep_Hours_Per_Night`, `Mental_Health_Score` se dejaron sin escalado adicional.

### 3.2 Variable Objetivo

La variable objetivo es **`Addicted_Score`**, una variable ordinal con valores del 3 al 9 (aunque teóricamente va de 0 a 9). Se trata como un problema de clasificación multiclase con 7 categorías.

## 4. Modelos Desarrollados

### 4.1 Modelo Baseline

Se construyó un modelo base con un **Random Forest** utilizando búsqueda en rejilla GridCV. Los hiperparámetros óptimos fueron:

- `n_estimators = 69`
- `max_depth = 11`
- `criterion = gini`

Este modelo fue entrenado sobre el conjunto de entrenamiento y evaluado con validación cruzada, registrando sus resultados en MLflow.

### 4.2 Ajuste Fino del Modelo

Se realizó un ajuste fino con una rejilla más específica en el rango `n_estimators = [60, 80]` y se utilizó **Optuna** para evaluar combinaciones adicionales. No se obtuvieron mejoras sustanciales, por lo que se mantuvo la configuración original.

### 4.3 Modelo Neuronal

Se implementó una red neuronal con:

- 1 capa oculta de 128 neuronas (ReLU)
- 1 capa de salida con 7 neuronas (Softmax)
- Entrenamiento con 100 épocas
- Optimización con Adam y pérdida categórica

Este modelo alcanzó métricas cercanas al 92% y se documentó en MLflow, pero no superó al bosque aleatorio.

## 5. Evaluación del Modelo Final

### 5.1 Métricas

| Clase | Precision | Recall | F1-Score | Soporte |
|-------|-----------|--------|----------|---------|
| 3     | 1.00      | 0.67   | 0.80     | 3       |
| 4     | 0.90      | 1.00   | 0.95     | 18      |
| 5     | 0.92      | 1.00   | 0.96     | 23      |
| 6     | 1.00      | 0.80   | 0.89     | 10      |
| 7     | 0.97      | 1.00   | 0.98     | 31      |
| 8     | 1.00      | 0.93   | 0.96     | 14      |
| 9     | 1.00      | 1.00   | 1.00     | 6       |
| **Prom. ponderado** | 0.95 | 0.95 | 0.95 | 106     |

### 5.2 Análisis

- El modelo tiene excelente rendimiento general.
- El bajo soporte en categorías como la 3 afecta el rendimiento puntual.
- El modelo generaliza bien y comete errores “graduales” (es decir, una predicción errónea suele estar cercana al valor real).

## 6. Registro y Trazabilidad

Se utilizó **MLflow** para:

- Registrar ejecuciones (`run`)
- Almacenar métricas y parámetros
- Versionar los modelos
- Visualizar resultados desde la UI local (`mlruns/`)

El entorno fue gestionado en Colab, utilizando `mlflow.set_experiment()` y `mlflow.start_run()` para mantener consistencia entre ejecuciones.

## 7. Conclusiones y Recomendaciones

- El **bosque aleatorio** es el mejor modelo hasta el momento.
- El **95% de acierto** en clasificación multiclase lo hace ideal para entornos reales.
- La red neuronal podría mejorar con más datos o arquitectura más profunda, pero no justificó su complejidad.
- En futuras versiones se puede considerar:
  - Mayor equilibrio de clases (recolección dirigida)
  - Regresores ordinales o modelos de clasificación jerárquica

## 8. Aplicaciones Potenciales

- Soporte en decisiones educativas y políticas públicas.
- Diseño de campañas de concienciación estudiantil.
- Herramientas diagnósticas automatizadas en entornos escolares o universitarios.

## 9. Referencias

- Escala de Adicción a Redes Sociales de Bergen (BSNAS)
- Scikit-Learn documentation
- Keras documentation
- MLflow tracking
- Literatura sobre clasificación ordinal y bosques aleatorios
