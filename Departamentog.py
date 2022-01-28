class Departamentos2g:
    secuencia_deparg = 2
    departamentos = [{"codigo":1,"departamento":"Reporte Técnico"},{"codigo":2,"departamento":"Talento Humano"}]
    def __init__(self,deparg):
        Departamentos2g.secuencia_deparg += 1
        self.codigo_deparg = Departamentos2g.secuencia_deparg
        self.deparg = deparg

    def registro_depg(self):
        return {"codigo":self.codigo_deparg,"departamento":self.deparg}

    def mostrar_depg(self):
        print("{} - {}".format(self.codigo_deparg,self.deparg))

    def datos_depg(self):
        return [self.codigo_deparg,self.deparg]