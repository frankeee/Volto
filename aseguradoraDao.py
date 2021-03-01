# -*- coding: utf-8 -*-

from aseguradoraVo import aseguradoVo
from aseguradoraBD import bbdasegurador
class aseguradoraDao:
    
    def __init__(self):
        self.roma = 0
    
    miasegurado = aseguradoVo()
    baseControl = bbdasegurador()
    
    def registrarpersona(self,miasegurado):
        import mysql.connector

        cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='bbdaseguradora')
        
        cursor = cnx.cursor()
       
        pepo = miasegurado.getPoliza()
        roman = miasegurado.getDni()
        agregarAsegurado = "INSERT INTO aseguradora (poliza, asegurado, dni, direccion, ramo, estado, vigencia) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        agregasu = (pepo,str(miasegurado.getAsegurado()),roman,str(miasegurado.getDireccion()),str(miasegurado.getRamo()),str(miasegurado.getEstado()),miasegurado.getVigencia())
        
        
        cursor.execute(agregarAsegurado, agregasu)
        
        cnx.commit()
        
        
        
    def consultarPersonaPoliza(self,miasegurado,baseControl,numpoliza):
        
        baseControl.conectar()
        baseControl.fCursor()
        
        query = ("SELECT poliza, asegurado, dni, direccion, ramo ,estado ,vigencia FROM aseguradora "
         "WHERE poliza = %s") % (numpoliza) 
        
        baseControl.haceQuery(query)
        
        
            
        resultados = baseControl.fCursor().fetchall()
        resultadoprimerafila = resultados[0]
        miasegurado.setPoliza(resultadoprimerafila[0])
        miasegurado.setAsegurado(resultadoprimerafila[1])
        miasegurado.setDni(resultadoprimerafila[2])
        miasegurado.setDireccion(resultadoprimerafila[3])
        miasegurado.setRamo(resultadoprimerafila[4])  
        miasegurado.setEstado(resultadoprimerafila[5])
        miasegurado.setVigencia(resultadoprimerafila[6])
        
        
            
    
    def consultarPersonaNombreAsegurado(self,miasegurado,baseControl,nombreasegurado):
        
        baseControl.conectar()
        baseControl.fCursor()
        
        query = ("SELECT poliza, asegurado, dni, direccion, ramo, estado, vigencia FROM aseguradora "
         "WHERE asegurado = '%s' ") % (nombreasegurado)
        
        baseControl.haceQuery(query)
        
        resultados = baseControl.fCursor().fetchall()
        resultadoprimerafila = resultados[0]
        miasegurado.setPoliza(resultadoprimerafila[0])
        miasegurado.setAsegurado(resultadoprimerafila[1])
        miasegurado.setDni(resultadoprimerafila[2])
        miasegurado.setDireccion(resultadoprimerafila[3])
        miasegurado.setRamo(resultadoprimerafila[4])  
        miasegurado.setEstado(resultadoprimerafila[5])
        miasegurado.setVigencia(resultadoprimerafila[6])
        
    def editarPolizaAsegurado(self,baseControl,nombreasegurado,nuevapoliza):
        
        baseControl.conectar()
        baseControl.fCursor()
        
        query = ("UPDATE `aseguradora` SET `poliza` = '%s' WHERE `asegurado` = '%s'") % (nuevapoliza,nombreasegurado)
        
        baseControl.haceQuery(query)
        baseControl.commit()
        
    def editarEstadoAsegurado(self,baseControl,nombreasegurado,nuevoestado):
        
        baseControl.conectar()
        baseControl.fCursor()
        
        query = ("UPDATE `aseguradora` SET `estado` = '%s' WHERE `asegurado` = '%s'") % (nuevoestado,nombreasegurado)
        
        baseControl.haceQuery(query)
        baseControl.commit()
        
        
    
    def editarVigenciaAsegurado(self,baseControl,nombreasegurado,nuevavigencia):
        
        baseControl.conectar()
        baseControl.fCursor()
        
        query = ("UPDATE `aseguradora` SET `vigencia` = '%s' WHERE `asegurado` = '%s'") % (nuevavigencia,nombreasegurado)
    
        baseControl.haceQuery(query)       
        baseControl.commit()
        
    def eliminarCuenta(self,baseControl,nombreasegurado):
        baseControl.conectar()
        baseControl.fCursor()
        
        query = ("Delete from aseguradora where asegurado = '%s'") % (nombreasegurado)
         

        baseControl.haceQuery(query)       
        baseControl.commit()
                
        
        
        
        
        
        