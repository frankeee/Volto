# -*- coding: utf-8 -*-


import mysql.connector



class bbdasegurador:
    def __init__(self):
        
        
       
        self.cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='bbdaseguradora')
        
        self.cursor = self.cnx.cursor()

    def conectar(self):
        return self.cnx
    def fCursor(self):
        return self.cursor
    def haceQuery(self,query):
        self.cursor.execute(query)
    def desconectar(self):
        self.cnx.close()
        self.cursor.close()
    def commit(self):
        self.cnx.commit()
        
    
