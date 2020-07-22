import sys
from conexion import Conector

class DaoGrupo(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result = False
        try:
            sql = "Select id cod, descripcion des From grupo where descripcion like '%" + str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta de Grupo",e)
            self.conn.rollback()
        finally: self.cerrar()
        return result
    
    def ingresar(self, gru):
        correcto = True
        try:
            sql = "insert into grupo (descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql, (gru.descripcion))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar Grupo",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

    def modificar(self, gru):
        correcto = True
        try:
            sql = 'Update grupo set descripcion = %s where id = %s'
            self.conectar()
            self.conector.execute(sql, (gru.descripcion, gru.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar Grupo",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto
    
    def eliminar(self, gru):
        correcto = True
        try:
            sql = 'delete from grupo where id = %s'
            self.conectar()
            self.conector.execute(sql, (gru.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar grupo",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

"""con = DaoGrupo()
grupos = con.consultar("")
print(grupos) 
for gru in grupos: 
    print(gru[1])
"""