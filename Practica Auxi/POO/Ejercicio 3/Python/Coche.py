#3. Crea una clase Coche con marca, modelo y velocidad
#a) Agrega un método acelerar () que aumente la velocidad en 10
#b) Agrega un método frenar () que disminuya la velocidad en 5
#c) Crea dos coches, aceléralos, frénalos y muestra sus velocidades
class Coche:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        print(self)  
        print(f"El coche aceleró de {self.velocidad} km/h")
        self.velocidad += 10
        print(f"Velocidad actual: {self.velocidad} km/h")

    def  frenar(self):
        self.velocidad -= 5
        print(self)
        print(f"El coche freno de {self.velocidad} km/h")
        self.velocidad -= 5
        if self.velocidad < 0:  
            self.velocidad = 0
        print(f"Velocidad actual: {self.velocidad} km/h")

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad: {self.velocidad} km/h"

Coche1 = Coche("Nissan", "Coupe", 87)
Coche1.acelerar()

Coche2 = Coche("Toyota", "Deportivo", 120) 
Coche2.frenar()

