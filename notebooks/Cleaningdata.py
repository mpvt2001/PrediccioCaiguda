import pandas as pd
from collections import Counter

df_concatenate = pd.read_csv('df/df_concatenate.csv')

TARGET = 'Fall'
count = df_concatenate[TARGET].value_counts()
print(count)

perc1 = count[1] / len(df_concatenate) * 100
perc0 = count[0] / len(df_concatenate) * 100

print("Percentatge de 1s: ", perc1)
print("Percentatge de 0s: ", perc0)

anys = []
for fila in df_concatenate['P2 Temps Sistema']:
    any = fila[:4]
    anys.append(any)

print("Anys trobats:")
contador = Counter(anys)

# Mostrar los resultados
print("Freqüencia de cada valor unic:")
for valor, frequencia in contador.items():
    print(f"L'any {valor} apareix {frequencia} vegades.")
    
df_concatenate['P1 Temps Sistema'] = pd.to_datetime(df_concatenate['P1 Temps Sistema'])
df_concatenate['P2 Temps Sistema'] = pd.to_datetime(df_concatenate['P2 Temps Sistema'])

# Contar las caídas por año
caidas_por_año1 = df_concatenate.groupby(df_concatenate['P1 Temps Sistema'].dt.year)['Fall'].sum()
caidas_por_año2 = df_concatenate.groupby(df_concatenate['P2 Temps Sistema'].dt.year)['Fall'].sum()

# Mostrar el resultado
print(caidas_por_año1)
print(caidas_por_año2)

df_concatenate.shape

df2014 = df_concatenate[df_concatenate['P2 Temps Sistema'].dt.year == 2014]
df2015 = df_concatenate[df_concatenate['P2 Temps Sistema'].dt.year == 2015]
df2014.to_csv("df/df2014.csv")
df2015.to_csv("df/df2015.csv")
