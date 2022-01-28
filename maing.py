from menug import Menu2g
from cargog import Cargos2g
from Departamentog import Departamentos2g
from Empleadosg import Empleados2g
import os

def buscacargo(codC):
    carg = 0
    for bcar in range(0,len(Cargos2g.cargos)):
        car = Cargos2g.cargos[bcar]
        if car["codigo"] == codC:
            carg = car["cargo"]
            break
    return carg

def buscadepartamento(codD):
    deparg = 0
    for bdepa in range(0,len(Departamentos2g.departamentos)):
        departa = Departamentos2g.departamentos[bdepa]
        if departa["codigo"] == codD:
            deparg = departa["departamento"]
            break
    return deparg

def sueldog(sueldo):
    try:
        float(sueldo)
        return True
    except ValueError:
        return False

menu_g = Menu2g()
list = ["1. Cargo","2. Departamento","3. Empleados","4. Salir"]
opcion = ""
while True:
    os.system("cls")
    opcion = menu_g.menu(list,"*** Menú Ficha Personal ***")
    if opcion == "1":
        op1 = ""
        while True:
            os.system("cls")
            op1 = Menu2g.menu("",["1). Ingreso","2). Consulta","3). Salir"],"Mantenimiento de cargos")
            os.system("cls")
            if op1 == "1":
                print(" *** Ingreso de Cargos *** ")
                cargo = input("Cargo a Ingresar: ").strip().capitalize()
                while len(cargo) > 20 or len(cargo) == 0:
                    print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                    cargo = input("Esriba el nombre del cargo: ").strip().capitalize()
                cargo_1 = Cargos2g(cargo)
                cargo_2 = cargo_1.registro_cargosg()
                Cargos2g.cargos.append(cargo_2)
                input("Su ingreso se ha realizaco con éxito // Presione una tecla cualquiera para volver al Menú")
            elif op1 == "2":
                print(" *** Lista de cargos *** ")
                print("Código"," "*7,"Descripción")
                for cargo_1 in Cargos2g.cargos:
                    codCar = cargo_1["codigo"]
                    desCar = cargo_1["cargo"]
                    print(" "*1,codCar," "*(12-len(str(codCar))),desCar)
                input("Presione una tecla cualquiera para volver al Menú")
            elif op1 == "3":
                break
    elif opcion == "2":
        op1 = ""
        while op1 != "3":
            os.system("cls")
            op1 = Menu2g.menu("",["1. Ingreso","2. Consulta","3. Salir"],"Mantenimiento De Departamentos")
            os.system("cls")
            if op1 == "1":
                print(" *** Ingreso de Departamentos *** ")
                departamento = input("Escriba el nombre del departamento: ").strip().capitalize()
                while len(departamento) > 20 or len(departamento) < 5:
                    print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                    departamento = input("Escriba el nombre del departamento: ").strip().capitalize()
                depa = Departamentos2g(departamento)
                depar = depa.registro_depsp6()
                Departamentos2g.departamentos.append(depar)
                input("Su ingreso se ha realizaco con éxito // Presione una tecla cualquiera para volver al Menú")
            elif op1 == "2":
                print(" *** Lista de departamentos ***")
                print("Código"," "*7,"Descripción")
                for depa in Departamentos2g.departamentos:
                    codDep = depa["codigo"]
                    desDep = depa["departamento"]
                    print(" "*1,codDep," "*(12-len(str(codDep))),desDep)
                input("Presione una tecla cualquiera para volver al Menú")
    elif opcion == "3":
        op1 = ""
        while op1 != "3":
            os.system("cls")
            op1 = Menu2g.menu("",["1. Ingreso","2. Consulta","3. Salir"],"Mantenimiento De Empleados")
            os.system("cls")
            if op1 == "1":
                print(" *** Ingreso de Empleados *** ")
                nombre = input("Nombre: ").strip().capitalize()
                while len(nombre) < 3 or len(nombre) > 20:
                    print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                    nombre = input("Nombre: ").strip().capitalize()
                cedula = input("Cédula: ")
                while cedula.isdigit() == False:
                    print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                    cedula = input("Cédula: ")
                if cedula.isdigit() == True:
                    while len(cedula) < 10 or len(cedula) > 10:
                        print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                        cedula = input("Cédula: ")
                cargo_2 = int(input("Ingrese el código del Cargo: "))
                cargo_3 = buscacargo(cargo_2)
                while cargo_3 == 0:
                    print("Error: Código no existe. Ingrese uno válido")
                    cargo_2 = int(input("Ingrese el código del Cargo: "))
                    cargo3 = buscacargo(cargo_2)
                departamento_2 = int(input("Ingrese el código del Departamento: "))
                departamento_3 = buscacargo(departamento_2)
                while departamento_3 == 0:
                    print("Error: Código no existe. Ingrese uno válido")
                    departamento_2 = int(input("Ingrese el código del Departamento: "))
                    departamento_3 = buscacargo(departamento_2)
                sueldo_1 = input("Sueldo: $")
                while sueldog(sueldo_1) is False:
                    print("Error: No es correcto el tipo de dato que ingreso en el sueldo")
                    sueldo_1 = input("Sueldo: $")
                sueldo_1 = round(float(sueldo_1),2)
                empleado_1 = Empleados2g(nombre,cedula,cargo_2,departamento_2,sueldo_1)
                empleado_2 = empleado_1.registro_empleadosg()
                Empleados2g.empleadosg.append(empleado_2)
                input("Su ingreso se ha realizaco con éxito // Presione una tecla cualquiera para volver al Menú")
            elif op1 == "2":
                print(" *** Lista de Empleados *** ")
                print("Código"," "*7,"Nombre"," "*18,"Cédula"," "*13,"Cargo"," "*11,"Departamento", " "*5,"Sueldo")
                for empleado_1 in Empleados2g.empleadosg:
                    codEmp = empleado_1["codigo"]
                    nom = empleado_1["nombre"]
                    cedu = empleado_1["cedula"]
                    cargo4 = empleado_1["cargo"]
                    cargdes = buscacargo(cargo4)
                    depar1 = empleado_1["departamento"]
                    depardes = buscadepartamento(depar1)
                    sueldo2 = empleado_1["sueldo"]
                    print(" "*2,codEmp," "*8,nom," "*(23-len(nom)),cedu," "*(22-len(str(cedu))),cargdes," "*(16-len(str(cargdes))),depardes," "*(16-len(str(depardes))),sueldo2)
                input("Presione una tecla cualquiera para volver al Menú")
    elif opcion == "4":
        print("\nGRACIAS POR USAR EL SISTEMA")

        break            