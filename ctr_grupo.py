from dao_grupo import DaoGrupo
from mod_grupo import ModGrupo
class CtrGrupo:
    def __init__(self, gru=None):
        self.descripcion = gru

    def consulta(self, buscar):
        objDao = DaoGrupo()
        return objDao.consultar(buscar)

    def ingresar(self, gru):
        objDao = DaoGrupo()
        return objDao.ingresar(gru)

    def modificar(self, gru):
        objDao = DaoGrupo()
        return objDao.modificar(gru)

    def eliminar(self, gru):
        objDao = DaoGrupo()
        return objDao.eliminar(gru)


"""#Consulta que la informacion esta siendo llamada
gru = ModGrupo()
ctr = CtrGrupo()
grupos=ctr.consulta("")
print(grupos) 
for gru in grupos: print(gru[0],gru[1])
"""

"""#Ingreso de datos y Revision de que se ingreso
gru = ModGrupo(0,"Otros")
ctr = CtrGrupo()
ctr.ingresar(gru)
grupos=ctr.consulta("")
print(grupos) 
for gru in grupos: print(gru[0],gru[1])
"""

"""#Edicion de Datos y revision que se edito
gru = ModGrupo()
gru.id=6
gru.descripcion='Editado'
ctr = CtrGrupo()
ctr.modificar(gru)
grupos=ctr.consulta("")
print(grupos) 
for gru in grupos: print(gru[0],gru[1])
"""

"""#Eliminacion de datos y revision de eliminacion
gru = ModGrupo()
ctr = CtrGrupo()
gru.id=6
ctr.eliminar(gru)
grupos=ctr.consulta("")
print(grupos) 
for gru in grupos: print(gru[0],gru[1])
"""

