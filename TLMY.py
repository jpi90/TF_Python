import struct
import ctypes
from OBT import OBT

# Clase TLMY:	Esta clase tiene como atributos cada parámetro del paquete de telemetría.
#				Se inicializan  solo los que se van a utilizar, es decir, la tensión de batería y el OBT.

class TLMY(OBT):

	def __init__(self,paquete):	
		vbat_raw = struct.unpack(">h",paquete[2354:2356])
		seconds = struct.unpack(">L",paquete[8+92:8+92+4])
		self.__vBat_avg = vbat_raw[0]*0.01873128 - 38.682956			# tensión de batería promedio
		super(TLMY, self).__init__(seconds[0])							# OBT

	def get_vbat(self):
		return (self.__vBat_avg)




