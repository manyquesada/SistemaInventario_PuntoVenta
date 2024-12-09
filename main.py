from flask import Flask, redirect, render_template, request, url_for 
from modelo.dao import db , Provedor ,  Vendedor 
import sqlite3
from datetime import datetime
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/ventas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

@app.route('/')
def inicio():
    return render_template('Vendedores.html')

@app.route('/Vendedores')
def Vendedores():
    return render_template('Vendedores.html')

@app.route('/Proveedores')
def Proveedores():
    return render_template('Proveedores.html')

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


@app.route('/cobro')
def cobro():
    return render_template('Cobro.html')


#--------------------Vendedores

@app.route('/Vendedores')
def mostrarVendedores():
    vende=Vendedor()
    vendens=vende.consultaGeneral()
    return render_template('Vendedores.html', vendens=vendens) 
     #------------actualizacion de los vendedores 

@app.route('/actualizarVendedors/<int:idvende>', methods=['post','get'])
def actVende(idVende):
    vendeMod=Vendedor()
    if request.method=='POST':
        vendeMod.IdVendedor=idVende
        vendeMod.Nombre=request.form['nombreV']
        vendeMod.Telefono=request.form['telefonoV']
        vendeMod.Fecha_Ingreso=request.form['fechaV']
        vendeMod.Rol=request.form['rolV']
        vendeMod.Contrasena=request.form['contrasenaV']
        vendeMod.actualizar()
        return redirect(url_for('mostrarVendedores'))
    vendeMod=vendeMod.consultaIndividual(idVende)
    return render_template('ModVendedor.html', vende=vendeMod)
      ## modulo de eliminar vendedor 
@app.route('/eliminarVendedors/<int:idvende>', methods=['post','get'])
def elimVende(idvende):
    vendeE=Vendedor()
    vendeE=vendeE.consultaIndividual(idvende)
    if request.method=='POST':
        vendeE.eliminar()
        return redirect(url_for('mostrarVendedores'))
    return render_template('ElimVendedor.html', vende=vendeE)

### registro de vendedor 

@app.route ('/regVende')
def registrarVende():
    return render_template('RegVendedores.html')

@app.route ('/guardarVende', methods=['post'])
def guardarVende():
    vendeNvo=Vendedor()
    vendeNvo.Nombre=request.form['nombreV']
    vendeNvo.Telefono=request.form['telefonoV']
    vendeNvo.Fecha_Ingreso=request.form['fechaV']
    vendeNvo.Rol=request.form['rolV']
    vendeNvo.Contrasena=request.form['contrasenaV']
    vendeNvo.agregar()
    return redirect(url_for('mostrarVendedores'))


#### APARTADO DE PROVEEDORES 

#--------------------provedores
@app.route('/provedores')
def mostrarProvedores():
    prov=Provedor()
    provs=prov.consultaGeneral()
    return render_template('Proveedores.html', provs=provs) 
### modificacion de proveedores 
@app.route('/actualizarProv/<int:idProv>', methods=['post','get'])
def actProv(idProv):
    provMod=Provedor()
    if request.method=='POST':
        provMod.Id_Proovedor=idProv
        provMod.NombreProveedor=request.form['nombreP']
        provMod.ContactoProveedor=request.form['contactoP']
        provMod.Marca=request.form['marcaP']
        provMod.TipoProducto=request.form['tipoP']
        provMod.actualizar()
        return redirect(url_for('mostrarProvedores'))
    provMod=provMod.consultaIndividual(idProv)
    return render_template('ModProv.html', prov=provMod)


### eliminacion de proveedores 
@app.route('/eliminarProv/<int:idProv>', methods=['post','get'])
def elimProv(idProv):
    provE=Provedor()
    provE=provE.consultaIndividual(idProv)
    if request.method=='POST':
        provE.eliminar()
        return redirect(url_for('mostrarProvedores'))
    return render_template('ElimProv.html', prov=provE)

## Registro de Vendedor 

@app.route ('/regProv')
def registrarProv():
    return render_template('RegProv.html')

@app.route ('/guardarProv', methods=['post'])
def guardarProv():
    provNvo=Provedor()
    provNvo.NombreProveedor=request.form['nombreP']
    provNvo.ContactoProveedor=request.form['contactoP']
    provNvo.Marca=request.form['marcaP']
    provNvo.TipoProducto=request.form['tipoP']
    provNvo.agregar()
    return redirect(url_for('mostrarProvedores'))


if __name__ == '__main__':
    app.run(debug=True)








