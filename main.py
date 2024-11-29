from flask import Flask, redirect, render_template, request, url_for 
from modelo.dao import db , Provedor , Productos,Empresas , DetallePedido, Factura,Ventas, Vendedor 
import sqlite3
from datetime import datetime
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/ventas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/Vendedores')
def Vendedores():
    return render_template('Vendedores.html')

@app.route('/Proveedores')
def Proveedores():
    return render_template('Proveedor.html')

@app.route('/Compras')
def Compras():
    return render_template()

@app.route('/DetalleCompra')
def DetalleCompra():
    return render_template('')

@app.route('/venta')
def ventas():
    return render_template('')

@app.route('/DetalleVenta')
def DetalleVenta():
    return render_template('')


@app.route('/carrito')
def carrito():
    return render_template('')


#--------------------Vendedores
@app.route('/Vendedores')
def mostrarVendedores():
    geren=Vendedor()
    gerens=geren.consultaGeneral()
    return render_template('Vendedors.html', gerens=gerens) 

@app.route('/actualizarGeren/<int:idGeren>', methods=['post','get'])
def actGeren(idGeren):
    gerenMod=Vendedor()
    if request.method=='POST':
        gerenMod.idGeren=idGeren
        gerenMod.nombre=request.form['nombreG']
        gerenMod.telefono=request.form['telefonoG']
        gerenMod.correo=request.form['correoG']
        gerenMod.direccion=request.form['direccionG']
        gerenMod.area=request.form['areaG']
        gerenMod.actualizar()
        return redirect(url_for('mostrarVendedors'))
    gerenMod=gerenMod.consultaIndividual(idGeren)
    return render_template('actVendedors.html', geren=gerenMod)

@app.route('/eliminarGeren/<int:idGeren>', methods=['post','get'])
def elimGeren(idGeren):
    gerenE=Vendedor()
    gerenE=gerenE.consultaIndividual(idGeren)
    if request.method=='POST':
        gerenE.eliminar()
        return redirect(url_for('mostrarVendedors'))
    return render_template('elimVendedors.html', geren=gerenE)

@app.route ('/regGeren')
def registrarGeren():
    return render_template('VendedorsNuevo.html')

@app.route ('/guardarGeren', methods=['post'])
def guardarGeren():
    gerenNvo=Vendedor()
    gerenNvo.nombre=request.form['nombreG']
    gerenNvo.telefono=request.form['telefonoG']
    gerenNvo.correo=request.form['correoG']
    gerenNvo.direccion=request.form['direccionG']
    gerenNvo.area=request.form['areaG']
    gerenNvo.agregar()
    return redirect(url_for('mostrarVendedors'))


if __name__ == '__main__':
    app.run(debug=True)








