class Cargos2g:
    secuencia_cargosg = 2
    cargos = [{"codigo":1,"cargo":"Tester"},{"codigo":2,"cargo":"Director"}]
    def __init__(self,cargo_g):
        Cargos2g.secuencia_cargosg += 1
        self.codigo_g = Cargos2g.secuencia_cargosg
        self.cargo_g = cargo_g

    def registro_cargosg(self):
        return {"codigo":self.codigo_g,"cargo":self.cargo_g}

    def mostrar_cargosg(self):
        print("{} - {}".format(self.codigo_g,self.cargo_g))

    def datos_cargosg(self):
        return [self.codigo_g,self.cargo_g]
