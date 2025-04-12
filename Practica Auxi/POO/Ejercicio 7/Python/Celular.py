#7. Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
#a) Crea un método para instalar una nueva aplicación
#b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más
#de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan
#más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza
#un 1% cada 10 minutos de uso)
#c) Muestra el porcentaje de batería restante
#d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el
#mensaje de celular apagado

class Celular:
    def __init__(self):
        self.aplicaciones = {}
        self.bateria = 100  
        self.espacio = 1024  

    def instAplicacion (self, nombre, peso):
        if len(self.aplicaciones) < 20 and self.espacio >= peso:
                self.aplicaciones[nombre] = peso
                self.espacio -= peso
                print(f"Aplicación {nombre} instalada.")
        else:
                print("No se puede instalar la aplicación. Espacio insuficiente.")

    def usarAplicacion(self, nombre, tiempo):
        if nombre in self.aplicaciones:
            peso = self.aplicaciones[nombre]
            if peso > 250:
                gasto = (tiempo / 10) * 5  
            elif peso > 100:
                gasto = (tiempo / 10) * 2  
            else:
                gasto = (tiempo / 10) * 1  

            if self.bateria >= gasto:
                self.bateria -= gasto
                print(f"Usando {nombre} por {tiempo} minutos. Batería restante: {self.bateria}%")
            else:
                print("Batería insuficiente. Celular apagandose.")
        else:
            print("Aplicación no instalada.")
            

celular = Celular()
celular.instAplicacion("WhatsApp", 150)
celular.usarAplicacion("WhatsApp", 30)
print("")
celular.instAplicacion("FreeFire", 450)
celular.usarAplicacion("FreeFire", 120)
print("")
celular.instAplicacion("Roblox", 1000)
celular.usarAplicacion("Roblox", 120)
print("")
   