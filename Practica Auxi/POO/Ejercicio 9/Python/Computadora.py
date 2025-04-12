#9. Realiza la abstracción de una Computadora
#a) Muestra los componentes principales de la computadora
#b) Muestra el estado de la computadora (encendido o apagado)
#c) Crea una instancia y simula encender y apagar la computadora.


class Computadora:
    def __init__(self, marca, modelo, procesador, ram, disco_duro):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = ram
        self.disco_duro = disco_duro
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Procesador: {self.procesador}, RAM: {self.ram}, Disco Duro: {self.disco_duro}"

    def encenderApagar(self, estado):
        if estado == "encender":
            print("La computadora está encendida.")
        elif estado == "apagar":
            print("La computadora está apagada.")
        else:
            print("Estado no válido.")

Computadora1 = Computadora("HP", "Pavilion", "Intel i5", "6GB", "512GB")
print(Computadora1)
Computadora1.encenderApagar("encender")
print("")
Computadora2 = Computadora("Dell", "Inspiron", "Intel core i7", "18GB", "1TB")
print(Computadora2)
Computadora2.encenderApagar("apagar")