class Cargogll:
  secuencia=2
  cargos = [{"codigo":1,"cargo":"operador"}, {"codigo":2,"cargo":"Jefa"}]
  def __init__(self, cargo):
    Cargogll.secuencia += 1
    self.codigo = Cargogll.secuencia
    self.descripcion = cargo
  def  registro(self):
    return {"codigo":self.codigo,"cargo":self.descripcion}