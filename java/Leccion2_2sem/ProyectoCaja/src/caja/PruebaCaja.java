
package caja;


public class PruebaCaja {

    
    public static void main(String[] args) { //Método main
        //Variables locales
        int medidaAncho = 3; //Valores ingresados en código duro
        int medidaAlto = 2;
        int medidaProf = 6; 
        
        Caja caja1 = new Caja(); //Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; //Le pasamos los valores al objetos
        caja1.alto = medidaAlto; //Le pasamos los valores al objeto
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen();//Llamamos al método
        
        //Primer resultado
        System.out.println("resultado volumen de caja 1: " + resultado);
        
        Caja caja2 =new Caja(2, 4, 6); //Llamamos al constructor 2 con nuevos argumentos
        //Llamamos con el nuevo objeto al método para un nuevo calculo
        System.out.println("resultado volumen de caja 2:" + caja2.calcularVolumen());
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    }

   
}
