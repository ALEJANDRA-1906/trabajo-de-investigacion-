class Departamentogll:
  secuencia=1
  departamentos = [{"departamento":1, "nombre":"Reporte tecnico" }]
  def __init__(self, descrip):
    Departamentogll.secuencia +=1
    self.codigo = Departamentogll.secuencia
    self.departamento = descrip
  def  registro(self):
    return {"departamento": self.codigo, "nombre": self.departamento}
