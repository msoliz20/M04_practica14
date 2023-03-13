import json

from INTEGRANTE_A.Car import Car
from INTEGRANTE_A.Animal import Animal


Cars = [
    Car("Renault", "1000KG", "Rojo", "Renault"),
    Car("Nissan", "900KG", "Blanco", "Nissan"),
    Car("Mercedes-benz", "1200KG", "Blanco", "Mercedes-benz"),
    Car("Audi", "1500KG", "Negro", "Audi"),
    Car("Volvo", "1100KG", "Amarillo", "Volvo")
]

Animals = [
    Animal("Leon", "150KG", "90cm", "Felino"),
    Animal("Elefante", "100KG", "300cm", "Mamifero"),
    Animal("Tigre", "100KG", "80cm", "Felino"),
    Animal("Canguro", "150KG", "150cm", "Marsupial"),
    Animal("Oso", "500KG", "180cm", "Mamifero")
]

cars_list = [u.to_dict() for u in Cars]
animal_list = [u.to_dict() for u in Animals]

data = {"cars":cars_list,"animals":animal_list}

with open("jsonAPI2/A.json",'w') as file:
    json.dump(data, file)