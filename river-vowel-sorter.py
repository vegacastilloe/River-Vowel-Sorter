import pandas as pd
from tabulate import tabulate

# 🧩 Datos originales
df_raw = pd.read_excel(xl, header=1)
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, :2].dropna(how='all')
# 📝 Renombrar columnas
df_input.columns = ['Group', 'River']

def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    comparison = df_actual.eq(df_expected.reset_index(drop=True)).all(axis=1)
    return pd.concat([df_actual, df_expected, comparison.rename('Match')], axis=1)

# 🧠 Función para verificar orden de vocales creciente o decreciente
VOWELS = 'aeiou'
def extract_vowels(word):
    return [char for char in word.lower() if char in VOWELS]

def is_ordered(vowels):
    if len(set(vowels)) < 2:
        return False
    directions = []
    for i in range(len(vowels) - 1):
        if vowels[i] < vowels[i + 1]:
            directions.append('up')
        elif vowels[i] > vowels[i + 1]:
            directions.append('down')
    return len(set(directions)) == 1

# ✅ Filtrado de ríos válidos
df_input['Vowels'] = df_input['River'].apply(extract_vowels)
df_input['Valid'] = df_input['Vowels'].apply(is_ordered)
df_valid = df_input[df_input['Valid']].drop(columns=['Vowels','Valid']).sort_values(['Group', 'River'])
df_valid['RiverNum'] = df_valid.groupby('Group').cumcount() + 1

# 🔢 Enumeración y pivotado
df_pivot = df_valid.pivot(index='Group', columns='RiverNum', values='River')
df_pivot.columns = [f'River{i}' for i in df_pivot.columns]
df_pivot = df_pivot.reset_index().fillna('')

# 🧪 Comparación con columnas esperadas
test = df_raw.iloc[:, 3:].copy()
df_final = compare_with_expected(df_pivot, test)

print(tabulate(df_final.values, headers=df_final.columns, tablefmt='fancy'))

# 💾 Exportación opcional
# df_final.to_excel("river_vowel_sorter_output.xlsx", index=False)
