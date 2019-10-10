'''0
Created on 06 Sep. 2019

@author: Iñigo Juan Pablo
'''
import struct
import ctypes
import os
import matplotlib
import matplotlib.pyplot as plt
from TLMY import *

# FUNCIÓN PARA GRAFICAR: ESTA FUNCIÓN GRAFICA EN LA FIGURA 1 SÓLO EL EJE X vs MUESTRAS. 
# EN LA FIGURA 2 GRAFICA EL EJE X vs Y (donde Y es el OBT). CABE ACLARAR QUE LA FIGURA 2
# GRAFICA MENOS CANTIDAD DE MUESTRAS PARA QUE NO SE CUELGUE CARGANDO TODOS LOS OBT.
def render(x,y):
	fig, ax = plt.subplots()
	ax.plot(y)
	ax.set(xlabel='Muestras', ylabel='Tensión Batería [V]', title='Tensión promedio de baterías')
	ax.grid()
	fig.set_size_inches(18.5,10)

	fig2, ax2 = plt.subplots()
	ax2.plot(x[0:500],y[0:500])
	ax2.set(xlabel='Tiempo', ylabel='Tensión Batería [V]', title='Tensión promedio de baterías')
	ax2.grid()
	fig2.set_size_inches(18.5,10)

	plt.xticks(rotation=45)
	plt.gcf().autofmt_xdate()
	plt.show() 	

def unpack_epoc(paquete):
	return(paquete.get_epoc())

if __name__ == '__main__':
	try:
		f = open("CGSS_20150603_091700_10020150603085920_SACD_HKTMST.bin","rb")
		tam_paquete = 4000
		# CHEQUEO TAMAÑO DEL ARCHIVO
		f.seek(0,2)		#VOY AL FINAL DEL ARCHIVO
		size = f.tell()
		if(size%tam_paquete):
			raise Exception("El archivo no es múltiplo de 4000 bytes")
		
		f.seek(0,0)		# VUELVO AL INICIO DEL ARCHIVO
		paquete = f.read(tam_paquete)
		list_TLMY = []
		list_bat = []
		list_epoc = []
		list_obt = []
		while(paquete):
			TLMY_paquet = TLMY(paquete)
			list_TLMY.append(TLMY_paquet)
			paquete = f.read(tam_paquete)

		# SE ORDENAN LOS OBJETOS POR LA EPOCA
		list_TLMY.sort(key=unpack_epoc)

		# POR CADA OBJETO OBTENGO VOLTAJE DE BATERIA, EPOCA Y OBT
		for ele in list_TLMY:
			list_bat.append(ele.get_vbat())
			list_obt.append(ele.get_obt())
			list_epoc.append(ele.get_epoc())

		render(list_obt,list_bat)

	except FileNotFoundError:
		print("Archivo inexistente")
	

