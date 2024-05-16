
import java.util.Scanner;





public class HolaMundo {
    public static void main(String[] args) {
      /*  System.out.println("Hola mundo desde java");
        
        int miVariable = 10 ;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
        
       //Var - inferencia de tipos en Java (Se puede sólo usar dentro del método main)
       var miVariableEntera2 = 10;
       var miVariableCadena2 = "seguimis estudiando ";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
       //Reglas para definir una variable en Java (se puede susa para comenzar variable $ y _)
        var miVariableEjemplo = 45;*/
       /* var usuario = "osvaldo";
        var titulo = "Ingeniero";
        var union = titulo +" "+ usuario ;
        System.out.println("union =" + union); 
      
      
      var a = 8;
      var b = 4;
      System.out.println(usuario +  (a + b));
      //Ejercicio: Caracteres Especiales con Java
      var nombre = "Natalia";
      System.out.println("\nNueva Linea: \n"+nombre); //salto de linea
      System.out.println("Tabulador: \t" + nombre); //Tabulador un espacio para centrar
      System.out.println("\t\t.:MENÚ:.");
      System.out.println("Retroseso:\b \b"+nombre); // Caracter de retroseso (borra un lugar hacia atras)
     // System.out.println("Comillas simples: \´"+nombre+"\´"); (comillas simple me tira errror)//
      System.out.println("Comillas Dobles:\""+nombre+"\""); */
        
     //Clase Scanner //creamos objeto dela clase scanner 
       /* Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el título");
        var titulo2 = entrada.nextLine ();
        System.out.println("Resultado: " +titulo2+" "+usuario2); */
       
       /* byte numEnteroByte = 10; 
        System.out.println("numeroEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:"+ Byte.MIN_VALUE); //Usamos la clase Byte
        System.out.println("Valor maximo del Byte"+ Byte.MAX_VALUE);
        
        short numEnteroShort = 10;
        System.out.println("numeroEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short: " + Short.MIN_VALUE); //Usamos la Clase short
        System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);
     
        int numEnteroInt = 10 ;
        System.out.println("numeroEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del int: " + Integer.MIN_VALUE); 
        System.out.println("Valor maximo del int: " + Integer.MAX_VALUE);
     
        
        long numEnteroLong = 10 ;
        System.out.println("numeroEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del long: " + Integer.MIN_VALUE); 
        System.out.println("Valor maximo del long: " + Integer.MAX_VALUE);
     */
       /* float numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de float:"+ Float.MIN_VALUE);
        System.out.println("El valor maximo del float:"+ Float.MAX_VALUE);
        
        double numDouble = 10;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de double:" + Double.MIN_VALUE);
        System.out.println(" El valor maxio de double:" + Double.MAX_VALUE); */
       
       
       //Inferencia de tipos var y tipos primitivos
       /*var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var  numFloat = 10.0F; // Automaticamente con el punto decimal se transforma en tipo double
        System.out.println("numEntero = " + numFloat);
        var numDouble = 10.0 ;
        System.out.println("numDouble = " + numDouble);*/
       
       //Tipos Primitivos char
       /* char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);

        char varCaracter = '\u0024'; // Código Unicode correcto
        System.out.println("varCaracter = " + varCaracter);*/
       
       //Conversion de tipos primitivos 
//       var edad = Integer.parseInt("20"); //convierte cadena a enteros
//        System.out.println("edad = " +(edad + 1));
//        
//        var valorPI = Double. parseDouble("3.1416"); //convierte cadena a Double
//        System.out.println("valorPI = " + valorPI);
        
       
       //pedir un valor//Clase Scanner
        var entrada = new Scanner(System.in); 
        /*System.out.println("Digite su edad");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad: = " + edad);*/
        
       //Coversión de tipos primitivos en Java parte 2  
    var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);

        var fraseChar = "programadores".charAt(4); // String no es primitivo, es un objeto
        System.out.println("fraseChar = " + fraseChar);

        System.out.println("Digite un caracter");
        
        // Inicializar el Scanner
       
        fraseChar = entrada.nextLine().charAt(0); 
        System.out.println("fraseChar = " + fraseChar);
    
    
    
    
    
    
    }       
    
}
