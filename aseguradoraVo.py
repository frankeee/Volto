# -*- coding: utf-8 -*-

class aseguradoVo:
    def __init__(self):
        
        self.poliza = 0
        self.asegurado = ""
        self.dni = 0
        self.direccion = ""
        self.ramo = ""
        self.estado = ""
        self.vigencia = ""
    
    def setPoliza(self,numero):
        self.poliza = numero
    def getPoliza(self):
        return self.poliza
    
    def setAsegurado(self,nombre):
        self.asegurado = nombre
    def getAsegurado(self):
        return self.asegurado
    
    def setDni(self,numero):
        self.dni = numero
    def getDni(self):
        return self.dni
    
    def setDireccion(self,calles):
        self.direccion = calles
    def getDireccion(self):
        return self.direccion
    
    def setRamo(self,rami):
        self.ramo = rami
    def getRamo(self):
        return self.ramo
    
    def setEstado(self,estadix):
        self.estado = estadix
    def getEstado(self):
        return self.estado
    
    def setVigencia(self,vigenci):
        self.vigencia = vigenci
    def getVigencia(self):
        return self.vigencia