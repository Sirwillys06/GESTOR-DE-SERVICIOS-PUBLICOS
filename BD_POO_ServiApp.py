import sqlite3

# --------------------------Método constructor y método conector a la BD--------------------------#
class DataBase:
    def __init__(self, nombre_bd):
        self.Data_base = sqlite3.connect(nombre_bd)
        self.cursor = self.Data_base.cursor()

    # -------------------------Método para crear las tablas dentro de la BD----------------------------#
    def Crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios_ServiApp2 (
            ID INTEGER PRIMARY KEY,
            NOMBRE TEXT NOT NULL,
            EMAIL TEXT NOT NULL UNIQUE,
            USUARIO TEXT NOT NULL UNIQUE,
            CONTRASENA TEXT NOT NULL,
            NUMERO_TELEFONICO INTEGER NOT NULL,
            TIPO_ID TEXT NOT NULL,
            NUMERO_ID INTEGER NOT NULL,
            DEPARTAMENTO TEXT NOT NULL,
            CIUDAD TEXT NOT NULL)""")
        self.Data_base.commit()

    def Crear_tabla2(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ServiPublicos (
            ID INTEGER PRIMARY KEY,
            USUARIO_ID INTEGER NOT NULL,
            EMPRESA_PRESTADORA_SERVICIO TEXT NOT NULL,
            TIPO_SERVICIO TEXT NOT NULL,
            POLIZA_CONTRATO INTEGER NOT NULL,
            FOREIGN KEY (USUARIO_ID) REFERENCES Usuarios_ServiApp2 (ID)
        )""")
        self.Data_base.commit()

    def Crear_tabla3(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Recordatorios_SA (
            ID INTEGER PRIMARY KEY,
            USUARIO_ID INTEGER NOT NULL,
            RECORDATORIOS TEXT NOT NULL,
            OBSERVACIONES TEXT,
            FECHA_DEL_RECORDATORIO TEXT NOT NULL,
            FOREIGN KEY (USUARIO_ID) REFERENCES Usuarios_ServiApp2 (ID)
        )""")
        self.Data_base.commit()
    

        
        
    # -------------------------------------------Método registro de usuarios-----------------------------------------------#
    def Registro_usuarios(self, nombre, email, usuario, contrasena, num_tel, tip_id, num_id, departamento, ciudad):
        try:
            self.cursor.execute("INSERT INTO Usuarios_ServiApp2 (NOMBRE, EMAIL, USUARIO, CONTRASENA, NUMERO_TELEFONICO, TIPO_ID, NUMERO_ID, DEPARTAMENTO, CIUDAD) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (nombre, email, usuario, contrasena, num_tel, tip_id, num_id, departamento, ciudad))
            self.Data_base.commit()
            print("Felicidades Te haz registrado exitosamente!😁")
        except sqlite3.IntegrityError:
            print("lo sentimos el correo o usuario que ingresaste ya está registrado. Por favor, intenta con uno diferente😬.")
            

    # --------------------------------------Método registro de Servicios----------------------------------------------------#
    def Registro_serviP(self, usuario_id, empresa, tipo_servicio, nic):
        try:
            self.cursor.execute(
                "INSERT INTO ServiPublicos (USUARIO_ID, EMPRESA_PRESTADORA_SERVICIO, TIPO_SERVICIO, POLIZA_CONTRATO) VALUES (?, ?, ?, ?)",
                (usuario_id, empresa, tipo_servicio, nic))
            self.Data_base.commit()
            print("Tu servicio público se ha registrado con éxito!")
        except sqlite3.Error as e:
            print("Error, no se pudo registrar tu servicio", str(e))
            

    # ----------------------------------Método inicio de sesión-----------------------------------------------------#
    def inicio_sesion(self, usuario, contrasena):
        self.cursor.execute("SELECT * FROM Usuarios_ServiApp2 WHERE USUARIO=? AND CONTRASENA=?", (usuario, contrasena))
        usuario_encontrado = self.cursor.fetchone()

        if usuario_encontrado:
            print(" ")
            print("Te hemos encontrado 😁!")
            print(f"Bienvenido {usuario_encontrado[1]}!")
            return usuario_encontrado
        else:
            print("Lo sentimos, no te hemos encontrado en nuestra base de datos 🤷, por favor regístrate e intenta nuevamente.")

    # -------------------------------------------Método datos usuarios-------------------------------------------------------------#
    def mostrar_datos_usuario(self, usuario_id):
        self.cursor.execute("SELECT * FROM Usuarios_ServiApp2 WHERE ID=?", (usuario_id,))
        usuario_encontrado = self.cursor.fetchone()

        if usuario_encontrado:
            print("Hola, esta es tu información registrada actualmente:\n")
            print(f"Nombre: {usuario_encontrado[1]}")
            print(f"Email: {usuario_encontrado[2]}")
            print(f"Número de teléfono: {usuario_encontrado[5]}")
            print(f"Tipo de identificación: {usuario_encontrado[6]}")
            print(f"Número de identificación: {usuario_encontrado[7]}")
            print(f"Departamento: {usuario_encontrado[8]}")
            print(f"Ciudad: {usuario_encontrado[9]}")
        else:
            print("El usuario no fue encontrado.")

    # -------------------------------------------Método datos servicios públicos------------------------------------------------------#
    def mostrar_datos_Sp(self, nic):
        self.cursor.execute("SELECT * FROM ServiPublicos WHERE POLIZA_CONTRATO=?", (nic,))
        nic_encontrado = self.cursor.fetchone()

        if nic_encontrado:
            print("Información del servicio público registrado:\n")
            print(f"Empresa Prestadora del servicio: {nic_encontrado[2]}")
            print(f"Tipo de servicio: {nic_encontrado[3]}")
            print(f"NIC o Contrato: {nic_encontrado[4]}")
        else:
            print("NIC no encontrado")

    # -------------------------------------------Método actualizar datos---------------------------------------------------------#
    def actualizar_datos_usuario(self, usuario_id, nueva_info):
        try:
            self.cursor.execute("""
                UPDATE Usuarios_ServiApp2
                SET NOMBRE=?, EMAIL=?, CONTRASENA=?, NUMERO_TELEFONICO=?, TIPO_ID=?, NUMERO_ID=?, DEPARTAMENTO=?, CIUDAD=?
                WHERE ID=?
            """, (*nueva_info, usuario_id))
            self.Data_base.commit()
            print("Datos del usuario actualizados exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al actualizar datos del usuario: {e}")


    # ------------------------------------------------Método para cerrar base de datos------------------------------------------#
    def cerrar(self):
        print("Gracias por usar ServiApp 💡, hasta pronto!")
        self.Data_base.close()
        
     #-----------------------------------------metodo para agregar recordatorios-------------------------------------------#   
    def Agregar_recordatorios(self,usuario_id,recordatorio,observacion,fecha):
        try:
            self.cursor.execute(
                "INSERT INTO Recordatorios_SA (USUARIO_ID,RECORDATORIOS, OBSERVACIONES,FECHA_DEL_RECORDATORIO ) VALUES (?, ?, ?, ?)",
                (usuario_id,recordatorio,observacion,fecha))
            self.Data_base.commit()
            print("Tu servicio recordatorio se ha registrado con éxito!")
        except sqlite3.Error as e:
            print("Error, no se pudo registrar tu recordatorio", str(e))
      #----------------------------------------------------metodo para mostrar recordatorios---------------------------------------------#      
    def mostrar_recordatorios(self, usuario_id):
        self.cursor.execute("SELECT * FROM Recordatorios_SA WHERE USUARIO_ID=?", (usuario_id,))
        recordatorios = self.cursor.fetchall()

        if recordatorios:
            for recordatorio in recordatorios:
                print(f"ID: {recordatorio[0]}")
                print(f"Recordatorio: {recordatorio[2]}")
                if recordatorio[3]: #Este if verifica si hay o no observaciones registradas
                    print(f"Observaciones: {recordatorio[3]}")
                print(f"Fecha del Recordatorio: {recordatorio[4]}\n")
        else:
            print("No tienes recordatorios registrados.")
        #-------------------------------------------------------Metido para eliminar recordatorios---------------------------------------------#
    def eliminar_recordatorio(self, usuario_id, id_recordatorio):
        self.cursor.execute("DELETE FROM Recordatorios_SA WHERE USUARIO_ID=? AND ID=?", (usuario_id, id_recordatorio))
        self.Data_base.commit()
        print("Recordatorio eliminado con éxito.")
        
        
   