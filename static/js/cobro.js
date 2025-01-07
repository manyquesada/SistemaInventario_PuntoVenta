function agregarProducto() {
    var codigoBarras = document.getElementById("codigoBarras").value;

    // Realizar solicitud AJAX a Flask
    fetch('/agregar_producto_cobro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'codigoBarras=' + codigoBarras
    })
    .then(response => response.json())
    .then(data => {
        // Buscar si el producto ya existe en la tabla
        var tabla = document.getElementById("tabla-productos").getElementsByTagName('tbody')[0];
        var filas = tabla.getElementsByTagName('tr');
        var encontrado = false;

        for (var i = 0; i < filas.length; i++) {
            var celdas = filas[i].getElementsByTagName('td');
            if (celdas[0].innerText === data.codigoBarras) {
                // Actualizar cantidad y subtotal
                var cantidad = parseInt(celdas[2].innerText) + 1;
                celdas[2].innerText = cantidad;
                celdas[4].innerText = (cantidad * parseFloat(data.precio)).toFixed(2);
                encontrado = true;
                break;
            }
        }

        if (!encontrado) {
            // Agregar nueva fila si el producto no existe
            var fila = tabla.insertRow();
            var celdaCodigo = fila.insertCell();
            var celdaNombre = fila.insertCell();
            var celdaCantidad = fila.insertCell();
            var celdaPrecio = fila.insertCell();
            var celdaSubtotal = fila.insertCell();

            celdaCodigo.innerHTML = data.codigoBarras;
            celdaNombre.innerHTML = data.nombre;
            celdaCantidad.innerHTML = 1;
            celdaPrecio.innerHTML = data.precio;
            celdaSubtotal.innerHTML = data.precio;
        }

        // Actualizar totales
        actualizarTotales();
    })
    .catch(error => console.error('Error:', error));
}

function actualizarTotales() {
    var tabla = document.getElementById("tabla-productos").getElementsByTagName('tbody')[0];
    var filas = tabla.getElementsByTagName('tr');
    var subtotal = 0;

    for (var i = 0; i < filas.length; i++) {
        var celdas = filas[i].getElementsByTagName('td');
        var precio = parseFloat(celdas[3].innerText);
        var cantidad = parseInt(celdas[2].innerText);
        subtotal += precio * cantidad;
    }

    var iva = subtotal * 0.16; // Suponiendo un IVA del 16%
    var total = subtotal + iva;

    document.getElementById("subtotal").innerText = subtotal.toFixed(2);
    document.getElementById("iva").innerText = iva.toFixed(2);
    document.getElementById("total").innerText = total.toFixed(2);
}

// Funciones para el modal
var modal = document.getElementById("modalCobro");
var btnAbrirModal = document.getElementById("abrirModal");
var btnCerrarModal = document.getElementsByClassName("close")[0];

btnAbrirModal.onclick = function() {
    modal.style.display = "block";
}

btnCerrarModal.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function calcularCambio() {
    var total = parseFloat(document.getElementById("total").innerText);
    var cantidadRecibida = parseFloat(document.getElementById("cantidadRecibida").value);
    var mensajeCambio = document.getElementById("mensajeCambio");

    if (cantidadRecibida >= total) {
        var cambio = cantidadRecibida - total;
        mensajeCambio.innerHTML = "<p>Cambio: $" + cambio.toFixed(2) + "</p>";

        // Guardar datos de la compra en el formulario
        guardarDatosCompra();

        // Enviar formulario automáticamente
        document.getElementById("formularioCompra").submit();
    } else {
        var falta = total - cantidadRecibida;
        mensajeCambio.innerHTML = "<p>Falta: $" + falta.toFixed(2) + "</p>";
    }
}

function guardarDatosCompra() {
    var tabla = document.getElementById("tabla-productos").getElementsByTagName('tbody')[0];
    var filas = tabla.getElementsByTagName('tr');
    var datosCompra = [];

    for (var i = 0; i < filas.length; i++) {
        var celdas = filas[i].getElementsByTagName('td');
        datosCompra.push({
            codigoBarras: celdas[0].innerText,
            nombre: celdas[1].innerText,
            cantidad: parseInt(celdas[2].innerText),
            precio: parseFloat(celdas[3].innerText)
        });
    }

    document.getElementById("datosCompra").value = JSON.stringify(datosCompra);
}