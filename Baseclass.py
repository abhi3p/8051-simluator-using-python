#!/usr/bin/python
from pylab import *


class BaseClass8051:
	"""The base class of 8051 which consists of all common data types and functions used for the simulator"""
	ROM=[hex(0)]*4096
	RAM=[hex(0)]*256	
	A=hex(0)
	R0=hex(0)
	R1=hex(0)
	R2=hex(0)
	R3=hex(0)
	R4=hex(0)
	R5=hex(0)
	R6=hex(0)
	R7=hex(0)
	B=hex(0)
	SP=hex(7)
	PSW=bin(0)+'0000000'
	PC=0
	DPTR=0
	MEM=[hex(0)]*65536

	def hex2bin(self,hexa):
		""" Function to convert Hex to Binary. Input '0A' (or '0a') output '00001010' """
		hexa='0x'+hexa
		bina=bin(int(hexa, 16))
		lenbin=len(bina)
		binappnd=['0']*(10-lenbin)
		binb=[bina.split('b')[1]]
		bina=binappnd+binb
		bina = ''.join(bina)
		return bina
		

	def bin2hex(self,bina):
		""" Function to convert Binary to Hex Input '00001010' Output '0C' """
		bina='0b'+bina
		hexa=self.dec2hex(int(bina,2))
		hexa=hexa.upper()		
		return hexa

	def hex2dec(self,hexa):
		"""return the integer value of a hexadecimal Input '0C' (or '0c') Output 13 """
		hexa='0x'+hexa
		deca = int(hexa, 16)
		return deca
		 
	def dec2hex(self,deca):
		"""Function to convert Decimal to Hex Input 12 Ouput '0C' """
		hexa=hex(deca)
		if len(hexa) < 4:		
			hexb=hexa.split('x')
			hexa=hexb[0]+'x'+hexb[0]+hexb[1]
		hexa=hexa[2:]
		hexa=hexa.upper()
		return hexa

	def incr(self,incra,n):
		""" Increment a hexadecimal value by n (n is integer)"""
		deca=self.hex2dec(incra)
		deca=deca+n
		hexa=self.dec2hex(deca)
		return hexa
			 
	def decr(self,decra,n):
		""" Decrement a hexadecimal value by n (n is integer)"""
		deca=self.hex2dec(decra)
		deca=deca-n
		hexa=self.dec2hex(deca)
		return hexa

UC = BaseClass8051()



