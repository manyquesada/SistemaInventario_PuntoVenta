from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, Integer, String , Date, Double,Time
db = SQLAlchemy() 


# Parte Vendedores ---------------------------------------------    #

class Vendedor(db.Model):
    __tablename__='vendedor'
    Id_Vendedor=Column(Integer, primary_key=True)
    NombreVendedor=Column(String)
    TelefonoVendedor=Column(Double)
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
    TelefonoProveedor=Column(Double)
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

#

### Parte Inventario 
class Inventario (db.Model):
    __tablename__='inventario'
    CodigoBarras=Column(Integer, primary_key=True)
    NombreProducto=Column(String)
    CantidadProducto=Column( String) 
    Precio_Compra=Column(Double)
    Precio_Venta=Column(Date)
    Iva=Column(Double)
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

   
    
  

