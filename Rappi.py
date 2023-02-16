#LISTAS Y VARIABLES A UTILIZAR
# [Nombre, Antiguedad, Clave de Departamento]
empleados = {
    920:["Carlos Iram Mendoza", 2, 1], 136:["Leticia Guerrero Franco", 1, 3], 
256:["Christian Israel Rodriguez", 10, 2], 187:["Omar Alejandro Menroz", 5, 2], 283:["Claudia Rodriguez", 3, 3], 
234:["Hipolito Mendoza Pacheco", 1, 2], 564:["Hector Guerrero", 1, 3], 356:["Amalia Franco", 4, 1]}

clave_dep_vacaciones = {1:[6,14,20], 2:[7,15,22], 3:[10,20,30]}

#[Sueldo, Numero Telefonico, Direccion]
info_privada_empleados = {
    920: [7000, 5631341770, "Richard o Robin #2"]
}
#______________________
#______________________ MOSTRAR EMPLEADO
def mostrar_empleado ():
    if id_empleado in empleados:
        nombre, antiguedad, clave = empleados[id_empleado]
        print(f"Nombre del empleado: {nombre}")
        print(f"Antiguedad: {antiguedad} años")
        print(f"Clave de Departamento : {clave}")
        empleado = [nombre, antiguedad, clave]
        return empleado
    else:
        print(f"El ID de empleado {id_empleado} no se encuentra en la lista.")
        pass
#_______________________
#_______________________ MOSTRAR VACACIONES
def mostrar_vacaciones (x):
    print(f"El empleado : {empleado[0]} tendra este 2023",x,"dias de vacaciones")

def clave_empleado1 (empleado):
    if empleado[1] == 1:
        return 6
    elif empleado[1] >= 2 and empleado [1] <= 6:
        return 14
    elif empleado[1] == 0:
        return 0
    else:
        return 20

def clave_empleado2 (empleado):
    if empleado[1] == 0:
        return 0
    elif empleado[1] == 1:
        return 7
    elif empleado[1] >= 2 and empleado [1] <= 6:
        return 15
    else:
        return 22

def clave_empleado3 (empleado):
    if empleado [1] == 0:
        return 0
    elif empleado [1] == 1:
        return 10
    elif empleado [1] >= 2 and empleado <= 6:
        return 20
    else:
        return 30

def calculador_vacacional (empleado):
    if empleado[1] == 1 and empleado [2] == 1:
        print(f"El empleado : {empleado[0]} debe tener este 2023 : 6 dias de vacaciones")
    if empleado[1] == 2 and empleado [2] == 1:
        print(f"El empleado : {empleado[0]} debe tener este 2023 : 14 dias de vacaciones") 
#_______________________
#_______________________ MOSTRAR INFORMACION PERSONAL
def mostrar_info_personal ():
    contraseña = "1825"
    print("Introduzca su contraseña : ")
    contraseña_usuario = str(input())
    if contraseña_usuario not in contraseña: 
        print("Contraseña incorrecta")
    if contraseña_usuario == contraseña:
        if id_empleado in info_privada_empleados:
            sueldo, celular, direccion = info_privada_empleados [id_empleado]
            print(f"Sueldo : {sueldo}")
            print(f"No. Telefonico : {celular}")
            print(f"Direccion : {direccion}")
            return empleado
#----------------------- AMBIENTE GLOBAL AMBIENTE GLOBAL AMBIENTE GLOBAL ----------------

#______________________

#QUE EMPLEADO SE CONSULTARA --- GLOBAL
print ("Rappi, Sistema de vacaciones. Introduzca el ID de empleado")
id_empleado = int(input(": "))
empleado = mostrar_empleado()
#___________________________

#QUE DESEA CONSULTAR SOBRE EL EMPLEADO --- GLOBAL
print ("¿Que deseas saber o hacer acerca de la informacion del empleado?")
funcion_a_realizar = str(input())
funcion = funcion_a_realizar.lower()
#___________________________

#VACACIONES --- GLOBAL
if "vacaciones" in funcion.split():
    if empleado[2] == 1:
        x = clave_empleado1(empleado)
        mostrar_vacaciones(x)
    elif empleado[2] == 2:
        x = clave_empleado2(empleado)
        mostrar_vacaciones(x)
    else:
        x = clave_empleado3(empleado)
        mostrar_vacaciones(x)
#____________________________

#MOSTRAR INFOMACION PERSONAL --- GLOBAL
if "info personal" or "informacion personal" or "personal" in funcion.split():
    mostrar_info_personal()
