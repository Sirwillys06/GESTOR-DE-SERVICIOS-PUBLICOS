class Inicio_sesion:
    
    def __init__ (self):
        self.usuario=None
        self.contraseña=None
        
    def Login (self):
        self.usuario = input("Ingrese usuario: ")
        self.contrasena = input("Ingrese contraseña: ")
    