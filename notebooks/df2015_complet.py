import pandas as pd
from datetime import datetime

df = pd.read_csv("df2015.csv")
df.columns
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.2'], axis=1)
df.shape
df_noduplicats = df.drop_duplicates()
df_noduplicats.shape

df_noduplicats['P1 Temps Sistema'] = pd.to_datetime(df_noduplicats['P1 Temps Sistema'])
df_noduplicats['P2 Temps Sistema'] = pd.to_datetime(df_noduplicats['P2 Temps Sistema'])

# Verificar si la parte de año, mes y día es igual en ambas columnas
df_noduplicats['MateixaData'] = (df_noduplicats['P1 Temps Sistema'].dt.date == df_noduplicats['P2 Temps Sistema'].dt.date)
count_date = df_noduplicats['MateixaData'].value_counts()
print(df_noduplicats.shape)
print(count_date)
df_noduplicats = df_noduplicats.loc[df_noduplicats['MateixaData'] == True]
print(df_noduplicats.shape)
df_noduplicats = df_noduplicats.drop(['MateixaData'], axis=1)

df_noduplicats['Any'] = df_noduplicats['P1 Temps Sistema'].dt.year
df_noduplicats['Mes'] = df_noduplicats['P1 Temps Sistema'].dt.month
df_noduplicats['Dia'] = df_noduplicats['P1 Temps Sistema'].dt.day
df_noduplicats['P1 Temps Sistema'] = df_noduplicats['P1 Temps Sistema'].dt.strftime('%H:%M:%S')
df_noduplicats['P2 Temps Sistema'] = df_noduplicats['P2 Temps Sistema'].dt.strftime('%H:%M:%S')
df_noduplicats.info()

fall_files = df_noduplicats[df_noduplicats['Fall'] == 1]
conteo_filas = fall_files.groupby(['Usuari', 'Any', 'Mes', 'Dia','P1 Temps Sistema','P2 Temps Sistema','Fall']).size().reset_index(name='conteo')

# Mostrar el conteo de filas por mes de cada año
print(conteo_filas)

df = df_noduplicats.copy()

suma_potencies = df['P1 accelerometre 1X']**2 + df['P1 accelerometre 1Y']**2 + df['P1 accelerometre 1Z']**2
suma_potencies2 = df['P1 accelerometre 2X']**2 + df['P1 accelerometre 2Y']**2 + df['P1 accelerometre 2Z']**2
suma_potencies3 = df['P2 accelerometre 1X']**2 + df['P2 accelerometre 1Y']**2 + df['P2 accelerometre 1Z']**2
suma_potencies4 = df['P2 accelerometre 2X']**2 + df['P2 accelerometre 2Y']**2 + df['P2 accelerometre 2Z']**2
df['P1 Mod1'] = np.sqrt(suma_potencies)
df['P1 Mod2'] = np.sqrt(suma_potencies2)
df['P2 Mod1'] = np.sqrt(suma_potencies3)
df['P2 Mod2'] = np.sqrt(suma_potencies4)

df.to_csv("df2015_net_amp.csv", index=False)


df['data_obj'] = df['Any'].astype(str)+"-"+df['Mes'].astype(str)+"-"+df['Dia'].astype(str)+" "+df['P1 Temps Sistema']
def convertir_a_datetime(cadena):
    return datetime.strptime(cadena, "%Y-%m-%d %H:%M:%S")
df['data'] = df['data_obj'].apply(convertir_a_datetime)
def convertir_a_unix(dt):
    return int(dt.timestamp())
df['P1 TempsUnix'] = df['data'].apply(convertir_a_unix)

df['data_obj2'] = df['Any'].astype(str)+"-"+df['Mes'].astype(str)+"-"+df['Dia'].astype(str)+" "+df['P2 Temps Sistema']
df['data2'] = df['data_obj2'].apply(convertir_a_datetime)
df['P2 TempsUnix'] = df['data2'].apply(convertir_a_unix)

columnes_esborrar = ['P1 timestamp', 'P2 timestamp', 'P1 accelerometre 1X', 'P1 accelerometre 1Y', 
                     'P1 accelerometre 1Z', 'P1 accelerometre 2X', 'P1 accelerometre 2Y', 
                     'P1 accelerometre 2Z', 'P2 accelerometre 1X', 'P2 accelerometre 1Y', 
                     'P2 accelerometre 1Z', 'P2 accelerometre 2X', 'P2 accelerometre 2Y', 
                     'P2 accelerometre 2Z', 'P1 Temps Sistema', 'P2 Temps Sistema', 'P1 Calibració', 'P2 Calibració',
                     'Any', 'Mes', 'Dia', 'data_obj', 'data_obj2', 'data', 'data2']
df = df.drop(columnes_esborrar, axis=1)

df.to_csv("df2015_model.csv", index=False) #(20594298, 42)
