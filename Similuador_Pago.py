from tqdm import tqdm
from time import sleep
class Pagar:
    
    def __init__ (self):
        self.titular= None
        self.num_tarjeta = None
        self.cvc = None
        self.F_vencimiento = None
        self.valor = None
        self.Servicio_p = None
        self.Tipo_tarjeta= None
        
    def Cargador(self):
        print("Procesando pago...")
        print(" ")
        for i in tqdm (range(10)):
            sleep (.100)
        print(" ")
        print("Pago exitoso!")
        
    def information(self):
        
        print("Ingresa los siguientes datos para hacer el pago: ")
        
        self.titular = input ("Nombre Titular: ")
        self.Tipo_tarjeta = input("Ingresa el tipo de tarjeta (Debito/Credito): ")
        while True:
            self.num_tarjeta = input("Número de tarjeta: ")
            if self.num_tarjeta.isdigit():
                self.num_tarjeta = self.num_tarjeta
                break
            else:
                print("Por favor ingrese solo números.")
        while True:
            self.cvc = input("CVC: ")
            if self.cvc.isdigit():
                self.cvc = self.cvc
                break
            else:
                print("Por favor ingrese solo números.")
        self.F_vencimiento = input("Ingresa la fecha de expedicion separado por /:  ")
        while True:
            self.valor = input("Valor sin puntos ni comas:  ")
            if self.valor.isdigit():
                self.valor = self.valor
                break
            else:
                print("Por favor ingrese solo números.")
        self.servicio_p = input("Ingresa el servicio a pagar: ")
        print(" ")
        
    def Resumen(self):
        print("Resumen de tu pago:\n")
        print(f"Servicio pagado: {self.servicio_p}")
        print(f"Valor: {self.valor}")
        print(f"Pagado a nombre de: {self.titular}")
        
        
                
    
            
        
        
        