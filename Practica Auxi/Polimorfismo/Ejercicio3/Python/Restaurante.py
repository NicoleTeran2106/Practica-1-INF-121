#3. Un restaurante organiza a su personal mediante las siguientes clases:
#a) Instanciar 1 Cocinero, 2 objetos Mesero y 2 objetos Administrativo.
#b) Sobrecargar el método SueldoTotal para mostrar el sueldo total,
#sumándole las horas extra, considerando el sueldo por hora y la propina
#en caso de los meseros.
#c) Sobrecargar el método para mostrar a aquellos Empleados que tengan
#SueldoMes igual a X.
class Cocinero:
    def __init__(self, nombre, sueldoMes, hrsExtra, sueldoHora):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.hrsExtra = hrsExtra
        self.sueldoHora = sueldoHora
    def mostrar(self):
        print("Nombre: ", self.nombre," Sueldo mensual: ", self.sueldoMes, " las horas extras trabajadas son: ", self.hrsExtra, " su sueldo por hora es de: ", self.sueldoHora)
class Mesero:
    def __init__(self, nombre, sueldoMes, hrsExtra, sueldoHora, propina):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.hrsExtra = hrsExtra
        self.sueldoHora = sueldoHora
        self.propina = propina
    def sueldoTotal(self):
        return self.sueldoMes + (self.hrsExtra * self.sueldoHora) + self.propina
    def mostrar(self):
        print("Nombre: ", self.nombre," Sueldo mensual: ", self.sueldoMes, " las horas extras trabajadas son: ", self.hrsExtra, " su sueldo por hora es de: ", self.sueldoHora, " recibe una propina de: ", self.propina)
        print("Su suelto total es de: ", self.sueldoTotal())
class Administrativo:
    def __init__(self, nombre, sueldoMes, cargo):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.cargo = cargo
    def mostrar(self):
        print("Nombre: ", self.nombre," Sueldo mensual: ", self.sueldoMes, " Cargo: ", self.cargo)
Cocinero1 = Cocinero("Pepe", 3100, 5, 18.5)
Mesero1 = Mesero("Maria", 2200, 5, 15.7, 5)
Mesero2 = Mesero("Enrique", 2100, 5, 15.3, 2)
Administrativo1 = Administrativo("Pepe2", 7500, "Gerente")
Administrativo2 = Administrativo("Galindo", 9500, "Gerente General")
Cocinero1.mostrar()
Mesero1.mostrar()
Mesero2.mostrar()
Administrativo1.mostrar()
Administrativo2.mostrar()