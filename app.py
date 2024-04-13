import pandas as pd

datos = {
    "propietario": ["Juan Pérez", "María López", "Carlos Gómez", "Ana Rodríguez", "Luis Martínez", "Laura Pérez", "Pablo Ruiz", "Marta Gutiérrez", "Manuel González", "Sofía Díaz", "Laura Martínez", "Carlos Vargas"],
    "metros": [200, None, 5000, None, 300, None, 400, None, 600, None, 250, None],
    "propiedad_ocupada": ["S", "S", "N", None, None, None, None, "N", None, None, "S", "S"],
    "num_cuartos": [3, 2, 4, 1, 5, 3, 4, 2, 16, 3, 4, 2],
    "tipo_prop": ["Casa", "Apartamento", "Casa", None, "Casa", "Apartamento", None, "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento"],
    "ubicacion": ["Alajuela", "San José", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "San José", "Cartago", "Limón", "Alajuela", "Heredia", "Alajuela"],
    "año_construccion": [1995, 2010, 1980, 2015, 2005, 2018, 2000, 19900, 2008, 2012, 2007, 2019],
    "valor_prop": [250000, 180000, 400000, 120000, 320000, 20000000, 350000, 150000, 450000, 220000, 280000, 130000],
    "num_baños": [2, 1, 3, 1, None, 1.5, 2.5, 1.5, 3.5, 2, None, 1],
    "estado_prop": ["Buen estado", "Buen estado", "Necesita reparaciones", None, "Buen estado", "Buen estado", "Buen estado", "Necesita reparaciones", "Buen estado", "Buen estado", "Buen estado", "Nuevo"],
    "tipo_construccion": ["Tradicional", None, "Tradicional", "Moderna", "Tradicional", "Moderna", "Tradicional", "Tradicional", "Moderna", "Moderna", "Tradicional", "Moderna"],
    "servicios_disp": ["Garaje", "Gimnasio", "Jardín", "Estacionamiento", "Garaje", None, "Terraza", "Estacionamiento", "Piscina", "Estacionamiento", "Terraza", "Balcón"],
    "comodidades": ["Terraza", "Balcón", "Chimenea", None, "Terraza", None, "Chimenea", "Balcón", "Terraza", "Balcón", "Patio", "Vista a la ciudad"],
    "num_garajes": [2, 1, 3, 1, 2, None, 2, 1, 3, 1, None, 1]
}

df = pd.DataFrame(datos)

df_numericos = df[['metros', 'num_cuartos', 'año_construccion', 'valor_prop','num_baños', 'num_garajes']]

Q1 = df_numericos.quantile(0.25)
Q3 = df_numericos.quantile(0.75)
IQR = Q3 - Q1

umbral = 1.5 
for columna in df_numericos.columns:
    valor_bajo = Q1[columna] - umbral * IQR[columna]
    valor_alto = Q3[columna] + umbral * IQR[columna]
    atipico_columna = ((df_numericos[columna] < valor_bajo) | (df_numericos[columna] > valor_alto)) & df_numericos[columna].notnull()
    
    if df_numericos[atipico_columna][columna].any():
        print(f"Valores atípicos en la columna {columna}:")
        print(df_numericos[atipico_columna][columna])