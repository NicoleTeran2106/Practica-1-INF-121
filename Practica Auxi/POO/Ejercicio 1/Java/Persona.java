/*
1. Crea una clase Persona con nombre, edad y ciudad
   a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
   b) Crea tres personas y muestra su saludo
   c) Agrega un método para verificar si es mayor de edad
*/
public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public void setN(String nombre){
        this.nombre = nombre;
    }

    public void setE(int edad){
        this.edad = edad;
    }

    public void setC(String ciudad){
        this.ciudad= ciudad;
    }

    public String getN(){
        return this.nombre;
    }
    public int getE(){
        return this.edad;
    }

    public String getC(){
        return this.ciudad;
    }

    public boolean igual(Persona o){
        return this.nombre.equals(o.nombre) && this.edad == o.edad && this.ciudad.equals(o.ciudad);
    }
@Override
    public String toString(){
        return "Nombre: " + this.nombre + ", Edad: " + this.edad + ", Ciudad: " + this.ciudad;
    }

    public boolean  esMayordeedad(){
            return this.edad >= 18;
  
}
    public String presentacion(){
        return "Hola, soy " + this.nombre  + " de " + this.ciudad;
    }
}