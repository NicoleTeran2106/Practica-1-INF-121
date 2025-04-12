/*
3. Crea una clase Coche con marca, modelo y velocidad
   a) Agrega un método acelerar() que aumente la velocidad en 10
   b) Agrega un método frenar() que disminuya la velocidad en 5
   c) Crea dos coches, aceléralos, frénalos y muestra sus velocidades
*/
public class Coche {
    private String marca;
    private String modelo;
    private int velocidad;

    public Coche(String marca, String modelo, int velocidad) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = velocidad;
    }

    public void acelerar() {
        System.out.println(this);  
        System.out.println("El coche aceleró de " + velocidad + " km/h");
        velocidad += 10;
        System.out.println("Velocidad actual: " + velocidad + " km/h");
    }

    public void frenar() {
        System.out.println(this);
        System.out.println("El coche frenó de " + velocidad + " km/h");
        velocidad -= 5;
        if (velocidad < 0) {
            velocidad = 0;
        }
        System.out.println("Velocidad actual: " + velocidad + " km/h");
    }

    @Override
    public String toString() {
        return "Marca: " + marca + ", Modelo: " + modelo + ", Velocidad: " + velocidad + " km/h";
    }
}