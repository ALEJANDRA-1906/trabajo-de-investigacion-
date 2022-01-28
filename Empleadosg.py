from cargog import Cargo2g 
from Departamentog import Departamentos2g

class Empleadosg:
    secuencia_empleadosg = 2
    empleadosg = [{"codigo":1,"nombre":"Carlos","cedula":"0927954271","cargo":1,"departamento":1,"sueldo":500.00}]

    def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo):
        Empleadosg.secuencia_empleadosg += 1
        self.codigo_empleado = Empleadosg.secuencia_empleadosg
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = codCargo
        self.departamento = codDepartamento
        self.sueldo = sueldo

    def mostrar_empleadosg(self):
            print("{} - {} - {} - {}".format(self.codigo_empleado,self.nombre,self.cedula,self.cargo,self.departamento))

    def registro_empleadosg(self):
        return{"codigo":self.codigo_empleado,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"departamento":self.departamento,"sueldo":self.sueldo}