class Registro_usuario:
    def __init__(self):
        self.__Nombre = None 
        self.__Email = None
        self.__Usuario = None
        self.__Contrasena = None
        self.__Num_tel = None
        self.__Tip_id = None #No
        self.__Num_id = None
        self.__Departamento = None#No
        self.__Ciudad = None

    # Getters

    def get_name(self):
        return self.__Nombre

    def get_correo(self):
        return self.__Email

    def get_user(self):
        return self.__Usuario

    def get_password(self):
        return self.__Contrasena

    def get_numero_tel(self):
        return self.__Num_tel

    def get_tipo_id(self):
        return self.__Tip_id

    def get_numero_id(self):
        return self.__Num_id

    def get_departamento(self):
        return self.__Departamento

    def get_ciudad(self):
        return self.__Ciudad

    # Setters

    def set_name(self, new_name):
        self.__Nombre = new_name

    def set_correo(self, new_correo):
        self.__Email = new_correo

    def set_user(self, new_user):
        self.__Usuario = new_user

    def set_password(self, new_password):
        self.__Contrasena = new_password

    def set_numero_tel(self, new_numero_tel):
        self.__Num_tel = new_numero_tel

    def set_tipo_id(self, new_tipo_id):
        self.__Tip_id = new_tipo_id

    def set_numero_id(self, new_numero_id):
        self.__Num_id = new_numero_id

    def set_departamento(self, new_departamento):
        self.__Departamento = new_departamento

    def set_ciudad(self, new_ciudad):
        self.__Ciudad = new_ciudad

    def Registro(self):
        print("Por favor ingrese los siguientes datos para registrarse: \n")
        self.set_name(input("Nombre: "))
        self.set_correo(input("Email: "))
        self.set_user(input("Usuario: "))
        self.set_password(input("Contraseña: "))

        while True:
            num_tel = input("Número de teléfono: ")
            if num_tel.isdigit():
                self.set_numero_tel(num_tel)
                break
            else:
                print("Por favor ingrese solo números.")

        self.set_tipo_id(input("Tipo de identificación: "))

        while True:
            num_id = input("Número de identificación: ")
            if num_id.isdigit():
                self.set_numero_id(num_id)
                break
            else:
                print("Por favor ingrese solo números.")

        self.set_departamento(input("Departamento: "))
        self.set_ciudad(input("Ciudad: "))
