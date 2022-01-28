# import os
# os.system("cls")

class Menu2g:
    def __init__(self):
        pass
    def menu(self,opciones,titulo):
        print(titulo)
        for x in opciones:
            print(x)
        opc = input("Elija la Opción[1...{}]: ".format(len(opciones)))