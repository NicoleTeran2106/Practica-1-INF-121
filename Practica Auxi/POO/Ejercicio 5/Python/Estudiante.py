#5. Crea una clase Estudiante con nombre, nota_1, nota_2
#a) Agrega un método para calcular el promedio
#b) Agrega un método para verificar si aprobó (promedio >=6)
#c) Crea tres estudiantes, muestra sus promedios y si aprobaron

class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def CalcularPromedio(self):
        return (self.nota_1 + self.nota_2) / 2
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Promedio: {self.CalcularPromedio()}"
    
    def Aprobo(self):
        if self.CalcularPromedio() >= 6:
            print ("El estudiante aprobó")
            return True
        else:
            print ("El estudiante no aprobó")
            return False
        
    def Notas(self):   
        if self.nota_1 + self.nota_2 < 0 or self.nota_1 + self.nota_2 > 20:  
            print("Las notas deben ser de 0 a 10")
            return False
        return True
        
Estudiante1 = Estudiante("Pepe", 10, 7)
if Estudiante1.Notas():  
    print(Estudiante1)
    Estudiante1.Aprobo()
print()  
Estudiante2 = Estudiante("Maria", 5, 5)
if Estudiante2.Notas(): 
    print(Estudiante2)
    Estudiante2.Aprobo()
print()  

Estudiante3 = Estudiante("Pedro", 6, 79)
if Estudiante3.Notas():  
    print(Estudiante3)
    Estudiante3.Aprobo()
print()  