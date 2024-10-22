#-----------------------------------------Importacion de los archivos y sus respectivas clases----------------------------------#
from os import system
system('cls')  
from BD_POO_ServiApp import DataBase
from Registro_usuario import Registro_usuario
from Registro_SP import Registro_SP
from Iniciar_Sesion import Inicio_sesion
from Recordatorios import Recordatorio
from Emergencia import Agua, Gas, Luz, elegir_servicio
from Similuador_Pago import Pagar



# -------------------------------------Instanciar Database, darle nombre al archivo de la base de datos y crear objeto (data_base)-----------------------------------------#
db_nombre = "Usuarios_ServiApp.db"
data_base = DataBase(db_nombre)
data_base.Crear_tabla() #USUARIO
data_base.Crear_tabla2() # SERVICIOS
data_base.Crear_tabla3() # RECORDATORIOS

#----------------------------------Variable Iniciadora---------------------------------------------#
usuario_encontrado = None

print("¡Bienvenid@ a ServiApp💡!\n")

while True:
  
    print("----------------Menu de opciones-------------------\n")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    # uno solo 
    print("3. Registrar servicio público")# si
    
    print("4. Mostrar datos del usuario registrado")#No y si
    print("5. Mostrar Datos del servicio registrado")#No y si
    
    print("6. Actualizar datos del usuario")#No
    
    print("7. Agregar un recordatorio")#si
    print("8. Mostrar recordatorios")#si
    print("9. Eliminar recordatorio")#si
    
    print("10. Reportar Emergencias")# Si cambiando el nombre numeros de emergencias
    print("11. Pagar servcio publico")# encontrar forma de hacerlo (tentativo)
    #-----------------------------------Estadisticas------------------------------#
    # elegir cuantos meses va a calcular minmo 3
    # Pedir datos de los KW/H consumidos en cada mes

    #----------------Admin---------------#
    #Hacer promedio del consumo y comparar con el promedio del usuario
    # Condiciones:
    #Si el consumo excede el promedio Alertar y recomendaciones
    #Si el consumo esta por debajo del promedio felicitar y dar consejos para seguir asi
    #si el consumo esta cerca de excederse alertar y dar consejos.
    
    
    
    print("12. Salir\n") 
    opcion = input("Ingrese el número de la opción: ")

    while opcion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
        print("La opción escogida no está disponible, intenta nuevamente.\n")
        opcion = input("Ingrese el número de la opción: ")

    print(" ")

    

    if opcion == "1":
        datos_usuario = Registro_usuario()
        datos_usuario.Registro()


        nombre = datos_usuario.get_name()
        email = datos_usuario.get_correo()
        usuario = datos_usuario.get_user()
        contrasena = datos_usuario.get_password()
        num_tel = datos_usuario.get_numero_tel()
        tip_id = datos_usuario.get_tipo_id()
        num_id = datos_usuario.get_numero_id()
        departamento = datos_usuario.get_departamento()
        ciudad = datos_usuario.get_ciudad()
        
       

        data_base.Registro_usuarios(nombre, email, usuario, contrasena, num_tel, tip_id, num_id, departamento, ciudad)




    elif opcion == "2":
        login = Inicio_sesion()
        login.Login()
        usuario_encontrado = data_base.inicio_sesion(login.usuario, login.contrasena)

    elif opcion == "3":
        if usuario_encontrado:
            datos_servicio = Registro_SP()
            datos_servicio.Registro_Spublico()
            data_base.Registro_serviP(usuario_encontrado[0], datos_servicio.empresa,
                                      datos_servicio.tipo_servicio, datos_servicio.nic)
        else:
            print("Debes iniciar sesión primero.")

    elif opcion == "4":
        if usuario_encontrado:
            data_base.mostrar_datos_usuario(usuario_encontrado[0])
        else:
            print("Para mostrar la información debes primero iniciar sesión.")

    elif opcion == "5":
        if usuario_encontrado:
            nic = int(input("Ingresa el contrato o póliza del servicio que tienes registrado: "))
            data_base.mostrar_datos_Sp(nic)
        else:
            print("Para mostrar los datos debes primero iniciar sesión.")
    elif opcion == "6":
        if usuario_encontrado:
            print("Actualizar datos del usuario:\n")
            nuevo_nombre = input(f"Nombre actual: {usuario_encontrado[1]}, ingrese nuevo nombre: ") or usuario_encontrado[1]
            nuevo_email = input(f"Email actual: {usuario_encontrado[2]}, ingrese nuevo Email: ") or usuario_encontrado[2]
            nueva_contrasena = input(f"Contraseña actual: {usuario_encontrado[4]}, ingresa nueva contraseña : ") or usuario_encontrado[4]
            nuevo_num_tel = input(f"Número de teléfono actual: {usuario_encontrado[5]}, ingresa nuevo número tel: ") or usuario_encontrado[5]
            nuevo_tip_id = input(f"Tipo de identificación actual: {usuario_encontrado[6]}, Ingresa nuevo tipo de identificación: ") or usuario_encontrado[6]
            nuevo_num_id = input(f"Número de identificación actual: {usuario_encontrado[7]}, ingresa nuevo número de identificación: ") or usuario_encontrado[7]
            nuevo_departamento = input(f"Departamento actual: {usuario_encontrado[8]}, ingrese nuevo departamento: ") or usuario_encontrado[8]
            nueva_ciudad = input(f"Ciudad actual: {usuario_encontrado[9]}, ingrese nueva ciudad: ") or usuario_encontrado[9]

            nueva_info = (nuevo_nombre, nuevo_email, nueva_contrasena, nuevo_num_tel, nuevo_tip_id, nuevo_num_id, nuevo_departamento, nueva_ciudad)
            data_base.actualizar_datos_usuario(usuario_encontrado[0], nueva_info)
        else:
            print("Debes iniciar sesión primero.")

    

    elif opcion == "7":
        if usuario_encontrado:
            recordar = Recordatorio()
            recordar.Recordatorios()
            data_base.Agregar_recordatorios(usuario_encontrado[0], recordar.recordatorio, recordar.observacion, recordar.fecha)
        else:
            print("Debes iniciar sesión primero.")

    elif opcion == "8":
        if usuario_encontrado:
            print("Tus recordatorios son:")

            data_base.mostrar_recordatorios(usuario_encontrado[0])
        else:
            print("Debes iniciar sesión primero.")

    elif opcion == "9":
        if usuario_encontrado:
            id_recordatorio = input("Ingresa el ID del recordatorio que deseas eliminar: ")
            data_base.eliminar_recordatorio(usuario_encontrado[0], id_recordatorio)
        else:
            print("Debes iniciar sesión primero.")
            
    elif opcion == "10":
        if usuario_encontrado:
            opcion_emergencia = elegir_servicio()

            if opcion_emergencia == 1:
                emergencia = Agua()
            elif opcion_emergencia == 2:
                emergencia = Luz()
            elif opcion_emergencia == 3:
                emergencia = Gas()
            else:
                print("Opción no válida")
    
            emergencia.ReportAr()
        else:
            print("Debes iniciar sesión primero.")
            
    elif opcion == "11":
        
        if usuario_encontrado:
            pay = Pagar()
            pay.information()
            pay.Cargador()
            pay.Resumen()
        else: 
            print("Primero debes inicar sesion")
    elif opcion == "12":
        data_base.cerrar()
        break
    else:
        print("Opcion incorrecta!")
            
