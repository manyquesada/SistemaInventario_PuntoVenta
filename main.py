from flask import Flask, redirect, render_template, request, url_for 
from modelo.dao import db , Provedor ,  Vendedor ,Inventario
import sqlite3
from flask import jsonify
from datetime import datetime
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/ventas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

@app.route('/')
def inicio():
    return render_template('login.html')


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





#-------------------------------------------------------------------Vendedores


@app.route('/vendedores')
def mostrarVendedores():
    vende=Vendedor()
    vendens=vende.consultaGeneral()
    return render_template('Vendedores.html', vendens=vendens)

@app.route('/actualizarVendedors/<int:idVende>', methods=['post','get'])
def actVende(idVende):
    vendeMod=Vendedor()
    if request.method=='POST':
        vendeMod.Id_Vendedor=idVende
        vendeMod.NombreVendedor=request.form['nombreV']
        vendeMod.TelefonoVendedor=request.form['telefonoV']
        vendeMod.Fecha_Ingreso=request.form['fechaV']
        vendeMod.Rol=request.form['rolV']
        vendeMod.Contrasena=request.form['contrasenaV']
        vendeMod.actualizar()
        return redirect(url_for('mostrarVendedores'))
    vendeMod=vendeMod.consultaIndividual(idVende)
    return render_template('ModVendedor.html', vende=vendeMod)

      ## modulo de eliminar vendedor 
@app.route('/eliminarVendedors/<int:idVende>', methods=['post','get'])
def elimVende(idVende):
    vendeE=Vendedor()
    vendeE=vendeE.consultaIndividual(idVende)
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
    vendeNvo.NombreVendedor=request.form['nombreV']
    vendeNvo.TelefonoVendedor=request.form['telefonoV']
    vendeNvo.Fecha_Ingreso=request.form['fechaV']
    vendeNvo.Rol=request.form['rolV']
    vendeNvo.Contrasena=request.form['contrasenaV']
    vendeNvo.agregar()
    return redirect(url_for('mostrarVendedores'))


#### APARTADO DE PROVEEDORES 

#--------------------provedores
@app.route('/Provedores')
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
        provMod.TelefonoProveedor=request.form['contactoP']
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





## Registro de proovedor 

@app.route ('/regProv')
def registrarProv():
    return render_template('RegProv.html')

@app.route ('/guardarProv', methods=['post'])
def guardarProv():
    provNvo=Provedor()
    provNvo.NombreProveedor=request.form['nombreP']
    provNvo.TelefonoProveedor=request.form['contactoP']
    provNvo.Marca=request.form['marcaP']
    provNvo.TipoProducto=request.form['tipoP']
    provNvo.agregar()
    return redirect(url_for('mostrarProvedores'))



#### PARTE DE INVENTARIO 



#-------------------PRODUCTOS 
@app.route('/Productos')
def mostrarProductos():
    prod=Inventario()
    prods=prod.consultaGeneral()
    return render_template('Productos.html', prods=prods) 
### modificacion de productos
@app.route('/actualizarProd/<int:idProd>', methods=['post','get'])
def actProd(idProd):
    prodMod=Inventario()
    if request.method=='POST':
        
        prodMod.CodigoBarras = idProd
        prodMod.NombreProducto=request.form['nombreI']
        prodMod.CantidadProducto=request.form['cantidadI']
        prodMod.Precio_Compra=request.form['preciocompraI']
        prodMod.Precio_Venta=request.form['precioVentaI']
        prodMod.Iva=request.form['ivaI']
        prodMod.Categoria=request.form['categoriaI']
        prodMod.actualizar()
        return redirect(url_for('mostrarProductos'))
    prodMod=prodMod.consultaIndividual(idProd)
    return render_template('ModProd.html', prodMod=prodMod)


### eliminacion de productos
@app.route('/eliminarProd/<int:idProd>', methods=['post','get'])
def elimProd(idProd):
    prodE=Inventario()
    prodE=prodE.consultaIndividual(idProd)
    if request.method=='POST':
        prodE.eliminar()
        return redirect(url_for('mostrarProvedores'))
    return render_template('ElimProd.html', prod=prodE)

## Registro de producto

@app.route ('/regProd')
def registrarProd():
    return render_template('RegProd.html')

@app.route ('/guardarProd', methods=['post'])
def guardarProd():
    prodNvo=Inventario()
    prodNvo.CodigoBarras = request.form['codigoBarrasI']
    prodNvo.NombreProducto=request.form['nombreI']
    prodNvo.CantidadProducto=request.form['cantidadI']
    prodNvo.Precio_Compra=request.form['preciocompraI']
    prodNvo.Precio_Venta=request.form['precioVentaI']
    prodNvo.Iva=request.form['ivaI']
    prodNvo.Categoria=request.form['categoriaI']
    prodNvo.agregar()
    return redirect(url_for('mostrarProductos'))




    
if __name__ == '__main__':
    app.run(debug=True)








