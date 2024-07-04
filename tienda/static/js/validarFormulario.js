
const nombre = document.getElementById('name');
const number = document.getElementById('number');
const email = document.getElementById('email');
const coment = document.getElementById('coment');
const errorNombre = document.getElementById('errorNombre'); 
const errorNumero = document.getElementById('errorNumero'); 
const errorEmail = document.getElementById('errorEmail'); 
const errorcoment = document.getElementById('errorcoment'); 

nombre.addEventListener('input', validarFormularioNombre);
number.addEventListener('input', validarFormularioNumero);
email.addEventListener('input', validarFormularioEmail);
coment.addEventListener('input', validarFormularioComentario);


function validarFormularioNombre() {
    let mensajesError = [];
    
    if (nombre.value === null || nombre.value === '') {
        mensajesError.push(' ¡Ingrese su nombre!. ');

    } else if (/\d/.test(nombre.value)) {
        nombre.value = nombre.value.replace(/\d/g, '');
        mensajesError.push(' Ingresar solo letras, por favor. ');

    } else if (nombre.value.length < 3) {
        mensajesError.push(' Debe contener al menos 3 letras. ');
    } else if (nombre.value.length >40) {
        mensajesError.push(' Cantidad excedida. ');
    }
    if (mensajesError.length > 0) {
        errorNombre.textContent = mensajesError.join(' ');
    } else {
        errorNombre.textContent = '';
    }
}



function validarFormularioNumero() {
    let mensajesError = [];

    

        if(number.value === null || number.value === ''){
         mensajesError.push(' ¡Ingrese su numero!.');
         errorNumero.textContent = ' ¡Ingrese su numero!.';  
        }else if (/[A-Z a-z]/.test(number.value))  {
        number.value = number.value.replace(/\D/g, '');
         mensajesError.push(' Ingresar solo numeros, por favor.');
         errorNumero.textContent = ' Ingresar solo numeros, por favor.';
        } else if (!/^\d{5,}$/.test(number.value)) {
            
            mensajesError.push(' Debe ingresar al menos 5 numeros.');
            errorNumero.textContent = ' Debe ingresar al menos 5 numeros.';
        }
        if (mensajesError.length > 0) {
            errorNumero.textContent = mensajesError.join(' ');
        } else {
            errorNumero.textContent = '';
        }
  
}   


function validarFormularioEmail() {
    let mensajesError = [];

        if (email.value === null || email.value === '') {
         mensajesError.push(' ¡Ingrese su email!.');
         errorEmail.textContent = '¡Ingrese su email!.';
        } else if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value)) {
         mensajesError.push(' El email no tiene un formato valido');
         errorEmail.textContent = ' El email no tiene un formato valido.';
        


        } else {
         errorEmail.textContent = ''; 
        }
  
} 
  
function validarFormularioComentario()  {
    let mensajesError = [];
    
    if (coment.value === null || coment.value === '') {
        mensajesError.push(' ¡Ingrese un comentario!. ');

    } else if (/\d/.test(coment.value)) {
        coment.value = coment.value.replace(/\d/g, '');
        mensajesError.push(' Ingresar solo letras, por favor. ');

    } else if (coment.value.length < 3) {
        mensajesError.push(' Debe contener al menos 3 letras. ');
    } else if (coment.value.length >70) {
        mensajesError.push(' Cantidad excedida. ');
    }
    if (mensajesError.length > 0) {
        errorcoment.textContent = mensajesError.join(' ');
    } else {
        errorcoment.textContent = '';
    }

}
function validarFormulario() {
 
    validarFormularioNombre();
    validarFormularioNumero();
    validarFormularioEmail();
    validarFormularioComentario();
    
    
    
    
   
}
