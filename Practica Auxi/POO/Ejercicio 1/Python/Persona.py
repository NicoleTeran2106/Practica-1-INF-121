#1. Crea una clase Persona con nombre, edad y ciudad
#a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
#b) Crea tres personas y muestra su saludo
#c) Agrega un método para verificar si es mayor de edad

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludo(self):
        return f"Hola, soy {self.nombre}, soy de {self.ciudad}."

    def mayoriaDeEdad(self):
        edad = self.edad
        if edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
            return True
        else:
            print(f"{self.nombre} es menor de edad.")
            return False
        
Persona1 = Persona("Maria", 20, "Mexico")
print(Persona1.saludo())
Persona1.mayoriaDeEdad()

Persona2 = Persona("Ana", 12, "Peru")
print(Persona2.saludo())
Persona2.mayoriaDeEdad()

Persona3 = Persona("Pepe", 67, "España") 
print(Persona3.saludo())
Persona3.mayoriaDeEdad()


