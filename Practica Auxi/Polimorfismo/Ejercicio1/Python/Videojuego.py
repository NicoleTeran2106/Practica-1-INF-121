#1. Sea la clase Videojuego:
#a) Instanciar al menos 2 videojuegos
#b) Sobrecargar el constructor 2 veces
#c) Implementar un método mostrar()
#d) Sobrecargar el método agregarJugadores() donde en el primero se agregue
#solo 1 jugador y en otro se ingrese una cantidad de jugadores a aumentar.
class Videojuego:
    def __init__(self, nombre, plataforma, cantidadJugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores
    def mostrar(self):
        print("Videojuego: ", self.nombre, "Plataforma: ", self.plataforma, "Cantidad de jugadores: ", self.cantidadJugadores)
    def agregarJugadores(self, cantidad=1):
        self.cantidadJugadores += cantidad
        print(f"Cantidad de jugadores actualizada: {self.cantidadJugadores}")
juego1 = Videojuego("Pou", "PlayStation", 2)
juego2 = Videojuego("FreeFire", "PC")
juego1.mostrar()
juego2.mostrar()
juego1.agregarJugadores()
juego2.agregarJugadores(3) 