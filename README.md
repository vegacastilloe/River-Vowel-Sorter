# River Vowel Sorter
![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/River-Vowel-Sorter)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 --- CAN YOU SOLVE THIS - EXCEL CHALLENGE 805 ---
- 🌟 **Author**: Excel (Vijay A. Verma) BI
 
    - List the Rivers which contain at least 2 distinct vowels and vowels are either in increasing order (>=) or decreasing order (<=) but not both.
 
 🔰 Este script en Python filtra y agrupa nombres de ríos según una regla lingüística: deben contener al menos dos vocales distintas, y estas deben estar en orden creciente o decreciente (pero no ambos).
 
 🔗 Link to Excel file:
 👉 https://lnkd.in/djZt7JMu

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/River-Vowel-Sorter/blob/main/river-vowel-sorter.py

---
---

## 🌊 River Vowel Sorter

Este script en Python filtra y agrupa nombres de ríos según una regla lingüística: deben contener al menos dos vocales distintas, y estas deben estar en orden creciente o decreciente (pero no ambos). El resultado se presenta en formato tabular, agrupado por región, y se compara contra columnas esperadas.

## 📦 Requisitos

- Python 3.7+
- pandas
- tabulate
- Archivo Excel con al menos las siguientes columnas:
  - Columna 1: `Group`: nombre del grupo o región
  - Columna 2: `River`: nombre del río
  - Opcionalmente, puede incluir columnas esperadas a partir de la columna 4 para validación.

---

## 🚀 Cómo funciona

1. **Carga de datos** desde Excel con validación de estructura.
2. **Extracción de vocales** de cada nombre de río.
3. **Validación de orden**: se aceptan solo ríos con vocales en orden creciente o decreciente.
4. **Agrupamiento** por región y enumeración de ríos.
5. **Pivotado** para mostrar cada grupo en una fila y sus ríos en columnas `River1`, `River2`, etc.
6. **Comparación** con columnas esperadas (si existen).
7. **Visualización** en formato de tabla con `tabulate`.

---

## 📤 Salida

El script imprime un DataFrame con:

- `Group` y `River1`, `River2`, `River3` ordenados por secuencia
- Columnas esperadas desde el Excel
- Columna `Match` con valores `True` o `False`

---
## ✨ Output:

| Group | River1 | River2 | River3 | Group | River1 | River2 | River3 | Match |
|-------|--------|--------|--------|-------|--------|--------|--------|-------|
| Alpha | Amazon | Nile | Yangtze | Alpha | Amazon | Nile | Yangtze | True |
| Delta | Lena | Niger |          | Delta | Lena | Niger |          | True |
| Gamma | Amur |       |          | Gamma | Amur |       |          | True |

---

## 🛠️ Personalización

Puedes adaptar el script para:

- Cambiar el criterio de orden de vocales
- Validar contra diferentes estructuras
- Exportar el resultado a Excel o CSV

## 🚀 Ejecución
```bash
pip install pandas openpyxl
```
```python
river-vowel-sorter.py
```

## 📄 Licencia

Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.
