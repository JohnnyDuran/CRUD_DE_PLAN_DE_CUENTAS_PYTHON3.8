
import os
os.system('cls')
def menu(opciones, titulo):
    print('*'*40)
    print('--',format(titulo),'--')
    print('*'*40)
    for op in range(0,len(opciones)):
        print("{}) {}".format(op, opciones[op]))
    opc = input('Elija una Opción [0....{}]: '.format(len(opciones)-1))
    return opc

"""men = menu(('Grupos de Cuentas','Plan de Cuentas','Salir'), 'CRUD de Plan de Cuenta')"""