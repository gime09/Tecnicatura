
package CicloWhile;

public class EjercicioWhile01 {

    public static void main(String[] args) {
        var conteo = 0;
        while (conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }
        var contador = 0;
        do {
            System.out.println("contador 0" + contador);
            contador++;

        } while (contador < 7);
        
        
        for(var contando = 0 ; contando < 7; contando++ ){
            System.out.println("contando =" + contando);
            
        }

    }
}
