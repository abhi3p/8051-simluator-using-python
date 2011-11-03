#!/usr/bin/python
class BaseClass8051:
	"""The base class of 8051 which consists of all common data types and functions used for the simulator"""
	ROM=[hex(0)]*65536
	DPTR=[0]*65536
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
	DPTR_cntr=0
	
	def hex2bin(self,hexa):
		""" Function to convert from hex to binary"""
		bina=bin(int(hexa, 16))
		lenbin=len(bina)
		binappnd=['0']*(10-lenbin)
		bin0b=['0b']
		binb=[bina.split('b')[1]]
		bina=bin0b+binappnd+binb
		bina = ''.join(bina)
		return bina
		

	def bin2hex(self,bina):
		""" Function to convert binary number to hexadecimal"""
		hexa=self.dec2hex(int(bina,2))
		return hexa

	def hex2dec(self,hexa):
		"""return the integer value of a hexadecimal string s"""
		hexa = int(hexa, 16)
		return hexa
		 
	def dec2hex(self,deca):
		"""Return the hex value in 0xHH format"""
		hexa=hex(deca)
		if len(hexa) < 4:		
			hexb=hexa.split('x')
			hexa=hexb[0]+'x'+hexb[0]+hexb[1]
		return hexa

	def incr(self,incra,n):
		""" Increment any thing by anything"""
		deca=self.hex2dec(incra)
		deca=deca+n
		hexa=self.dec2hex(deca)
		return hexa
			 
	def decr(self,decra,n):
		""" Increment any thing by anything"""
		deca=self.hex2dec(incra)
		deca=deca-n
		hexa=self.dec2hex(deca)
		return hexa

UC = BaseClass8051()



