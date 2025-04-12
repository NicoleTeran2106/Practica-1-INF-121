/*
3. Crea una clase Coche con marca, modelo y velocidad
   a) Agrega un método acelerar() que aumente la velocidad en 10
   b) Agrega un método frenar() que disminuya la velocidad en 5
   c) Crea dos coches, aceléralos, frénalos y muestra sus velocidades
*/
public class Main {
    public static void main(String[] args) {
        Coche coche1 = new Coche("Nissan", "Coupe", 87);
        coche1.acelerar();

        Coche coche2 = new Coche("Toyota", "Deportivo", 120);
        coche2.frenar();
    }
}