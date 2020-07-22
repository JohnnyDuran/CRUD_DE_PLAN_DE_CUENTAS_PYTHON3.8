from ctr_grupo import CtrGrupo
from mod_grupo import ModGrupo
from ctr_plancuenta import CtrPlancuenta
from mod_plancuenta import ModPlancuenta
from funciones import menu
import os
import time

#GRUPO
#Inserción de Grupo
ctr = CtrGrupo()
def insertar_grupo(rango):
    for i in range(int(rango)):
        descripcion = input('Ingrese El Grupo (Nombre Del Grupo): ')
        cli = ModGrupo(des=descripcion)
        if ctr.ingresar(cli):
            print('\n','Registro Grabado Correctamente','\n')
            time.sleep(2)
        else:
            print('\n','Error Al Grabar Registro','\n')
            time.sleep(2)

#Modificación de Grupo
def modificar_grupo():
    id = input('Ingrese El ID Del Grupo A Modificar: ')
    descripcion = input('Ingrese El Grupo (Nombre Del Grupo): ')
    cli = ModGrupo(cod=id,des=descripcion)
    if ctr.modificar(cli):
        print('\n','Registro Modificado Correctamente','\n')
        time.sleep(2)
    else:
        print('\n','Error Al Modificar Registro','\n')
        time.sleep(2)

#Eliminación de Grupo
def eliminar_grupo():
    id = input('Ingrese el ID Del Grupo a Eliminar: ')
    cli = ModGrupo(cod=id)
    if ctr.eliminar(cli):
        print('\n','Registro Eliminado Correctamente','\n')
        time.sleep(2)
    else:
        print('\n','Error Al Eliminar Registro','\n')
        time.sleep(2)

#Consulta de Grupo
def consultar_grupo():
    buscar = input('Ingrese Grupo A Consultar: ')
    cli = ctr.consulta(buscar)
    print('   -ID-    Descripción')
    for registro in cli:
        print('{:6}      {}'.format(registro[0], registro[1]))

#PLAN DE CUENTAS
#Inserción Del Plan De Cuentas
ctr1 = CtrPlancuenta()
def insertar_cuenta(rango):
    for i in range(int(rango)):
        codigo = input('Ingrese El Código Para La Cuenta: ')
        grupo= input('Ingrese El Grupo: ')
        descripcion = input('Ingrese La Descripcion De La Cuenta: ')
        naturaleza= input('Ingrese su Naturaleza (D= Deudora, A= Acredora): ')
        estado= input('Ingrese el Estado (1= True, 0=False): ')
        cli1 = ModPlancuenta(codg= codigo, grup= grupo, des=descripcion, nat=naturaleza, est=estado)
        if ctr1.ingresar(cli1):
            print('\n','Registro grabado correctamente','\n')
            time.sleep(2)
        else:
            print('\n','Error al grabar el Registro','\n')
            time.sleep(2)

#Modificacion Del Plan De Cuentas
def modificar_cuenta():
    id = input('Ingrese El ID De La Cuenta: ')
    codigo = input('Ingrese El Código De La Cuenta: ')
    grupo= input('Ingrese El Grupo: ')
    descripcion = input('Ingrese La Descripcion De La Cuenta: ')
    naturaleza= input('Ingrese su Naturaleza (D= Deudora, A= Acredora): ')
    estado= input('Ingrese el Estado (1= True, 0=False): ')
    cli1 = ModPlancuenta(cod=id,codg= codigo, grup= grupo, des=descripcion, nat=naturaleza, est=estado)
    if ctr1.modificar(cli1):
        print('\n','Registro modificado correctamente','\n')
        time.sleep(2)
    else:
        print('\n','Error al modificar el Registro','\n')
        time.sleep(2)

#Eliminacion Del Plan De Cuentas
def eliminar_cuenta():
    id = input('Ingrese el ID De La Cuenta: ')
    cli1 = ModPlancuenta(cod=id)
    if ctr1.eliminar(cli1):
        print('\n','Registro eliminado correctamente','\n')
        time.sleep(2)
    else:
        print('Error al eliminar el Registro')
        time.sleep(2)

#Consulta Del Plan De Cuentas
def consultar_cuenta():
    buscar = input('Ingrese La Descripcion Del Grupo A Buscar: ')
    cli1 = ctr1.consulta(buscar)
    print('    ID   Codigo   Grupo   Descripción       Naturaleza   Estado')
    for registro in cli1:
        print('{:6}\t   {:3}\t{:5}\t   {:6}\t\t{:1}\t{:4}'.format(
            registro[0], registro[1],registro[2],registro[3],registro[4],registro[5]))

def ejecutar_Plancuenta():
    opc = ''
    while opc != '2':
        opc = str(menu(
            ['Grupos de Cuentas','Plan de Cuentas','Salir'],
            'CRUD de Plan de Cuenta'))
        if opc == '0':
            os.system('cls')
            opc = ''
            while opc != '4':
                os.system('cls')
                opc = str(menu(
                ['Ingresar', 'Consultar', 'Modificar', 'Eliminar', 'Retornar al Menu Principal'],
                'Menu Grupo de Cuentas'))
                if opc == '0':
                    try:
                        os.system('cls')
                        print('\n<<<Ingresar datos>>> ')
                        valor = input('Ingrese cantidad de datos a Ingresar (1.....): ')
                        insertar_grupo(valor)
                    except:
                        print('\n','Ingrese Datos Validos Como Se Indica','\n')
                        input('Presione una tecla para continuar.....')
                elif opc == '1':
                    try:
                        os.system('cls')
                        print('\n<<<Consultar datos>>>')
                        consultar_grupo()
                        input('Presione una tecla para continuar.....')
                    except:
                        print('\n','Problemas al Consultar Datos','\n')
                        time.sleep(3)
                elif opc == '2':
                    try:
                        os.system('cls')
                        consultar_grupo()
                        print('\n<<<Modificar datos>>>')
                        modificar_grupo()
                    except:
                        print('\n','Ingrese Datos Validos Como Se Indica','\n')
                        input('Presione una tecla para continuar.....')
                elif opc == '3':
                    try:
                        os.system('cls')
                        consultar_grupo()
                        print('\n<<<Eliminar datos>>>')
                        eliminar_grupo()
                    except:
                        print('\n','Problemas con la Eliminación','\n')
                        input('Presione una tecla para continuar.....')
                elif opc == '4':
                    os.system('cls')
                elif opc != '4':
                    os.system('cls')
                    print('\n','Seleccione una opción correcta','\n')    
        elif opc == '1':
            os.system('cls')
            opc = ''
            while opc != '4':
                os.system('cls')
                opc = str(menu(
                ['Ingresar', 'Consultar', 'Modificar', 'Eliminar', 'Retornar al Menu Principal'],
                'Menu Grupo de Plan de Cuentas'))
                if opc == '0':
                    try:
                        os.system('cls')
                        consultar_cuenta()
                        print('\n<<<Ingresar datos>>> ')
                        valor = input('Ingrese cantidad de datos a Ingresar (1.....): ')
                        insertar_cuenta(valor)
                    except:
                        print('\n','Ingrese Datos Validos Como Se Indica','\n')
                        input('Presione una tecla para continuar.....')
                elif opc == '1':
                    try:
                        os.system('cls')
                        print('\n<<<Consultar datos>>>')
                        consultar_cuenta()
                        input('Presione una tecla para continuar.....')
                    except:
                        print('\n','Problemas al Consultar Datos','\n')
                        time.sleep(3)
                elif opc == '2':
                    try:
                        os.system('cls')
                        consultar_cuenta()
                        print('\n<<<Modificar datos>>>')
                        modificar_cuenta()
                    except:
                        print('\n','Ingrese Datos Validos Como Se Indica','\n')
                        input('Presione una tecla para continuar.....')
                elif opc == '3':
                    try:
                        os.system('cls')
                        consultar_cuenta()
                        print('\n<<<Eliminar datos>>>')
                        eliminar_cuenta()
                    except:
                        print('\n','Problemas con la Eliminación','\n')
                        time.sleep(3)
                elif opc == '4':
                    os.system('cls')
                elif opc != '4':
                    os.system('cls')
                    print('\n','Seleccione una opción correcta','\n')  
        elif opc == '2':
            os.system('cls')
            print('<<<Gracias por usar el Sistema>>>')
        elif opc != '2':
            os.system('cls')
            print("\n","Seleccione una opción correcta","\n")
            
ejecutar_Plancuenta()