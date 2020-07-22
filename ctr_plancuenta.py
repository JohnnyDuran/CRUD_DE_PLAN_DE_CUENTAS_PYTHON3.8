from dao_plancuenta import DaoPlancuenta
from mod_plancuenta import ModPlancuenta
class CtrPlancuenta:
    def __init__(self, plan=None):
        self.descripcion = plan

    def consulta(self, buscar):
        objDao = DaoPlancuenta()
        return objDao.consultar(buscar)

    def ingresar(self, plan):
        objDao = DaoPlancuenta()
        return objDao.ingresar(plan)

    def modificar(self, plan):
        objDao = DaoPlancuenta()
        return objDao.modificar(plan)

    def eliminar(self, plan):
        objDao = DaoPlancuenta()
        return objDao.eliminar(plan)


"""#Consulta que la informacion esta siendo llamada
plan = ModPlancuenta()
ctr = CtrPlancuenta()
cuentas=ctr.consulta("")
print(cuentas) 
for plan in cuentas: print(plan[0],plan[1],plan[2],plan[3],plan[4],plan[5])
"""

"""#Ingreso de datos y Revision de que se ingreso
plan = ModPlancuenta(0,"08",1,"Terreno","A","False")
ctr = CtrPlancuenta()
ctr.ingresar(plan)
cuentas=ctr.consulta("")
print(cuentas) 
for plan in cuentas: print(plan[0],plan[1],plan[2],plan[3],plan[4],plan[5])
"""

"""#Edicion de Datos y revision que se edito
plan = ModPlancuenta()
plan.id=9
plan.codigo= "08"
plan.grupo= 2
plan.descripcion='Edificio'
plan.naturaleza= "A"
plan.estado= True
ctr = CtrPlancuenta()
ctr.modificar(plan)
cuentas=ctr.consulta("")
print(cuentas) 
for plan in cuentas: print(plan[0],plan[1],plan[2],plan[3],plan[4],plan[5])
"""

"""#Eliminacion de datos y revision de eliminacion
plan = ModPlancuenta()
ctr = CtrPlancuenta()
plan.id=8
ctr.eliminar(plan)
cuentas=ctr.consulta("")
print(cuentas) 
for plan in cuentas: print(plan[0],plan[1],plan[2],plan[3],plan[4],plan[5])
"""