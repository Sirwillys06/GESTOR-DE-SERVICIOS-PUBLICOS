class Registro_SP:
    
    def __init__(self):
        self.empresa=None
        self.tipo_servicio = None
        self.nic=None
        



    def Registro_Spublico(self):
        print("Para registrar un servicio, ingrese los siguientes datos: \n")
        self.empresa = input("Empresa prestadora del servicio: ")
        self.tipo_servicio = input("Tipo de servicio (agua, energía, gas): ")
        while True:
            self.nic = input("POLIZA O CONTRATO de la factura del servicio: ")
            if self.nic.isdigit():
                break
            else:
                print("Por favor ingrese solo números.")