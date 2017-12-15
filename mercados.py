#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
proceso
estimacion de mercado 10000
porcentaje de division 10
pblico 1000
tasa de retencion

"""
from decimal import Decimal
import windows


#entrada de datos
print ("Estimación del público total")
total = input()
total = int(total)

idviajero  =3

print ("Estimación del porcentaje de division ")
divi = input()
divi = int(divi)

print ("Cual es la tasa de retención")
rete = input()
rete = int(rete)


# funcion 
class mercadoestimacion(object):
	def __init__(self,total,divi,rete):
		self.total = total
		self.divi = divi
		self.rete = rete

	def publicoReal(self):
		pubre = total / idviajero
		redondear = round (pubre, 0)
		print (redondear)

	def porcentajedeuso (object):
		pubRe = total / idviajero
		porcentPubRe = (pubRe * divi) / 100
		redondearpor = round (porcentPubRe, 0)
		print (redondearpor)

	def tasaretencion(object):
		pubRe = total / idviajero
		porcentPubRe = (pubRe * divi) / 100
		tasretenc = (porcentPubRe * rete) / 100
		red = round(tasretenc)
		print (red)


print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("Resultados" )
print ("___________________________________")
print ("\n")

result = mercadoestimacion(total,divi,rete)
print ("El publico real que usa tecnologia dentro de los viajeros es de : ")
result.publicoReal()

print ("De estos solo el",divi,"%"," usa apps para viajar lo cual representa el :")
result.porcentajedeuso()

print ("La tasa de retencion es de", rete, "% :")
result.tasaretencion()



		