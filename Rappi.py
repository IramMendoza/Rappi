import Asistente_Rappi as Asistente
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

#----------------------- AMBIENTE GLOBAL AMBIENTE GLOBAL AMBIENTE GLOBAL ----------------
Asistente = Asistente
#______________________

#QUE EMPLEADO SE CONSULTARA --- GLOBAL
print ("Rappi, Sistema de vacaciones. Introduzca el ID de empleado")
id_empleado = int(input(": "))
empleado = mostrar_empleado()
#___________________________

#QUE DESEA CONSULTAR SOBRE EL EMPLEADO --- GLOBAL
print ("Que deseas saber o hacer acerca de la informacion del empleado?")
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
if "info personal" or "informacion personal" or "personal" in funcion:
    mostrar_info_personal()
# Esto muestra que mis ideas sobre un commit funciona!
#VEAMOS