
let x = 10; // variable de tipo primitivo
console.log(x.length); // undefined, porque x es un número, no una cadena

// Objeto
let persona = {
    nombre: "Carlos",
    apellidos: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    nombreCompleto: function() {  //método o función en JavaScript
        return this.nombre + " " + this.apellidos;
    }
}
console.log(persona.nombre); 
console.log(persona.apellidos); 
console.log(persona.email); 
console.log(persona.edad); 
console.log(persona);
console.log(persona.nombreCompleto());
