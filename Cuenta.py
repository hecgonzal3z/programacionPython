'''Fecha: 18/02/2025
@version: 1.0
@author: Héctor González
'''

def__init__(self,valor,tipo,nombre):
    self.saldo=valor
    self.tipo=tipo
    self.nombre=nombre
    
def imprimirDetalles(self):
    #esta salida es para visualizar el momento de la llamada del método
    print("Desde el método")
    print("saldo::",self.saldo)
    print("tipo::",self.tipo)
    print("nombre::", self,nombre)
    
def retirar(self,cantidad):
    self.saldo=self.saldo-cantidad
    
def depositar(self,monto):
    self.saldo=self.saldo+monto
    