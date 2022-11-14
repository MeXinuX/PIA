#################### IMPORTACION DE LIBRERIAS REQUERIDAS ####################

#Esta libreria la importamos para la creacion de animaciones
from __future__ import unicode_literals
from optparse import Values

#Esta libreria la importamos para la creacion de animaciones
####!!! ESTA LIBRERIA NO VIENE POR DEFECTO EN PYTHON HAY QUE INSTALARLA !!! ####
from halo import Halo

#Esta libreria la importamos para la manipulacion de base de datos
import sqlite3
from sqlite3 import Error

#Esta libreria la importamos para realizar validaciones
import re

#Esta libreria la importamos para realizar validacion de fecha posible al momento de hacer una reservacion
import datetime

#Esta libreria la importamos para la creacion de animaciones
import time

#Esta libreria la importamos para la creacion de animaciones
import sys

#Esta libreria la importamos para el uso de CSV
import os

#Esta LIbreria la Importamos para el manejo de excel
import pandas as pd

####!!! ESTA LIBRERIA NO VIENE POR DEFECTO EN PYTHON HAY QUE INSTALARLA !!! ####

#Esta libreria la importamos para la creacion de animaciones
from tqdm import tqdm

#Esta libreria la importamos para la creacion de animaciones
from time import sleep


#COLORES PARA LA IMPRESION DE TEXTO EN PANTALLA
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[35m'

#################### CREACION DE FUNCIONES PARA LAS ANIMACIONES ####################
def create_animation(mensaje):#Animacion De Creacion de un Cliente
    numero = 100
    print(GREEN + f"\n {mensaje}")
    for i in tqdm(range(numero)):
        sleep(0.01)
    sleep(0)
    os.system('clear')

#Animacion de busqueda exitosa
def load_box(texto,mensaje):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    spinner = Halo(text=mensaje,color="blue", spinner="dots")

    try:
        spinner.start()
        time.sleep(4)
        spinner.succeed(texto)
    except (KeyboardInterrupt, SystemExit):
        spinner.stop()

#Animacion de busqueda fallida
def fail_load_box(texto,mensaje):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    spinner = Halo(text=mensaje,color="blue", spinner="dots")

    try:
        spinner.start()
        time.sleep(4)
        spinner.fail(texto)
    except (KeyboardInterrupt, SystemExit):
        spinner.stop()

#Animacion de cerrado de programa
def exit_animation():
    sys.stdout.write('\rSaliendo')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo.')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo..')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo...')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo....')
    time.sleep(0.2)
    os.system('clear')
def validar_numero(numero):
    while True:
        if numero == "":
            print(RED + "⛔ Debe Ingresar Un 🆔.\n")
            continue

        if (not re.match("^[0-9]*$", numero)):
            print(RED + "⛔ El 🆔 Del Cliente Debe Ser Un Número, Intente De Nuevo.\n")
            continue
        numero = int(numero)
        break


try:
    with sqlite3.connect("SalasCoworking.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id_cliente INTEGER NOT NULL PRIMARY KEY ,nombre_cliente TEXT NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS salas (id_sala INTEGER  NOT NULL PRIMARY KEY,nombre_sala TEXT NOT NULL,cupo_sala INTEGER NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS reservaciones (folio_reservacion INTEGER NOT NULL PRIMARY KEY ,fecha_reservacion TIMESTAMP NOT NULL,turno_reservacion text NOT NULL,fk_id_cliente INTEGER NOT NULL,nombre_cliente TEXT NOT NULL,fk_id_sala INTEGER NOT NULL,nombre_sala TEXT NOT NULL,nombre_evento TEXT NOT NULL,FOREIGN KEY(fk_id_cliente) REFERENCES clientes(id_cliente),FOREIGN KEY(fk_id_sala) REFERENCES salas(id_sala));")
except:
    print("☹ Ocurrió Un Error")

os.system('clear')
while True:
    #Limpieza De Pantalla
    print(BLACK + """\n
     -----------Menú de opciones----------
    |1)🎟️ Reservaciones                    |
    |2)🗃️ ​Reportes                         |
    |3)🛖 Registrar Una Sala               |
    |4)🚹​​Registrar Nuevo Cliente          |
    |5)✖ Salir                            |
     -------------------------------------""")
    menu = input("\nIngresa una opción del menú: ").strip()

    if menu not in "12345":
        print(RED + "⛔ Ingrese Una Opción Disponible Del Menú\n" + BLACK)
        continue

    #Salir
    if menu == "5":
        exit_animation()
        conn.close()
        break

    #Reservaciones
    if menu == "1":
        #Limpieza De Pantalla
        os.system('clear')

        while True:
            try:
                mi_cursor.execute("SELECT * FROM salas")
                registro_salas = mi_cursor.fetchall()

                mi_cursor.execute("SELECT * FROM clientes")
                registro_cliente = mi_cursor.fetchall()


                if not registro_salas:
                    print(RED + "⛔ No Se Encontró Ninguna Sala, Favor De Registrar Una.\n")
                    break

                if not registro_cliente:
                    print(RED + "⛔ No Se Encontró Ninguna Cliente, Favor De Registrar Uno.\n")
                    break
            except:
                print("☹ Ocurrió Un Error")

            print(BLACK + """\n
             --------------------Menú de opciones------------------
            |1)🆕Registrar Nueva Reservación                       |
            |2)✍ Modificar Descripcion De Una Reservación          |
            |3)🗓️ Consultar Disponibilidad De Salas Para Una Fecha  |
            |4)🗑️ Eliminar Una Reservación                          |
            |5)↩ Volver Al Menú Principal                          |
             ------------------------------------------------------""")
            sub_menu = input("\nIngresa una opción del menú: ").strip()

            if sub_menu not in "12345":
                print(RED + "⛔ Ingrese Una Opción Disponible Del Menú.\n" + BLACK)
                continue

            #Salir
            if sub_menu == "5":
                #Limpieza De Pantalla
                os.system('clear')
                break

            #Registrar Nueva Reservación
            if sub_menu == "1":
                #Limpieza De Pantalla
                os.system('clear')

                try:
                    mi_cursor.execute("SELECT * FROM clientes")
                    registro = mi_cursor.fetchall()

                    print(BLACK + "🆔 CLIENTE\t\tNOMBRE CLIENTE")
                    for id, nombre in registro:
                        print(f"{id}\t\t\t\t{nombre}")
                except:
                    print(RED + "☹ Ocurrió Un Error")

                while True:
                    id_cliente = input(BLACK + f"Ingrese Su 🆔 De Cliente:  ").strip()
                    if id_cliente == "":
                        print(RED + "⛔ Debe Ingresar Un 🆔.\n")
                        continue

                    if (not re.match("^[0-9]*$", id_cliente)):
                        print(RED + "⛔ El 🆔 Del Cliente Debe Ser Un Número, Intente De Nuevo.\n")
                        continue
                    id_cliente = int(id_cliente)

                    try:
                        valores = {"id_cliente":id_cliente}
                        mi_cursor.execute("SELECT id_cliente FROM clientes WHERE id_cliente = :id_cliente", valores)
                        registro = mi_cursor.fetchall()

                        if not registro:
                            print(RED + "⛔ No Se Encontró Su 🆔 De Cliente, Favor De Registrarse Como Cliente. \n")
                            break

                    except:
                        print(RED + "☹ Ocurrió Un Error")

                    try:
                        mi_cursor.execute("SELECT * FROM salas ORDER BY id_sala")
                        registro = mi_cursor.fetchall()

                        if not registro:
                            print(RED + "⛔ No Se Encontró Ninguna Sala, Favor De Registrar Una.\n")
                            break
                        else:
                            print(BLACK + "🆔 SALA\t\tNOMBRE SALA\tCUPO")
                            for id, nombre,cupo in registro:
                                print(f"{id}\t\t{nombre}\t\t{cupo}")
                    except:
                        print(RED + "☹ Ocurrió Un Error.\n")


                    while True:
                        sala = input("Seleccione una sala:  ").strip()

                        if sala == "":
                            print(RED + "⛔ Debe Seleccionar Una Sala. \n")
                            continue

                        if(not re.match("^[0-9]*$",sala)):
                            print(RED + "⛔ El 🆔 De La Sala Es Un Número, Intente De Nuevo. \n")
                            continue

                        sala = int(sala)

                        buscar_sala = {"id_sala":sala}
                        mi_cursor.execute("SELECT id_sala FROM salas WHERE id_sala = :id_sala", buscar_sala)
                        salarecuperada = mi_cursor.fetchall()
                        for id in salarecuperada:
                            salarecuperada = id


                        if not salarecuperada:
                            print(RED + "⛔ No Se Encontró Ninguna Sala con ese ID.")
                            continue

                        break
                    while True:
                        fecha_reservacion = input(BLACK + "🗓️ Ingrese La Fecha Deseada Con El Formato (dd/mm/aaaa): \n").strip()
                        if fecha_reservacion == "":
                            print(RED + "⛔ Debe Ingresar Una Fecha.\n")
                            continue

                        if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_reservacion)):
                            print(RED + "⛔ La Fecha Debe Tener El Formato(dd/mm/aaaa). \n")
                            continue

                        try:
                            fecha_reservacion = datetime.datetime.strptime(fecha_reservacion,"%d/%m/%Y").date()
                        except:
                            print(RED + "⛔ La Fecha Ingresada No Es Una Fecha Válida, Intente De Nuevo. \n")
                            continue

                        fecha_actual = (datetime.date.today())
                        limite_fecha = (fecha_reservacion - fecha_actual).days
                        if limite_fecha <=1:
                            print(RED + "⛔ Se Necesitan 2 Días De Anticipación. \n")
                            continue
                        break

                    while True:
                        turno = input(BLACK + """\n
                        ----------Turnos----------
                        ( 🅼  )🌥️ Matutino
                        ( 🆅  )☀️ Vespertino
                        ( 🅽  )🌜 Nocturno
                        ( 🆂  )✖ Salir
                        --------------------------\nSeleccione Un Turno:  """).upper().strip()

                        if turno not in "MVNS":
                            print(RED + "⛔ Debes Seleccionar Una Opción Disponible En El Menú, Intenta De Nuevo. \n")
                            continue

                        if turno == "":
                            print(RED + "⛔ Debe Seleccionar Un Turno. \n")
                            continue

                        if turno == "S":
                            break

                        if turno == "M":
                            turno="Matutino"

                        if turno == "V":
                            turno="Vespertino"

                        if turno == "N":
                            turno="Nocturno"

                        try:
                            criterios = {"fecha":fecha_reservacion,"turno":turno}
                            mi_cursor.execute("SELECT fecha_reservacion,turno_reservacion FROM reservaciones WHERE DATE(fecha_reservacion) == :fecha AND turno_reservacion=:turno;", criterios)
                            registros = mi_cursor.fetchall()

                            if registros:
                                print(RED + "⛔ Ya Existe Una Reservación En Ese Turno, Favor De Ingresar Otro Turno. \n")
                                continue

                            while True:
                                nombre_evento = input(BLACK + "Ingrese El Nombre Del Evento: ").title().strip()
                                if nombre_evento == "":
                                    print(RED + "⛔ Debe Ingresar Un Nombre Del Evento. \n")
                                    continue
                                break


                            values_salas={"id_sala":sala}
                            mi_cursor.execute("SELECT nombre_sala FROM salas where id_sala=:id_sala",values_salas)
                            query_sala=mi_cursor.fetchone()

                            for s in query_sala:
                                query_sala = s

                            mi_cursor.execute("SELECT nombre_cliente FROM clientes where id_cliente=:id_cliente",valores)
                            query_cliente=mi_cursor.fetchone()


                            for c in query_cliente:
                                query_cliente = c

                            reservaciones = (fecha_reservacion,turno,id_cliente,query_cliente,sala,query_sala,nombre_evento)
                            mi_cursor.execute("INSERT INTO reservaciones (fecha_reservacion,turno_reservacion,fk_id_cliente,nombre_cliente,fk_id_sala,nombre_sala,nombre_evento) VALUES(?,?,?,?,?,?,?);", reservaciones)
                            conn.commit()
                            mi_cursor.execute("SELECT MAX(folio_reservacion),fecha_reservacion,turno_reservacion,nombre_cliente,nombre_sala,nombre_evento FROM reservaciones;")
                            reservacion_creada = mi_cursor.fetchall()

                            create_animation("Realizando Reservación.")

                            print(GREEN + "✓ Reservación Creada Con Éxito.\n")

                            print(BLACK + "FOLIO RESERVACIÓN\t\tFECHA RESERVACIÓN\t\tTURNO\t\tNOMBRE CLIENTE\t\tNOMBRE SALA\t\tNOMBRE DEL EVENTO")
                            for fol, fecha,turno,cliente,sala,evento in reservacion_creada:
                                print(f"{fol}\t\t\t\t{fecha}\t\t\t{turno}\t{cliente}\t\t\t{sala}\t\t{evento}")

                        except Exception:
                            print(RED + "☹ Ocurrió Un Error.\n")
                        break
                    break

            #Modificar Descripcion
            if sub_menu == "2":
                #Limpieza De Pantalla
                os.system('clear')

                while True:
                    folio = input(BLACK + "Ingrese El Folio De Reservación: ").strip()
                    if folio == "":
                        print(RED + "⛔ Debe Ingresar El Folio De Reservación.\n")
                        continue

                    if(not re.match("^[0-9]*$",folio)):
                        print(RED + "⛔ El Folio De Reservación Debe Ser Un Numero.\n")
                        continue
                    folio = int(folio)
                    try:
                        valores = {"folio_reservacion":folio}
                        mi_cursor.execute("SELECT nombre_evento FROM reservaciones WHERE folio_reservacion = :folio_reservacion", valores)
                        registro = mi_cursor.fetchone()

                        if not registro:
                            fail_load_box("Reservación No Encontrada","Buscando Reservación")
                            print(RED + "⛔ No se encontró Una Reservación Con Ese Folio.\n")
                            break

                        load_box("Reservación Encontrada","Buscando Reservación")
                        nombre_antiguo=""
                        for nombre in registro:
                            nombre_antiguo=nombre
                        print("El nombre de La Reservación Es: " + BLUE + f"{nombre_antiguo}\n")
                    except:
                        print(RED + "☹ Ocurrió Un Error.\n")
                        break

                    while True:
                        nuevo_nombre = input(BLACK + "Ingrese El Nuevo Nombre De Su Evento: ").title().strip()
                        if nuevo_nombre == "":
                            print(RED + "⛔ Debe Ingresar Un Nombre Del Evento.\n")
                            continue

                        mi_cursor.execute('UPDATE reservaciones SET nombre_evento = (?) WHERE folio_reservacion=(?);',[nuevo_nombre,folio])
                        conn.commit()
                        create_animation("Actualizando Nombre Del Evento")

                        print(GREEN + "✓ Se Modificó el Nombre Del Evento.")
                        print(BLACK + "Nombre Anterior: " + BLUE + f"{nombre_antiguo}")
                        print(BLACK + "Nombre Nuevo: " + BLUE +  f"{nuevo_nombre}")
                        break
                    break

            #Consultar Disponibilidad
            if sub_menu == "3":
                #Limpieza De Pantalla
                os.system('clear')
                while True:
                    fecha_consulta = input(BLACK + "Ingrese La Fecha Qué Desea Consultar: ").strip()
                    if fecha_consulta == "":
                        print(RED + "⛔ Debe Ingresar una Fecha.\n")
                        continue

                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print(RED +"⛔ La Fecha Debe Tener El Formato(dd/mm/aaaa).\n")
                        continue

                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print(RED + "⛔ La Fecha Ingresada No es una Fecha Valida, Intente De Nuevo.\n")
                        continue

                    try:
                        criterios = {"fecha":fecha_consulta}
                        mi_cursor.execute("SELECT fk_id_sala,turno_reservacion FROM reservaciones WHERE DATE(fecha_reservacion) == :fecha;", criterios)
                        reservaciones_encontrados = mi_cursor.fetchall()

                        combinacion_reservas_encontradas = set(reservaciones_encontrados)

                        turnos = ["Matutino","Vespertino","Nocturno"]

                        mi_cursor.execute("SELECT nombre_sala FROM salas")
                        salas_encontradas = mi_cursor.fetchall()

                        salas_finales = []
                        for salas in salas_encontradas:
                            sala = salas[0]
                            salas_finales.append(sala)

                        reservaciones_posibles = []
                        for sala in salas_finales:
                            for turno in turnos:
                                reservaciones_posibles.append((sala,turno))
                            combinaciones_reservas_posibles = set((reservaciones_posibles))

                        reservas_posibles = set((combinaciones_reservas_posibles - combinacion_reservas_encontradas))
                        lista_reservas_posibles = list(reservas_posibles)
                        lista_reservas_posibles.sort()

                        load_box("Salas Disponibles","Buscando Disponibilidad")
                        print('SALA\t\tTURNO')
                        for sala,turno in lista_reservas_posibles:
                            print(f'{sala}\t\t{turno}')

                        break
                    except:
                        print(RED + "☹ Ocurrió Un Error.\n")
                    break

            #Eliminar Una Reservación
            if sub_menu == "4":
                #Limpieza De Pantalla
                os.system('clear')

                while True:
                    try:
                        mi_cursor.execute("SELECT * FROM reservaciones")
                        registro = mi_cursor.fetchall()

                        if not registro:
                            print(RED + "⛔ No Existe Ninguna Reservación, Favor De Registrar Una.\n")
                            break

                    except:
                        print(RED + "☹ Ocurrió Un Error.\n")

                    folio = input("Ingrese El Folio De Reservación: ").strip()
                    if folio == "":
                        print(RED + "⛔ Debe Ingresar El Folio De Reservación.\n" + BLACK)
                        continue

                    if(not re.match("^[0-9]*$",folio)):
                        print(RED + "⛔ El Folio De Reservación Debe Ser Un Numero.\n" + BLACK)
                        continue
                    folio = int(folio)
                    try:
                        valores = {"folio_reservacion":folio}
                        mi_cursor.execute("SELECT * FROM reservaciones WHERE folio_reservacion = :folio_reservacion", valores)
                        registros = mi_cursor.fetchall()

                        if not registros:
                            fail_load_box("Reservación No Encontrada","Buscando Reservación")
                            print(RED + "⛔ No se encontró Una Reservación Con Ese Folio.\n")
                            break
                        else:
                            load_box("Reservación Encontrada","Buscando Reservación")
                            mi_cursor.execute("SELECT DATE(fecha_reservacion) FROM reservaciones WHERE folio_reservacion = :folio_reservacion", valores)
                            fecha = mi_cursor.fetchone()

                            for fe in fecha:
                                fecha=fe

                            fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d").date()

                            fecha_actual = (datetime.date.today())
                            limite_fecha = (fecha - fecha_actual).days
                            if limite_fecha <= 2:
                                print(RED + "⛔ Se Necesitan 3 Días De Anticipación Para Cancelar Una Reservación. \n")
                                break

                            for folio, fecha,turno,cliente,sala,evento in registros:
                                print(BLACK + "Folio Reservación: "+ BLUE + f"{folio}")
                                print(BLACK + "Fecha Reservación: "+ BLUE + f"{fecha}")
                                print(BLACK + "Turno: "+ BLUE + f"{turno}")
                                print(BLACK + "🆔 Cliente: "+ BLUE + f"{cliente}")
                                print(BLACK + "🆔 Sala: "+ BLUE + f"{sala}")
                                print(BLACK + "Nombre Del Evento: "+ BLUE + f"{evento}")

                            while True:
                                decision = input(RED + "⚠️ ‼" + BLACK + " Esta Seguro Que desea Eliminar Esta Reservación "+ RED+"‼" + BLACK + " S/N:").upper().strip()

                                if decision not in "SN":
                                    print(RED + "⛔ Debes Seleccionar Una Opción Disponible Del Menú.\n")
                                    continue

                                if decision == "N":
                                    break

                                if decision == "":
                                    print(RED + "⛔ Debe Seleccionar Una Opción.\n")

                                if decision == "S":
                                    mi_cursor.execute("DELETE FROM reservaciones WHERE folio_reservacion = :folio_reservacion", valores)
                                    create_animation("Eliminando La Reservación.")
                                    conn.commit()
                                    print(GREEN + "✓ ‼ Se Ha eliminado La Reservación.‼")
                                    break
                    except:
                        print(RED + "☹ Ocurrio Un Error.\n")
                    break

    #Reportes
    if menu == "2":
        #Limpieza De Pantalla
        os.system('clear')
        while True:
            try:
                mi_cursor.execute("SELECT * FROM reservaciones ORDER BY folio_reservacion")
                registro = mi_cursor.fetchall()

                if not registro:
                    print(RED + "⛔ No Se Encontró Ninguna Reservación, Favor De Registrar Una.\n")
                    break
            except:
                print("☹ Ocurrió Un Error.\n")

            print(BLACK + """\n
             ---------------------Menú de opciones------------------
            |  1)🗒️ Reporte Reservaciones                            |
            |  2)📤Exportar Reporte Tabular A Excel                 |
            |  3)↩ Volver Al Menú Principal                         |
             -------------------------------------------------------""")
            sub_menu = input(BLACK + "\nIngresa Una Opción Del Menú: ").strip()

            if sub_menu not in "123":
                print(RED + "⛔ Ingrese Una Opción Disponible Del Menú.\n")
                os.system('clear')
                continue

            #Salir
            if sub_menu == "3":
                break

            #Reporte Reservaciones
            if sub_menu == "1":
                while True:
                    fecha_consulta = input(BLACK + "Fecha De Las Reservaciones A Consultar : ").strip()
                    if fecha_consulta == "":
                        print(RED + "⛔ Debe Ingresar una Fecha.\n")
                        continue

                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print(RED + "⛔ La Fecha Debe Tener El Formato(dd/mm/aaaa).\n" )
                        continue
                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print(RED + "⛔ La Fecha Ingresada No Es Una Fecha Válida, Intente De Nuevo.\n")
                        continue

                    try:
                            criterios = {"fecha":fecha_consulta}
                            mi_cursor.execute("SELECT folio_reservacion,fecha_reservacion,turno_reservacion,nombre_cliente,nombre_sala,nombre_evento FROM reservaciones WHERE DATE(fecha_reservacion) = :fecha;", criterios)
                            registros = mi_cursor.fetchall()

                            if not registros:
                                fail_load_box("Ningun Encontrado","Buscando Eventos")
                                print(RED + "⛔ No Se Encontró Ninguna Reservación, En Esa Fecha.\n")
                                break

                            load_box("Eventos Encontrados","Buscando Eventos")
                            print(BLACK + "FOLIO RESERVACIÓN\t\tFECHA RESERVACIÓN\t\tTURNO\t\tNOMBRE CLIENTE\t\tNOMBRE SALA\t\tNOMBRE DEL EVENTO")
                            for fol, fecha,turno,cliente,sala,evento in registros:
                                print(f"{fol}\t\t\t\t{fecha}\t\t\t{turno}\t{cliente}\t\t\t{sala}\t\t{evento}")
                            break
                    except:
                        print(RED + "☹ Ocurrió Un Error.\n")
                        break

            #Excel
            if sub_menu == "2":
                while True:
                    fecha_consulta = input(BLACK + "Ingrese La Fecha De Las Reservaciones A Consultar : ").strip()
                    if fecha_consulta == "":
                        print(RED + "⛔ Debe Ingresar Una Fecha.\n")
                        continue

                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print(RED + "⛔ La fecha Debe Tener El Formato(dd/mm/aaaa).\n")
                        continue
                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print(RED + "⛔ La Fecha Ingresada No Es Una Fecha Válida, Intente De Nuevo.\n")
                        continue

                    try:
                        criterios = {"fecha":fecha_consulta}
                        mi_cursor.execute("SELECT folio_reservacion,fecha_reservacion,turno_reservacion,nombre_cliente,nombre_sala,nombre_evento FROM reservaciones WHERE DATE(fecha_reservacion) = :fecha;", criterios)

                        registros = mi_cursor.fetchall()

                        if  not registros:
                            fail_load_box("Ningun Encontrado","Buscando Eventos")
                            print(RED + "⛔ No Se Encontró Ninguna Reservación, En Esa Fecha.\n")
                            break

                        registros_DataFrame = pd.DataFrame(registros)
                        registros_DataFrame.columns = ["FOLIO RESERVACIÓN", "FECHA RESERVACIÓN", "TURNO","NOMBRE CLIENTE","NOMBRE SALA","NOMBRE DEL EVENTO"]
                        registros_DataFrame_final = registros_DataFrame.set_index("FOLIO RESERVACIÓN")
                        registros_excel = registros_DataFrame_final.to_excel(f"{fecha_consulta}-Reporte Salas Coworking.xlsx")
                        load_box("Eventos Encontrados","Buscando Eventos")
                        create_animation("Exportando Reporte A Excel")
                        print(GREEN + "✓ Reporte Creado Con Éxito.\n")

                        break
                    except:
                        print(RED + "☹ Ocurrió Un Error.\n")
                        break

    #Registrar Una Sala
    if menu == "3":
        os.system('clear')
        while True:
            nombre_sala = input(BLACK + "Ingrese El Nombre De La Sala:  ").title().strip()
            if nombre_sala == "":
                print(RED + "⛔ Debe Ingresar Un Nombre A La Sala.\n")
                continue

            valores = {"nombre_sala":nombre_sala}

            mi_cursor.execute("SELECT nombre_sala FROM salas WHERE nombre_sala =:nombre_sala;", valores)
            registros = mi_cursor.fetchall()

            if registros:
                print(RED + "⛔ Ya Existe Una Sala Con Ese Nombre, Intente Otro Nombre.\n" )
                continue

            while True:
                cupo_sala = input(BLACK + "Ingrese El Cupo De La Sala:  ").strip()

                if cupo_sala == "":
                    print(RED + "⛔ Debe Ingresar El Cupo De La Sala.\n")
                    continue

                if(not re.match("^[0-9]{1,10}$",cupo_sala)):
                    print(RED + "⛔ Solamente Se Aceptan Números(Positivos) y No Mas De 10.\n")
                    continue

                if cupo_sala == "0":
                    print(RED + "⛔ El Cupo De La Sala Debe Ser Mayor A 0.\n")
                    continue

                cupo_sala=int(cupo_sala)
                mi_cursor.execute("INSERT INTO salas (nombre_sala,cupo_sala) VALUES (?,?);", [nombre_sala,cupo_sala])
                conn.commit()
                try:
                    mi_cursor.execute("SELECT MAX(id_sala),nombre_sala,cupo_sala FROM salas WHERE nombre_sala=(?);", [nombre_sala])
                    registros = mi_cursor.fetchall()

                    create_animation("Registrando Sala")

                    print(GREEN + "✓ Sala Creada Con Éxito.\n")
                    for idsala, nombre,cupo in registros:
                        print(BLACK + "🆔 Sala: "+ BLUE + f"{idsala}")
                        print(BLACK + "Nombre De La Sala: "+ BLUE + f"{nombre}")
                        print(BLACK + "Cupo: "+ BLUE + f"{cupo}")
                    break
                except:
                    print(RED + "☹ Ocurrió Un Error.\n")
                    break
            break

    #Registrar Un Cliente
    if menu == "4":
        os.system('clear')
        while True:
            nombre_cliente = input(BLACK + "Ingrese Su Nombre: ").title().strip()

            if nombre_cliente == "":#REVISAR ESPACIADO PARA EVITAR QUE EL USUARIO INGRESE NUMEROS Y PUEDA INGRESAR SOLO LETRAS
                print(RED + "⛔ El Nombre No Puede Quedar Vácio.\n")
                continue

            if (not re.match("^[a-zA-Z ñÑáÁéÉíÍóÓúÚ]*$", nombre_cliente)):#Expresion Regular para validar que el usuario solamente ingrese palabras y no numeros con espacios
                print(RED + "⛔ El Nombre solo pueden ser Letras, Intente de Nuevo.\n")
                continue
            else:
                mi_cursor.execute("INSERT INTO clientes (nombre_cliente) VALUES (?);", [nombre_cliente])
                conn.commit()
            try:
                mi_cursor.execute("SELECT MAX(id_cliente),nombre_cliente FROM clientes WHERE nombre_cliente=(?);", [nombre_cliente])
                registros = mi_cursor.fetchall()
                create_animation("Registrando Cliente")

                print(GREEN + "✓ Cliente Creado Con Éxito.\n")

                for idcliente, nombre in registros:
                    print(BLACK + "Su 🆔 De Cliente:" + BLUE +  f"{idcliente}")
                    print(BLACK + "Su Nombre De Cliente: " + BLUE + f"{nombre}")
            except:
                print(RED + "☹ Ocurrió Un Error.\n")
            break