// 0BJETO

let x = 10; // variable de tipo primitivo
console.log(x.length); // undefined, porque x es un número, no una cadena
console.log("Tipos primitivos");

// Objeto
let persona = {
    nombre: "Carlos",
    apellidos: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma: "ES",
    get lang(){
        return this.idioma.toUpperCase(); //Conviete las minúsculas a mayúsculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function() {  //método o función en JavaScript
        return this.nombre + " " + this.apellidos;
    },
    get nombreEdad(){ // Este es el método get
        return "El nombre es: "+this.nombre+", Edad: "+this.edad;
    }
    
}
console.log(persona.nombre); 
console.log(persona.apellidos); 
console.log(persona.email); 
console.log(persona.edad); 
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");

let persona2 = new Object(); // Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.dirección = "Salada 14";
persona2.telefono = "334854874576475843";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona["apellidos"]);
console.log("Usamos el ciclo for in")
// For in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
console.log(propiedad);
console.log(persona[propiedad]);
}
console.log("Cambiamos y eliminamos un error");
persona.apellida = "Betancud"; // Cambiamos dinamicamente un valor del objeto
delete persona.apellida;  // Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Número 1: La más sencilla: Concatenar cada valor de cada propiedad
console.log("Número 1: La más sencilla: Concatenar cada valor de cada propiedad");
console.log(persona.nombre+", "+persona.apellidos);

//Número 2: A través del ciclo for in 
console.log("Número 2: A través del ciclo for in"); 
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}
console.log("Número 3: La función Object.values()");
//Número 3: La función Object.values()
let personaArray = Object.values(persona);
console.log(personaArray);

// número 4 : Utilizaremos el método JSON.stringify
console.log("Distintas formas de imprimir un objeto: Forma 4");
let personaString =JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a utilñizar el método get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el método get y set para idiomas");
persona.lang = "en";
console.log(persona.lang);

function persona3(nombre, apellido, email){ //contructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+ " "+this.apellido;

    }
   
}
let padre = new persona3("Leo", "Lopez", "lopezl@gmail.com");
padre.nombre = "Luis" // modificamos el nombre
padre.telefono = "454545665453434535"; //Una propiedad exclusiva del objeto padre
console.log(padre);

console.log(padre.nombreCompleto()); // Utilizamos la función

let madre = new persona3("Laura", "Contrerra", "contrerral@gmail.com");
console.log(madre);
console.log(madre.telefono); //la propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//caso objeto 1 
let miObjeto = new Object(); // Esta es una opción formal
//caso objeto 2
let miObjeto2 = {}; //Esta opción es breve y recomendada

//caso String 1 
let miCadena1 = new String("Hola"); //Sintaxis formal
//caso String 2
let miCadena2 = "Hola"; //Esta es la sintaxis simplificada y recomendada

//caso con números 1
let miNumero = new Number(1); //Es formal no recomendable
//caso con números 2
let miNumero2 = 1; //Sintaxis recomendada

//caso boolean 1
let miBoolean1 = new Boolean(false); //Formal
//caso boolean 2
let miBoolean2 = false; // Sintaxis recomendada

//caso Arreglos 1 
let miArreglo1 = new Array(); //Formal
//caso Arreglo 2
let miArreglo2 = []; //Sintaxis recomendada

//caso function 1
let miFuncion1 = new function(){}; //Todo despues de NEW es considerado OBJETO
//caso function 2 
let miFuncion2 = function(){}; // Notación simplificada y recomendada

//Uso de prototype
persona3.prototype.telefono = "261156301728";
console.log(padre);
console.log(madre.telefono);
madre.telefono = "549261156301728";
console.log(madre.telefono);

//Uso del call
let persona4 ={
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo,telefono){
     return titulo+": "+this.nombre+" "+this.apellido+" "+telefono;
    //return this.nombre+" "+this.apellido;
    }
}

let persona5 ={
    nombre: "Carlos",
    apellido: "Lara",
    
}
console.log(persona4.nombreCompleto2("Lic.", "9858439540"));
console.log(persona4.nombreCompleto2.call(persona5, "Ing", "765844793248329"));

//Método Apply
let arreglo = ["Ing.", "8596854968547"];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));

