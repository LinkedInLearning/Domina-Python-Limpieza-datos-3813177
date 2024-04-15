import pandas as pd

datos = {
    "propietario": ["Juan Pérez", "María López", "Carlos Gómez", "Ana Rodríguez", "Luis Martínez", "Laura Pérez", "Pablo Ruiz", "Marta Gutiérrez", "Manuel González", "Sofía Díaz", "Laura Martínez", "Carlos Vargas"],
    "metros": [200, 100, 500, 233, 300, 200, 400, 160, 600, 250, 250, 140],
    "propiedad_ocupada": ["S", "S", "N", "S", "S", "S", "S", "N", "S", "S", "S", "S"],
    "num_cuartos": [3, 2, 4, 1, 5, 3, 4, 2, 6, 3, 4, 2],
    "tipo_prop": ["Casa", "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento", "Casa", "Apartamento"],
    "ubicacion": ["Alajuela", "San José", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "San José", "Cartago", "Limón", "Alajuela", "Heredia", "Alajuela"],
    "año_construccion": [1995, 2010, 1980, 2015, 2005, 2018, 2000, 1990, 2008, 2012, 2007, 2019],
    "valor_prop": ["$250,000", "$180,000", "$400,000", "$120,000", "$320,000", "$200,000", "$350,000", "$150,000", "$450,000", "$220,000", "$280,000", "$130,000"],
    "num_baños": [2, 1, 3, 1, 2, 4, 2.5, 1.5, 3, 2, 2, 1],
    "estado_prop": ["Buen estado", "Buen estado", "Necesita reparaciones", "Buen estado", "Buen estado", "Buen estado", "Buen estado", "Necesita reparaciones", "Buen estado", "Buen estado", "Buen estado", "Nuevo"],
    "tipo_construccion": ["Tradicional", "Moderna", "Tradicional", "Moderna", "Tradicional", "Moderna", "Tradicional", "Tradicional", "Moderna", "Moderna", "Tradicional", "Moderna"],
    "servicios_disp": ["Garaje", "Gimnasio", "Jardín", "Estacionamiento", "Garaje", "Piscina", "Terraza", "Estacionamiento", "Piscina", "Estacionamiento", "Terraza", "Balcón"],
    "comodidades": ["Terraza", "Balcón", "Chimenea", "Balcón", "Terraza", "Vista al parque", "Chimenea", "Balcón", "Terraza", "Balcón", "Patio", "Vista a la ciudad"],
    "num_garajes": [2, 1, 3, 1, 2, 1, 2, 1, 3, 1, 1, 1]
}

df = pd.DataFrame(datos)
