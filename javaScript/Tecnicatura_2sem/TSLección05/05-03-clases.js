//let persona3 = new Persona("Carla", "Ponce"); esto no se debe hacer: Persona is not defined

class Persona {  //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        
    }


    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

 // Método get para obtener el apellido
  get apellido() {
  return this._apellido;
  }

  // Método set para modificar el apellido
  set apellido(nuevoApellido) {
  this._apellido = nuevoApellido;
  }

nombreCompleto(){
    return this._nombre+" "+this._apellido;
}

//Sobreescribiendo el método de la clase padre (Object)
toString(){ //Regresa un STRING
    //Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecución
    //El método que se ejecuta depende si es una referencia de tipo padre o hija
    return this.nombreCompleto();
}


}

class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
           this._departamento = departamento;

    }

    //Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+", "+this._departamento;
    }

     
}


let persona1 = new Persona("Martin", "Perez");
console.log(persona1.nombre);
persona1._nombre = "juan Carlos";
console.log(persona1._nombre);
// Modificar el apellido a través del set
persona1.apellido = "González";
//console.log(persona1);
let persona2 = new Persona("Carlos", "Lara");
console.log(persona2.nombre);
persona2._nombre = "María Laura";
console.log(persona2._nombre);
// Modificar el apellido a través del set
persona2.apellido = "Rodriguez";
//console.log(persona2);
// Mostrar el apellido utilizando el método get
console.log(persona1.apellido); 
console.log(persona2.apellido); // Mostrará "González"

let empleado1 = new Empleado("María", "Gimenez", "Sistemas");
console.log(empleado1);
//console.log(empleado1.nombre);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString Esta es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString());
console.log(persona1.toString());
