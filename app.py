import pandas as pd
from sklearn.impute import KNNImputer

datos = {
    "propietario": ["Juan Pérez", "María López", "Carlos Gómez", "Ana Rodríguez", "Luis Martínez", "Laura Pérez", "Pablo Ruiz", "Marta Gutiérrez", "Manuel González", "Sofía Díaz", "Laura Martínez", "Carlos Vargas"],
    "metros": [200, 100, None, 233, 300, 200, 400, 160, None, 250, 250, 140],
    "propiedad_ocupada": ["S", "S", "N", "S", "S", "S", "S", "N", "S", "S", "S", "S"],
    "num_cuartos": [3, 2, 4, None, 3, 3, None, 2, 1, None, 4, 2],
    "tipo_prop": ["Casa", "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento"],
    "ubicacion": ["Alajuela", "San José", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "San José", "Cartago", "Limón", "Alajuela", "Heredia", "Alajuela"],
    "año_construccion": [1995, 2010, 1980, 2015, None, 2018, 2000, 1990, 2008, 2012, 2007, 2019],
    "valor_prop": [250000, None, 400000, 120000, 320000, 200000, 350000, 150000, 450000, 220000, 280000, 130000],
    "num_baños": [2, 1, None, 1, 2, None, 2.5, 1.5, None, 2, 2, None],
    "estado_prop": ["Buen estado", "Buen estado", "Necesita reparaciones", "Buen estado", "Buen estado", "Buen estado", "Buen estado", "Necesita reparaciones", "Buen estado", "Buen estado", "Buen estado", "Nuevo"],
    "tipo_construccion": ["Tradicional", "Moderna", "Tradicional", "Moderna", "Tradicional", "Moderna", "Tradicional", "Tradicional", "Moderna", "Moderna", "Tradicional", "Moderna"],
    "servicios_disp": ["Garaje", "Gimnasio", "Jardín", "Estacionamiento", "Garaje", "Piscina", "Terraza", "Estacionamiento", "Piscina", "Estacionamiento", "Terraza", "Balcón"],
    "comodidades": ["Terraza", "Balcón", "Chimenea", "Balcón", "Terraza", "Vista al parque", "Chimenea", "Balcón", "Terraza", "Balcón", "Patio", "Vista a la ciudad"],
    "num_garajes": [2, None, 3, 1, 2, None, 2, 1, 3, None, 1, 1]
}

df = pd.DataFrame(datos)

print("Valores faltantes por columna: \n", df.isnull().sum()) 