# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos (EDA) para el proyecto de predicción de adicción a redes sociales. El objetivo del EDA es comprender las características y estructura del conjunto de datos, detectar posibles problemas de calidad y guiar las decisiones de preprocesamiento y modelado posteriores.

---

## 1. Resumen general de los datos

El conjunto de datos consta de **705 observaciones** y **13 características**. Tras una limpieza inicial, se descartó una variable no relevante. Las **12 variables restantes** se dividen en:

- **6 numéricas**
- **6 categóricas**
- La variable objetivo `Addicted_Score` es de tipo numérico discreto (enteros del 1 al 10).

No se identificaron valores faltantes, duplicados, corruptos ni inconsistencias de formato.

La mayoría de las variables numéricas presentan distribuciones normales. Sin embargo, la variable objetivo presenta un **sesgo a la izquierda**, con una mayor concentración de valores altos.

---

## 2. Resumen de calidad de los datos

- **Valores faltantes:** Ninguno.
- **Duplicados:** Ninguno.
- **Errores de formato o de tipo:** Ninguno.
- **Variables categóricas:** Todas las categorías están dentro de lo esperado; no se detectaron errores de tipeo ni categorías espurias.
- **Valores extremos:** Presentes, pero plausibles. No se eliminarán, ya que aportan información relevante para el modelado.

**Acciones tomadas:**
- Revisión completa de consistencia en variables categóricas.
- Validación cruzada de tipos de datos.
- Conservación de outliers para análisis posterior.

---

## 3. Variable objetivo: `Addicted_Score`

- Se distribuye en una escala discreta de 1 a 10.
- Se observa un **sesgo a la izquierda**: los valores altos son más frecuentes.
- El valor **máximo** observado fue 9; el valor **más frecuente** fue 8, seguido del 5.
- El valor **mínimo** fue 1; el valor 2 aparece muy pocas veces.

Esta distribución puede modelarse con una distribución **Beta** con parámetros `α=8` y `β=4`, que refleja la asimetría observada.

> **Figura 1**: Histograma de `Addicted_Score`.

---

## 4. Análisis de variables individuales

### Variables numéricas

- Presentan distribuciones normales.
- No se identificaron valores extremos que deban eliminarse.
- Se considera aplicar **escalado estándar** antes del modelado.

### Variables categóricas

- **Academic_Level**: fuerte desbalance. La mayoría son estudiantes de pregrado.
- **Relationship_Status**: categoría "Complicado" muy poco representada.
- **Most_Used_Platform**: altamente dominada por Instagram, TikTok, Facebook y WhatsApp.

**Acciones propuestas:**

- Agrupar categorías poco frecuentes en una categoría "Otro".
- Aplicar **codificación one-hot** para todas las variables categóricas.
- Considerar técnicas de balanceo (como `SMOTE`) si se binariza la variable objetivo en el futuro.

---

## 5. Ranking de variables importantes

Se evaluó la correlación lineal entre variables numéricas y la variable objetivo.

- **Alta correlación positiva**: 
  - `Conflicts_Over_Social_Media`
  - `Avg_Daily_Usage_Hours`
- **Alta correlación negativa**:
  - `Mental_Health_Score`

> **Figura 2**: Mapa de calor de correlaciones numéricas.

En cuanto a las variables categóricas, la relación con la variable objetivo no es evidente a simple vista. Se evaluará su impacto mediante:

- Codificación one-hot.
- Modelos de regresión lineal múltiple.
- Importancia de características en modelos de bosque aleatorio y redes neuronales.

---

## 6. Conclusiones y siguientes pasos

- Los datos están limpios y listos para transformación y modelado.
- Se identificaron variables clave con potencial predictivo.
- Se deben transformar adecuadamente las variables categóricas.
- Se recomienda realizar una normalización de las variables numéricas para modelos sensibles a escala.

La calidad de los datos es alta, lo que proporciona una buena base para el modelado predictivo.

---


