from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, Integer, String , Date, Double,Time
db = SQLAlchemy() 


# Parte Vendedores ---------------------------------------------    #

class Vendedor(db.Model):
    __tablename__='vendedor'
    IdVendedor=Column(Integer, primary_key=True)
    Nombre=Column(String)
    Telefono=Column(Float)
    Fecha_Ingreso=Column(Date)
    Rol=Column(String)
    Contrasena=Column(String)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return Vendedor.query.get(id)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()
    


##### -----------------------------------------------------Parte de Proveedores -----------------------------------------

class Provedor(db.Model):
    __tablename__='proveedor'
    Id_Proovedor=Column(Integer, primary_key=True)
    NombreProveedor=Column(String)
    ContactoProveedor=Column(Double)
    Marca=Column(String)
    TipoProducto=Column(String)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return Provedor.query.get(id)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

  

###------------------------------------------------------- Parte de Inventario 

class Inventario (db.Model):
    __tablename__='inventario'
    CodigoBarras=Column(Integer, primary_key=True)
    NombreProducto=Column(String)
    CantidadProducto=Column( String) 
    Precio_Compra=Column(Double)
    Precio_Venta=Column(Date)
    Iva=Column(Double)
    Categoria=Column(String)



##-------------------------------------------------------------- Parte de ventas 
class Ventas(db.Model):
    __tablename__='ventas'
    Id_Venta=Column(Integer, primary_key=True)
    FechaVenta=Column(Date)
    Hora=Column(Time)
    TotalVenta=Column(Double)
    Subtotal=Column(Double)
    CantProductos=Column(Double)
    Efectivo=Column(Double)
    Cambio=Column(Double)
    Id_Vendedor=Column(Integer , foreign_key=True)




##-------------------------------------------------------------- Parte de DetalleVentas
class DetalleVentas(db.Model):
    __tablename__='detalleventa'
    Id_DetalleVenta=Column(Integer, primary_key=True)
    CodigoBarras=Column(Integer, foreign_key=True)
    NombreProducto=Column(String)
    Cantidad=Column(Double)
    Precio=Column(Double)
    subtotal=Column(Double)
    Iva=Column(Double)
    Id_Venta=Column(Integer , foreign_key=True)




##-------------------------------------------------------------- Parte de Compras 
class Compras(db.Model):
    __tablename__='compras'
    Id_Compra=Column(Integer, primary_key=True)
    FechaCompra=Column(Date)
    TotalCompra=Column(Double)
    CantidadCompra=Column(Double)
    Observaciones=Column(String)
    Id_Proveedor=Column(Integer , foreign_key=True)

   
    

##-------------------------------------------------------------- Parte de Compras 
class Detallecompras(db.Model):
    __tablename__='detallecompras'
    Id_DetalleCompra=Column(Integer, primary_key=True)
    NombreProducto=Column(String)
    CantidadProducto=Column(Double)
    Precio_Producto=Column(Double)
    Subtotal=Column(Double)
    Iva=Column(Double)
    Id_compra=Column(Integer , foreign_key=True)

   
   
    
  

