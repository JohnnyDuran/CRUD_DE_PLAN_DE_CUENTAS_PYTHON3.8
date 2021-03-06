import sys
import pymysql


class Conector:
    def __init__(self, server='localhost', usuario='root', password='', basedato='db_tarea_crud'):
        self.__server = server
        self.__usuario = usuario
        self.__password = password
        self.__basedato = basedato
        self.__conn = ''
        self.__conector = ''
     
    def conectar(self):
        try:
            self.__conn = pymysql.connect(
                host=self.__server, user=self.__usuario, passwd=self.__password, db=self.__basedato)
            self.__conector = self.__conn.cursor()
        except (pymysql.err.OperationalError, pymysql.err.IntegrityError) as e:
            print("Error en la conexión", e)
            sys.exit(1)
    
    def cerrar(self):
        self.__conn.close()
        self.__conector.close()
    
    @property
    def conector(self):
        return self.__conector

    @property
    def conn(self):
        return self.__conn

con = Conector()
con.conectar()
print('ok')