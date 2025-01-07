from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, Integer, String , Date, Double,Time
db = SQLAlchemy() 


# Parte Vendedores ---------------------------------------------    #

class Vendedor(db.Model):
    __tablename__='vendedor'
    Id_Vendedor=Column(Integer, primary_key=True)
    NombreVendedor=Column(String)
    TelefonoVendedor=Column(String)
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
    TelefonoProveedor=Column(String)
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

#----------------------------------------------------------

### Parte Inventario 
class Inventario (db.Model):
    __tablename__='inventario'
    Id_Producto=Column(Integer, primary_key=True)
    CodigoBarras=Column(String)
    NombreProducto=Column(String)
    CantidadProducto=Column(Float) 
    Precio_Compra=Column(Float)
    Precio_Venta=Column(Float)
    Iva=Column(Float)
    Categoria=Column(String)


    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return Inventario.query.get(id)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

   
    
  

