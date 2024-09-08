miFuncion(8,2); // Esto se lo conoce como Hosting

function miFuncion(a,b){
//console.log("Sumamos:"+ (a + b));
return a + b;
}
//Llamando a la función
miFuncion(5,4);

let resultado = miFuncion(6,7);
console.log(resultado);

//Declaramos una función de tipo expresión o anónima
let x = function(a, b){return a + b}; //necesita cierre con punto y coma
resultado = x(5,6); //al llamarla se pone la variable y parentesis
console.log(resultado);

//Funciones de tipo self y invoking
(function(a, b){
    console.log("Ejecutando la función: "+ (a + b)); 

})(9,6)

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
}
miFuncionDos(5, 7);

//toString (convierte la función a texto)
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones flecha
const  sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); //Asignamos el valor a una variable
console.log(resultado);

//Función  tipo expresión 
let sumar = function(a = 4, b = 8){
    console.log(arguments[0]);// Muestra el parametro de : a 
    console.log(arguments[1]); // Muestra el parametro de : b
    console.log(arguments[2]);
    return a + b;
    
}
resultadoesultado = sumar(3, 2);
console.log(resultado);


let sumarr = function(a = 4, b = 8){
    console.log(arguments[0]);// Muestra el parametro de : a 
    console.log(arguments[1]); // Muestra el parametro de : b
    console.log(arguments[2]);
    return a + b + arguments[2];
    
}
resultado = sumarr(3, 2, 9);
console.log(resultado);

// Sumar todos lo argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0; 
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; //arguments es para arreglos
    }
    return suma; 
}

// Tipos primitivos (Por Valor / El valor de la variable NO cambia)
let k = 10;
function cambiarValor(a){
    a = 20;
}
cambiarValor(k);
console.log(k); 

// (Por Referencia / El valor de la variable apunta al mismo espacio de memoria por eso cambia )
const persona = {
nombre: "Juan",
apellido:"Lepez"
}
console.log(persona);
function cambiarValorObjeto(p1){

    p1.nombre = "Ignacio";
    p1.nombre = "Perez";
}
cambiarValorObjeto(persona); 
console.log(persona);