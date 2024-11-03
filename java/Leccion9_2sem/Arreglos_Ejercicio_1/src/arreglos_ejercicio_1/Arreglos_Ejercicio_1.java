/*
Ejercicio 1: Leer 5 números, guardarlos en un arreglo y 
mostrarlos en el mismo orden introducidos.
*/

package arreglos_ejercicio_1;
import java.util.Scanner;
public class Arreglos_Ejercicio_1 {
    
   public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[5]; // Declaramos un arreglo para guardar 5 números

        // Leer los números y guardarlos en el arreglo
        System.out.println("Introduce 5 números:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        // Mostrar los números en el mismo orden que fueron introducidos
        System.out.println("\nNúmeros introducidos:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Número " + (i + 1) + ": " + numeros[i]);
        }
    }  
    
    
}