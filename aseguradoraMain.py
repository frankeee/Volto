# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:10:19 2018

@author: Franco
"""

from tkinter import *
from tkinter import ttk
import os
from aseguradoraVo import aseguradoVo
from aseguradoraBD import bbdasegurador
#from aseguradoraDao import aseguradoraDao

#basero = bbdasegurador()
#hombredao = aseguradoraDao()
#hombrevo =aseguradoVo()


window = Tk()
import tkinter as tk

window.title("GG Seguros")

# gives weight to the cells in the grid
rows = 0
while rows < 50:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows, weight=1)
    rows += 1
    

 
# Defines and places the notebook widget
nb = ttk.Notebook(window)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Registrar')
 
# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Consultar')

page3 = ttk.Frame(nb)
nb.add(page3,text = "Editar")

try:
    def salir():
        basero.desconectar()
        return os._exit(0)
except SystemExit as er :
    print(er)
    
def aceptarRegi():
    hombrevo.setPoliza(cajapoliza.get())
    hombrevo.setAsegurado(cajaasegurado.get())
    hombrevo.setDni(cajadni.get())
    hombrevo.setDireccion(cajadireccion.get())
    hombrevo.setRamo(cajaramo.get())
    hombrevo.setEstado(cajaestado.get())
    hombrevo.setVigencia(cajavigencia.get())
    hombredao.registrarpersona(hombrevo)
    
    cajapoliza.delete(0,'end')
    cajaasegurado.delete(0,'end')
    cajadni.delete(0,'end')
    cajadireccion.delete(0,'end')
    cajaramo.delete(0,'end')
    cajaestado.delete(0,'end')
    cajavigencia.delete(0,'end')

def buscaPol():
    mensajeconsulta.delete(0.0,'end')
    hombredao.consultarPersonaPoliza(hombrevo,basero,cajaconsultapoliza.get())
    mensajeconsulta.insert(1.1,"Nombre:"+hombrevo.getAsegurado()+"\n")
    mensajeconsulta.insert(2.2,"Direccion:"+hombrevo.getDireccion()+"\n")
    mensajeconsulta.insert(3.3,"Dni:"+str(hombrevo.getDni())+"\n")
    mensajeconsulta.insert(5.5,"Poliza:"+str(hombrevo.getPoliza())+"\n")
    mensajeconsulta.insert(6.6,"Ramo:"+hombrevo.getRamo()+"\n")
    mensajeconsulta.insert(7.7,"Estado:"+hombrevo.getEstado()+"\n")
    juan = str(hombrevo.getVigencia())
    mensajeconsulta.insert(8.8,"Vigencia:"+juan[0]+juan[1]+"/"+juan[2]+juan[3])
    
    
    
def buscaAse():
    mensajeconsulta.delete(0.0,'end')
    hombredao.consultarPersonaNombreAsegurado(hombrevo,basero,cajaconsultaasegurado.get())
    mensajeconsulta.insert(1.1,"Nombre:"+hombrevo.getAsegurado()+"\n")
    mensajeconsulta.insert(2.2,"Direccion:"+hombrevo.getDireccion()+"\n")
    mensajeconsulta.insert(3.3,"Dni:"+str(hombrevo.getDni())+"\n")
    mensajeconsulta.insert(5.5,"Poliza:"+str(hombrevo.getPoliza())+"\n")
    mensajeconsulta.insert(6.6,"Ramo:"+hombrevo.getRamo()+"\n")
    mensajeconsulta.insert(7.7,"Estado:"+hombrevo.getEstado()+"\n")
    mensajeconsulta.insert(8.8,"Vigencia:"+hombrevo.getVigencia())
    
def editaPolizaAse():
    hombredao.editarPolizaAsegurado(basero,cajanomedit.get(),cajaeditpol.get())
    cajaeditpol.delete(0,'end')
def editaEstadoAse():
    hombredao.editarEstadoAsegurado(basero,cajanomedit.get(),cajaeditestado.get())    
    cajaeditestado.delete(0,'end')
def editaVigenciaAse():
    hombredao.editarVigenciaAsegurado(basero,cajanomedit.get(),cajaeditvigencia.get())    
    cajaeditvigencia.delete(0,'end')
    
def elimina():
    hombredao.eliminarCuenta(basero,cajaeliminar.get())
    cajaeliminar.delete(0,'end')
        
    
tk.Label(page1,text = "Poliza",borderwidth = 20).grid(row =10,column =10)
cajapoliza = tk.Entry(page1)
cajapoliza.grid(row = 10 , column = 11)

tk.Label(page1,text = "Asegurado",borderwidth = 20).grid(row = 11 , column = 10)
cajaasegurado = tk.Entry(page1)
cajaasegurado.grid(row = 11 , column = 11)

tk.Label(page1, text = "DNI",borderwidth = 20).grid(row = 12 , column = 10)
cajadni = tk.Entry(page1)
cajadni.grid(row = 12 , column = 11)

tk.Label(page1,text = "Direccion",borderwidth = 20).grid(row = 13,column = 10)
cajadireccion = tk.Entry(page1)
cajadireccion.grid(row = 13 , column = 11)

tk.Label(page1,text = "Ramo",borderwidth = 20).grid(row = 14 , column = 10)
cajaramo = tk.Entry(page1)
cajaramo.grid(row = 14, column = 11)

tk.Label(page1,text = "Estado",borderwidth = 20).grid(row = 15,column = 10)
cajaestado = tk.Entry(page1)
cajaestado.grid(row = 15 , column = 11)


tk.Label(page1,text = "Vigencia:",borderwidth = 20).grid(row = 17,column = 10)
cajavigencia = tk.Entry(page1)
cajavigencia.grid(row = 17,column = 11)

botonaceptarregi =tk.Button(page1,text = "Aceptar", borderwidth = 3,command = aceptarRegi).grid(row = 19,column =10)
botonsalirregi = tk.Button(page1,text = "Salir", borderwidth = 3,command = salir)
botonsalirregi.grid(row = 19,column = 12)

tk.Label(page2,text="Consultar por:",borderwidth = 50).grid(row = 10 , column = 10)

tk.Label(page2,text = "Numero de Poliza:", borderwidth = 20).grid(row = 12,column = 10)
cajaconsultapoliza = tk.Entry(page2,borderwidth = 7)
cajaconsultapoliza.grid(row = 12,column = 11 )
botonconsultapoliza = tk.Button(page2,text="Buscar",borderwidth = 7,command = buscaPol).grid(row = 12, column = 12)

tk.Label(page2, text= "Nombre de Asegurado").grid(row = 13,column = 10)
cajaconsultaasegurado = tk.Entry(page2,borderwidth = 7)
cajaconsultaasegurado.grid(row = 13,column = 11)
botonconsultaasegurado = tk.Button(page2,text = "Buscar",borderwidth = 7,command = buscaAse).grid(row = 13,column = 12)

mensajeconsulta = tk.Text(page2)
mensajeconsulta.grid(row= 14,column =10)

botonsalirconsul = tk.Button(page2,text = "Salir", command = salir).grid(row = 15,column = 10 ) 

tk.Label(page3 , text = "Nombre de cuenta a editar:",borderwidth = 20).grid(row = 10,column = 10)
cajanomedit = tk.Entry(page3)
cajanomedit.grid(row = 10,column = 11)

tk.Label(page3,text="Editar Poliza:",borderwidth = 20).grid(row = 11,column = 10 )
cajaeditpol = tk.Entry(page3)
cajaeditpol.grid(row = 11 , column = 11)
btnedipol = tk.Button(page3,text="Editar",command = editaPolizaAse).grid(row=11,column = 12)

tk.Label(page3,text = "Editar Estado:",borderwidth = 20).grid(row = 12,column = 10)
cajaeditestado = tk.Entry(page3)
cajaeditestado.grid(row = 12,column = 11)
btneditestado = tk.Button(page3,text="Editar",command = editaEstadoAse).grid(row = 12,column = 12)

tk.Label(page3,text = "Editar Vigencia:",borderwidth = 20).grid(row = 13,column = 10)
cajaeditvigencia = tk.Entry(page3)
cajaeditvigencia.grid(row = 13,column = 11)
btneditvigencia = tk.Button(page3,text="Editar",command = editaVigenciaAse).grid(row = 13,column = 12)

tk.Label(page3,text = "Nombre de cuenta a Eliminar:",borderwidth = 20).grid(row =15,column = 10)
cajaeliminar = tk.Entry(page3)
cajaeliminar.grid(row = 15 , column = 11)
btnelim = tk.Button(page3,text="Eliminar",command = elimina).grid(row = 15,column =12)

window.mainloop()



