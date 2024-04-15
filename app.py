import pandas as pd

datos = {
    "propietario": ["Juan Pérez", "María López", "Carlos Gómez", "Ana Rodríguez", "Luis Martínez", "Laura Pérez", "Pablo Ruiz", "Marta Gutiérrez", "Manuel González", "Sofía Díaz", "Laura Martínez", "Carlos Vargas"],
    "metros": [200, 100, None, 233, 300, None, 400, 160, 600, 250, 250, 140],
    "propiedad_ocupada": ["S", "S", None, "S", "S", "S", "S", "N", "S", "S", "S", "S"],
    "num_cuartos": [3, 2, None, 1, 3, 3, 4, 2, 1, 3, 4, 2],
    "tipo_prop": ["Casa", "Apartamento", None, "Apartamento", "Casa", None, "Casa", "Apartamento", "Casas", "Apartamento", "Casa", "Apartamento"],
    "ubicacion": ["Alajuela", "San José", "Cartago", "Heredia", "Guanacaste", None, "San José", "Cartago", "Limón", "Alajuela", "Heredia", "Alajuela"],
    "año_construccion": [1995, 2010, None, 2015, 2005, None, 2000, 1990, 2008, 2012, 2007, 2019],
    "valor_prop": [250000, 180000, None, 120000, 320000, None, 350000, 150000, 450000, 220000, 280000, 130000],
    "num_baños": [2, 1, 3, 1, 2, None, 2.5, 1.5, 3, 2, 2, 1],
    "estado_prop": ["Buen estado", "Buen estado", None, "Buen estado", "Buen estado", None, "Buen estado", "Necesita reparaciones", "Buen estado", "Buen estado", "Buen estado", "Nuevo"],
    "tipo_construccion": ["Tradicional", "Moderna", None, "Moderna", "Tradicional", None, "Tradicional", "Tradicional", "Moderna", "Moderna", "Tradicional", "Moderna"],
    "servicios_disp": ["Garaje", "Gimnasio", None, "Estacionamiento", "Garaje", None, "Terraza", "Estacionamiento", "Piscina", "Estacionamiento", "Terraza", "Balcón"],
    "comodidades": ["Terraza", "Balcón", None, "Balcón", "Terraza", None, "Chimenea", "Balcón", "Terraza", "Balcón", "Patio", "Vista a la ciudad"],
    "num_garajes": [2, 1, None, 1, 2, 1, 2, 1, 3, 1, 1, 1]
}

df = pd.DataFrame(datos)
