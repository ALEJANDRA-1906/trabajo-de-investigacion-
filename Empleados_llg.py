from Cargo_llg import Cargollg   
class Empleadollg:
  secuenciallg=1
  Empleados= [{"codigo":1,"nombre":"Kleinny","cedula":"0951995331","cargo":"Jefa","departamento":"Recursos humanos","sueldo":750.90}]
  def __init__(self,Nombre,Cedula,CodiCargo,CodiDepartamento,Sueldo ):
    Empleadollg.secuenciallg +=1
    self.Codigollg = Empleadollg.secuenciallg
    self.Nombrellg = Nombre
    self.Cedulallg= Cedula
    self.Cargollg = CodiCargo
    self.Departamentollg = CodiDepartamento
    self.Sueldollg = Sueldo
  def  registro(self):
    return {"codigo": self.Codigollg, "nombre": self.Nombrellg, "cedula": self.Cedulallg, "cargo": self.Cargollg, "departamento": self.Departamentollg, "sueldo": self.Sueldollg}