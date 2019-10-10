# Clase OBT:	La misma se inicializa ingresando los segundos desde 06/01/1980 00:00:00
# 				y calcula el on board time.
#				Se implementa método para leer el OBT.

class OBT(object):

	def __init__(self,seconds):						# segundos desde 06/01/1980 00:00:00 (1980 año biciesto)
		seconds_per_day = 86400
		seconds_per_hour = 3600
		days = (seconds + 6*seconds_per_day) // seconds_per_day			# días desde 01/01/1980
		rem_sec = (seconds + 6*seconds_per_day) % seconds_per_day		# segundos restantes
		years = 1980
		month = 1
		# calculo del año
		while(days>=365):
			if(self.__esBi(years)):						# año biciesto
				if(days<=366):
					break
				else:
					days = days - 366
			else:										# año no biciesto
				if(days<=365):
					break
				else:
					days = days - 365
			years = years +1
		
		month_days = 0
		# calculo del mes
		while(days>=28):
			if (month==1):
				month_days = 31
			elif (month==2):
				if(self.__esBi(years)):						# año biciesto
					month_days = 29
				else:
					month_days = 28
			elif (month==3):
				month_days = 31
			elif (month==4):
				month_days = 30
			elif (month==5):
				month_days = 31
			elif (month==6):
				month_days = 30
			elif (month==7):
				month_days = 31
			elif (month==8):
				month_days = 31
			elif (month==9):
				month_days = 30
			elif (month==10):
				month_days = 31
			elif (month==11):
				month_days = 30
			elif (month==12):
				month_days = 31
			else:
				raise Exception("Error en cálculo del mes")
			
			if(days<=month_days):
				break
			else:
				days = days - month_days
				month = month + 1
			
		self.__year = years
		self.__month = month
		self.__day = days
		self.__hour = rem_sec//seconds_per_hour		
		self.__minute = (rem_sec%seconds_per_hour)//60	
		self.__second = (rem_sec%seconds_per_hour)%60
		self.__epoc = seconds

	def get_obt(self):
		return(str("{:02d}".format(self.__day))+ "/" + str("{:02d}".format(self.__month)) + "/" + str("{:02d}".format(self.__year)) + " " + str("{:02d}".format(self.__hour)) + ":" + str("{:02d}".format(self.__minute)) + ":" + str("{:02d}".format(self.__second)))

	def get_epoc(self):
		return(self.__epoc)

	def __esBi(self,years):
		if (years % 4):
			return 0	
		else:
			if (years % 100):
				return 1
			else:
				if (years % 400):
					return 0
				else:
					return 1
