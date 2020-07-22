import sys
from conexion import Conector

class DaoPlancuenta(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result = False
        try:
            sql = "Select id cod, codigo codg, grupo grup, descripcion des, naturaleza nat, estado est From plancuenta where descripcion like '%" + str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta de Plan de Cuenta",e)
            self.conn.rollback()
        finally: self.cerrar()
        return result
    
    def ingresar(self, plan):
        correcto = True
        try:
            sql = "insert into plancuenta (codigo, grupo, descripcion, naturaleza, estado) values (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql, (plan.codigo, plan.grupo, plan.descripcion, plan.naturaleza, plan.estado))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar Plan de Cuenta",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

    def modificar(self, plan):
        correcto = True
        try:
            sql = 'Update plancuenta set codigo= %s, grupo= %s, descripcion= %s, naturaleza= %s, estado= %s where id = %s'
            self.conectar()
            self.conector.execute(sql, (plan.codigo, plan.grupo, plan.descripcion, plan.naturaleza, plan.estado, plan.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar Plan de Cuentas",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto 
    
    def eliminar(self, plan):
        correcto = True
        try:
            sql = 'delete from plancuenta where id = %s'
            self.conectar()
            self.conector.execute(sql, (plan.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar Plan de Cuentas",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

"""con = DaoPlancuenta()
cuentas = con.consultar("")
print(cuentas) 
for plan in cuentas: 
    print(plan[3])
"""