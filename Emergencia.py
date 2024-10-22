class EmergenCia:
    def __init__(self, servicio, numero_telefono):
        self.servicio = servicio
        self.numero_telefono = numero_telefono

    def ReportAr(self):
        print(f"Reportar inmediantemente a la línea {self.numero_telefono} para la atención de la emergencia de {self.servicio} desde un teléfono fijo.")

class Agua(EmergenCia):
    def __init__(self):
        super().__init__("agua", "116")

class Luz(EmergenCia):
    def __init__(self):
        super().__init__("luz", "115")

class Gas(EmergenCia):
    def __init__(self):
        super().__init__("gas", "164")

def elegir_servicio():
    print("Seleccione el servicio que desea reportar:")
    print("1. Emergencia de Agua")
    print("2. Emergencia de Luz")
    print("3. Emergencia de Gas")
    opcion = int(input("Ingrese el número correspondiente al servicio: "))
    return opcion

