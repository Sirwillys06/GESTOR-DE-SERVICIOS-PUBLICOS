# class Recordatorio:
    
#     def __init__ (self):
        
#         self.recprdatorio=None
#         self.observacion = None
#         self.fecha = None        
        
        
#     def Recordatorios(self):   
#         print("Guarda tu recordatorio: \n")
#         self.recordatorio = input("Escribe tu recordatorio:  ")
#         self.observacion = input("Observaciones (opcional): ")
#         self.fecha = input("Escribe la fecha de tu recordatorio seaparada por /: ")

from datetime import datetime

class Recordatorio:
    
    def __init__(self):
        self.recordatorio = None
        self.observacion = None
        self.fecha = None

    def Recordatorios(self):
        while True:
            print("Guarda tu recordatorio:\n")
            self.recordatorio = input("Escribe tu recordatorio: ")
            self.observacion = input("Observaciones (opcional): ")
            fecha_str = input("Escribe la fecha de tu recordatorio separada por / (formato: DD/MM/YYYY): ")

          
            try:
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
                if fecha < datetime.now():
                    raise ValueError("La fecha ingresada no es valida.")
               
                break
            
            except ValueError as e:
                print(f"Error: {e}\nIntenta nuevamente.")

        self.fecha = fecha