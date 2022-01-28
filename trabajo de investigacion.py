#Nombres : Vanessa Garcia Cortez, Dayana Quintana Moreira, Ariel Perez Castro 
#1). Ingreso
#2). Consulta
#3). Salir

class Cargo:
    secuencia_cargo_gqp = 2
    cargos = [{"codigo":1,"cargo":"Economista"},{"codigo":2,"cargo":"Ingeniero"}]
    def __init__(self,cargo_gqp):
        Cargo.secuencia_cargo_gqp += 1
        self.codigo_cargo_gqp = Cargo.secuencia_cargo_gqp
        self.cargo_gqp = cargo_gqp

    def registro_cargo_gqp(self):
        return {"codigo":self.codigo_cargo_gqp,"cargo":self.cargo_gqp}

    def mostrar_cargo_gqp(self):
        print("{} - {}".format(self.codigo_cargo_edd,self.cargo_gqp))

    def datos_cargo_gqp(self):
        return [self.codigo_cargo_gqp,self.cargo_gqp]