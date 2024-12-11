
// Objeto para almacenar la cantidad de cada producto
var cantidadesProductos = {};

function buscarProducto() {
var codigo = document.getElementById("codigo").value;
var indicador = document.getElementById("indicador");
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
 if (this.readyState == 4 && this.status == 200) {
     var producto = JSON.parse(this.responseText);
     if (producto.error) {
         // Producto no encontrado, mostrar indicador rojo
         indicador.classList.remove("verde");
         indicador.classList.add("rojo");
     } else {
         // Producto encontrado, mostrar indicador verde
         indicador.classList.remove("rojo");
         indicador.classList.add("verde");
     }
 }
};
xhttp.open("GET", "/buscar_producto/" + codigo, true);
xhttp.send();
}

function agregarProducto() {
var codigo = document.getElementById("codigo").value;

// Verificar si el producto ya existe en la tabla
var existe = false;
var table = document.getElementById("cuerpoTabla");
for (var i = 0; i < table.rows.length; i++) {
 if (table.rows[i].cells[0].innerHTML == codigo) {
     existe = true;
     // Incrementar la cantidad del producto en la tabla
     var cantidadActual = parseInt(table.rows[i].cells[2].innerHTML);
     table.rows[i].cells[2].innerHTML = cantidadActual + 1;
     // Actualizar el total de la fila
     var precioVenta = parseFloat(table.rows[i].cells[4].innerHTML);
     var iva = parseFloat(table.rows[i].cells[5].innerHTML);
     var totalProducto = (precioVenta + (precioVenta * (iva / 100))) * (cantidadActual + 1);
     table.rows[i].cells[6].innerHTML = totalProducto;
     break;
 }
}

if (!existe) {
 // Realizar la petición AJAX para obtener los detalles del producto
 var xhttp = new XMLHttpRequest();
 xhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
         var producto = JSON.parse(this.responseText);
         if (producto.error) {
             // Mostrar un mensaje de error si el producto no se encuentra
             alert(producto.error);
         } else {
             // Calcular el total del producto
             var totalProducto = producto.precio_venta + (producto.precio_venta * (producto.iva / 100)); 

             // Crear una nueva fila en la tabla
             var row = table.insertRow();
             var cell1 = row.insertCell();
             var cell2 = row.insertCell();
             var cell3 = row.insertCell();
             var cell4 = row.insertCell();
             var cell5 = row.insertCell();
             var cell6 = row.insertCell();
             var cell7 = row.insertCell();
             var cell8 = row.insertCell(); // Celda para el botón "Eliminar"

             cell1.innerHTML = codigo;
             cell2.innerHTML = producto.nombre;
             cell3.innerHTML = 1; // Cantidad inicial
             cell4.innerHTML = producto.precio_compra;
             cell5.innerHTML = producto.precio_venta;
             cell6.innerHTML = producto.iva;
             cell7.innerHTML = totalProducto;

             // Agregar botón "Eliminar"
             cell8.innerHTML = '<button onclick="eliminarProducto(this)">Eliminar</button>';
         }
     }
 };
 xhttp.open("GET", "/buscar_producto/" + codigo, true);
 xhttp.send();
}

// Actualizar el total de la venta
actualizarTotal();

// Limpiar el campo de código 
document.getElementById("codigo").value = "";
}

function eliminarProducto(button) {
var row = button.parentNode.parentNode; // Obtener la fila del botón
row.parentNode.removeChild(row); // Eliminar la fila de la tabla
actualizarTotal(); // Actualizar los totales
}

function actualizarTotal() {
var subtotal = 0;
var totalIVA = 0;
var table = document.getElementById("cuerpoTabla");
for (var i = 0; i < table.rows.length; i++) {
 var precioVenta = parseFloat(table.rows[i].cells[4].innerHTML);
 var iva = parseFloat(table.rows[i].cells[5].innerHTML);
 var cantidad = parseInt(table.rows[i].cells[2].innerHTML);

 subtotal += precioVenta * cantidad; // Sumar el precio de venta al subtotal
 totalIVA += (precioVenta * (iva / 100)) * cantidad; // Sumar el IVA al totalIVA
}
document.getElementById("subtotal").innerHTML = subtotal;
document.getElementById("iva").innerHTML = totalIVA;
document.getElementById("totalVenta").innerHTML = "Total: " + (subtotal + totalIVA);
}


// parte del modal

function confirmarVenta() {
    // 1. Obtener los datos de la venta (productos, totales, etc.)
    var datosVenta = obtenerDatosVenta(); 
  
    // 2. Enviar los datos al servidor con AJAX (ruta /generar_ticket)
    enviarDatosAlServidor(datosVenta);
  
    // 3. Mostrar el ticket en pantalla o redirigir a la página del ticket
    mostrarTicket(datosVenta); 
  
    // 4. Cerrar el modal
    $('#modalCobro').modal('hide');
  }
  
  function obtenerDatosVenta() {
    // Implementa la lógica para obtener los datos de la venta de la tabla
    // ...
  }
  
  function enviarDatosAlServidor(datosVenta) {
    // Implementa la lógica para enviar los datos al servidor con AJAX
    // ...
  }
  
  function mostrarTicket(datosVenta) {
    // Implementa la lógica para mostrar el ticket en pantalla
    // ...
  }