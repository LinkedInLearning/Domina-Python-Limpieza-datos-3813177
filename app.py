import pandas as pd

datos = {
    "propietario": ["Juan Pérez", "María López", "Carlos Gómez", "Juan Pérez", "Luis Martínez", "Laura Pérez", "Pablo Ruiz", "Marta Gutiérrez", "Manuel González", "Sofía Díaz", "Laura Martínez", "Carlos Vargas"],
    "metros": [200, None, 5000, 200, 300, None, 400, None, 600, None, 250, None],
    "propiedad_ocupada": ["S", "S", "N", "S", None, None, None, "N", None, None, "S", "S"],
    "num_cuartos": [3, 2, 4, 3, 5, 3, 4, 2, 16, 3, 4, 2],
    "tipo_prop": ["Casa", "Apartamento", "Casa", "Casa", "Casa", "Apartamento", None, "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento"],
    "ubicacion": ["Alajuela", "San José", "Cartago", "Alajuela", "Guanacaste", "Puntarenas", "San José", "Cartago", "Limón", "Alajuela", "Heredia", "Alajuela"],
    "año_construccion": [1995, 2010, 1980, 1995, 2005, 2018, 2000, 19900, 2008, 2012, 2007, 2019],
    "valor_prop": [250000, 180000, 400000, 250000, 150000, 200000, 350000, 150000, 450000, 220000, 280000, 130000],
    "num_baños": [2, 1, 3, 2, None, 1.5, 2.5, 1.5, 3.5, 2, None, 1],
    "estado_prop": ["Buen estado", "Buen estado", "Necesita reparaciones", "Buen estado", "Buen estado", "Buen estado", "Buen estado", "Necesita reparaciones", "Buen estado", "Buen estado", "Buen estado", "Nuevo"],
    "tipo_construccion": ["Tradicional", None, "Tradicional", "Tradicional", "Tradicional", "Moderna", "Tradicional", "Tradicional", "Moderna", "Moderna", "Tradicional", "Moderna"],
    "servicios_disp": ["Garaje", "Gimnasio", "Jardín", "Garaje", "Garaje", None, "Terraza", "Estacionamiento", "Piscina", "Estacionamiento", "Terraza", "Balcón"],
    "comodidades": ["Terraza", "Balcón", "Chimenea", "Terraza", "Terraza", None, "Chimenea", "Balcón", "Terraza", "Balcón", "Patio", "Vista a la ciudad"],
    "num_garajes": [2, 1, 3, 2, 2, None, 2, 1, 3, 1, None, 1]
}

df = pd.DataFrame(datos)

duplicados = df.duplicated()

print("Filas duplicadas:\n ",df[duplicados])