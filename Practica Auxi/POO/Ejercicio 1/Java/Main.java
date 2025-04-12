/*
1. Crea una clase Persona con nombre, edad y ciudad
   a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
   b) Crea tres personas y muestra su saludo
   c) Agrega un método para verificar si es mayor de edad
*/
public class Main {
    public static void main(String[] args) {
        Persona p1 = new Persona("Maria", 20, "Mexico");
        System.out.println(p1.presentacion());
        if (p1.esMayordeedad()) { 
            System.out.println(p1.getN() + " es mayor de edad.");
        } else {
            System.out.println(p1.getN() + " es menor de edad.");
        }

        Persona p2 = new Persona("Pepe", 12, "Argentina"); // Cambié el nombre para mayor claridad
        System.out.println(p2.presentacion());
        if (p2.esMayordeedad()) {
            System.out.println(p2.getN() + " es mayor de edad.");
        } else {
            System.out.println(p2.getN() + " es menor de edad.");
        }

        Persona p3 = new Persona("Dayana", 18, "Peru"); // Cambié el nombre para mayor claridad
        System.out.println(p3.presentacion());
        if (p3.esMayordeedad()) {
            System.out.println(p3.getN() + " es mayor de edad.");
        } else {
            System.out.println(p3.getN() + " es menor de edad.");
        }
    }
}
