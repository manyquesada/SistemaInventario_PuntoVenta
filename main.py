from flask import Flask, redirect, render_template, request, url_for 
from modelo.dao import db , Provedor , Productos,Empresas , DetallePedido, Factura,Ventas, Gerente 
import sqlite3
from datetime import datetime
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/cocacola'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/Empresas')
def empresas():
    return render_template('Empresas.html')

@app.route('/Gerentes')
def Gerentes():
    return render_template('Gerentes.html')

@app.route('/transporte')
def transporte():
    return render_template('transporte.html')


@app.route('/carrito')
def carrito():
    return render_template('carrito.html')


@app.route('/DetallesPedido')
def DetallesPedido():
    return render_template('DetallesPedido.html')





provs=[
    ('Alan', 100, 'Latas de coca-cola', 'Calle 5 de mayo'),
    ('Roberto', 79, 'Botellas de Fanta', 'Calle 20 de noviembre')
]
#--------------------provedores
@app.route('/provedores')
def mostrarProvedores():
    prov=Provedor()
    provs=prov.consultaGeneral()
    return render_template('transporte.html', provs=provs) 

@app.route('/actualizarProv/<int:idProv>', methods=['post','get'])
def actProv(idProv):
    provMod=Provedor()
    if request.method=='POST':
        provMod.idProv=idProv
        provMod.nombre=request.form['nombreP']
        provMod.precio=request.form['precioP']
        provMod.descripcion=request.form['descripcionP']
        provMod.actualizar()
        return redirect(url_for('mostrarProvedores'))
    provMod=provMod.consultaIndividual(idProv)
    return render_template('actTransporte.html', prov=provMod)

@app.route('/eliminarProv/<int:idProv>', methods=['post','get'])
def elimProv(idProv):
    provE=Provedor()
    provE=provE.consultaIndividual(idProv)
    if request.method=='POST':
        provE.eliminar()
        return redirect(url_for('mostrarProvedores'))
    return render_template('elimTransporte.html', prov=provE)

@app.route ('/regProv')
def registrarProv():
    return render_template('transporteNuevo.html')

@app.route ('/guardarProv', methods=['post'])
def guardarProv():
    provNvo=Provedor()
    provNvo.nombre=request.form['nombreP']
    provNvo.precio=request.form['precioP']
    provNvo.descripcion=request.form['descripcionP']
    provNvo.agregar()
    return redirect(url_for('mostrarProvedores'))

#--------------------Gerentes
@app.route('/gerentes')
def mostrarGerentes():
    geren=Gerente()
    gerens=geren.consultaGeneral()
    return render_template('Gerentes.html', gerens=gerens) 

@app.route('/actualizarGeren/<int:idGeren>', methods=['post','get'])
def actGeren(idGeren):
    gerenMod=Gerente()
    if request.method=='POST':
        gerenMod.idGeren=idGeren
        gerenMod.nombre=request.form['nombreG']
        gerenMod.telefono=request.form['telefonoG']
        gerenMod.correo=request.form['correoG']
        gerenMod.direccion=request.form['direccionG']
        gerenMod.area=request.form['areaG']
        gerenMod.actualizar()
        return redirect(url_for('mostrarGerentes'))
    gerenMod=gerenMod.consultaIndividual(idGeren)
    return render_template('actGerentes.html', geren=gerenMod)

@app.route('/eliminarGeren/<int:idGeren>', methods=['post','get'])
def elimGeren(idGeren):
    gerenE=Gerente()
    gerenE=gerenE.consultaIndividual(idGeren)
    if request.method=='POST':
        gerenE.eliminar()
        return redirect(url_for('mostrarGerentes'))
    return render_template('elimGerentes.html', geren=gerenE)

@app.route ('/regGeren')
def registrarGeren():
    return render_template('GerentesNuevo.html')

@app.route ('/guardarGeren', methods=['post'])
def guardarGeren():
    gerenNvo=Gerente()
    gerenNvo.nombre=request.form['nombreG']
    gerenNvo.telefono=request.form['telefonoG']
    gerenNvo.correo=request.form['correoG']
    gerenNvo.direccion=request.form['direccionG']
    gerenNvo.area=request.form['areaG']
    gerenNvo.agregar()
    return redirect(url_for('mostrarGerentes'))

#--------------------Empresas
@app.route('/empresas')
def mostrarEmpresas():
    emp=Empresas()
    emps=emp.consultaGeneral()
    return render_template('Empresas.html', emps=emps) 

@app.route('/actualizarEmp/<int:idEmp>', methods=['post','get'])
def actEmp(idEmp):
    empMod=Empresas()
    if request.method=='POST':
        empMod.idEmp=idEmp
        empMod.nombre=request.form['nombreE']
        empMod.telefono=request.form['telefonoE']
        empMod.direccion=request.form['direccionE']
        empMod.actualizar()
        return redirect(url_for('mostrarEmpresas'))
    empMod=empMod.consultaIndividual(idEmp)
    return render_template('actEmpresas.html', emp=empMod)

@app.route('/eliminarEmp/<int:idEmp>', methods=['post','get'])
def elimEmp(idEmp):
    empE=Empresas()
    empE=empE.consultaIndividual(idEmp)
    if request.method=='POST':
        empE.eliminar()
        return redirect(url_for('mostrarEmpresas'))
    return render_template('elimEmpresas.html', emp=empE)

@app.route ('/regEmp')
def registrarEmp():
    return render_template('EmpresasNuevo.html')

@app.route ('/guardarEmp', methods=['post'])
def guardarEmp():
    empNvo=Empresas()
    empNvo.nombre=request.form['nombreE']
    empNvo.telefono=request.form['telefonoE']
    empNvo.direccion=request.form['direccionE']
    empNvo.agregar()
    return redirect(url_for('mostrarEmpresas'))

if __name__ == '__main__':
    app.run(debug=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------



