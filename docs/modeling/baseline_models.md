# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline desarrollado para predecir el nivel de adicción a redes sociales en estudiantes.

---

## 1. Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base del rendimiento, sobre la cual se compararán modelos posteriores.

Se seleccionó un **modelo de Bosque Aleatorio (Random Forest Classifier)**, entrenado para una tarea de **clasificación multiclase**. Se realizó una búsqueda en rejilla (Grid Search) y se encontró que un bosque con los siguientes hiperparámetros ofrecía el mejor desempeño:

- **Número de árboles**: 69  
- **Profundidad máxima**: 11  
- **Criterio de impureza**: Gini  

---

## 2. Variables de entrada

Se utilizaron todas las variables disponibles, **excepto** `Student_ID`. El preprocesamiento incluyó:

- **Codificación One Hot** para variables categóricas, incluida `Country`.
- **Conversión a ordinal** de `Academic_Level`:
  - High School → 1
  - Undergraduate → 2
  - Graduate → 3
- **Variables numéricas**: no se estandarizaron ni escalaron, ya que el modelo de bosque aleatorio no es sensible a la escala.

Lista de variables utilizadas:

`Age`, `Gender`, `Academic_Level`, `Country`, `Avg_Daily_Usage_Hours`, `Most_Used_Platform`, `Affects_Academic_Performance`, `Sleep_Hours_Per_Night`, `Mental_Health_Score`, `Relationship_Status`, `Conflicts_Over_Social_Media`.

---

## 3. Variable objetivo

La variable objetivo fue `Addicted_Score`, una variable numérica discreta con **valores enteros entre 3 y 9** (aunque originalmente permitía del 1 al 10).

Dado que los valores representan niveles ordinales de adicción, se trató como un problema de **clasificación multiclase**.

> Nota: Se podría evaluar en futuras iteraciones si un enfoque de **regresión ordinal** o **agrupación en clases** (bajo, medio, alto) mejora la interpretación y desempeño.

---

## 4. Evaluación del modelo

### Métricas de evaluación

Se utilizaron las métricas estándar para clasificación multiclase:

- **Precision**  
- **Recall**  
- **F1-Score**  

Dado el desequilibrio de clases, se reportaron los **promedios ponderados** y **macro promedio**.

### Resultados

| Clase | Precision | Recall | F1-score | Soporte |
|-------|-----------|--------|----------|---------|
| 3     | 1.00      | 0.67   | 0.80     | 3       |
| 4     | 0.90      | 1.00   | 0.95     | 18      |
| 5     | 0.92      | 1.00   | 0.96     | 23      |
| 6     | 1.00      | 0.80   | 0.89     | 10      |
| 7     | 0.97      | 1.00   | 0.98     | 31      |
| 8     | 1.00      | 0.93   | 0.96     | 14      |
| 9     | 1.00      | 1.00   | 1.00     | 6       |
| **Accuracy**       |           |        | **0.95** | 106     |
| **Macro avg**      | 0.85      | 0.80   | 0.82     | 106     |
| **Weighted avg**   | 0.95      | 0.95   | 0.95     | 106     |

---

## 5. Análisis de los resultados

El modelo obtiene un rendimiento excelente en términos generales, con una **accuracy del 95%**. Las clases con mayor cantidad de observaciones (`5` y `7`) tienen métricas sobresalientes.

Sin embargo, las clases con muy pocas muestras (`3`, `6`, `9`) presentan mayor variabilidad en las métricas. Esto se debe a que el modelo tiene menos ejemplos para aprender y generalizar correctamente.

> Esto sugiere una posible necesidad de **balanceo de clases**, o bien reagrupar las categorías menos frecuentes.

---

## 6. Conclusiones

- El modelo baseline ofrece un excelente punto de partida.
- Los resultados son sólidos y consistentes con el comportamiento esperado del algoritmo.
- El enfoque de **clasificación multiclase con Random Forest** funciona bien en este problema.
- Se recomienda explorar modelos adicionales para comparación, como:
  - **Regresión lineal con variable ordinal**
  - **Red neuronal sencilla**
  - **Regresión logística multinomial**

Además, se puede incorporar la **importancia de variables** del Random Forest para análisis de interpretabilidad en la próxima fase.

---

## 7. Referencias

- Scikit-learn documentation: [https://scikit-learn.org](https://scikit-learn.org)
- Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5–32.
- Kuhn, M., & Johnson, K. (2013). Applied Predictive Modeling.

---

