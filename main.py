import pandas as pd
import numpy as rp
import matplotlib.pyplot as plt

basepath = "./"

file = basepath + "Example.xlsx"

df = pd.read_excel("./Example.xlsx",sheet_name="Hoja1")

print(df.head())

suma = df['Valores'].sum()
print(f'El valor medio es: {suma}')

# Calcula la media de los valores
media = df['Valores'].mean()
print(f'Media de los valores: {media}')

# Encuentra el valor máximo
maximo = df['Valores'].std()
print(f'Desviacion Estandar: {maximo}')

# Encuentra el valor mínimo
cantidad = df['Valores'].shape[0]
print(cantidad)
valorMedio = media/rp.sqrt(cantidad)
print(f'Desviacion Estandar Medio: {valorMedio}')

# algo = dfind[["Valores"]]

# print(algo)

