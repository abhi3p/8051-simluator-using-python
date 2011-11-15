#!/usr/bin/env python
from Baseclass import *

def setpsw(n):
	temp = UC.hex2dec(UC.bin2hex(UC.PSW[2:]))
	if n == 0 and UC.PSW[9] == '0':
		temp += 1
	elif n == 1 and UC.PSW[8] == '0':
		temp += 2
	elif n == 2 and UC.PSW[7] == '0':
		temp += 4
	elif n == 3 and UC.PSW[6] == '0':
		temp += 8
	elif n == 4 and UC.PSW[5] == '0':
		temp += 16
	elif n == 5 and UC.PSW[4] == '0':
		temp += 32
	elif n == 6 and UC.PSW[3] == '0':
		temp += 64
	elif n == 7 and UC.PSW[2] == '0':
		temp += 128
	UC.PSW = '0b'+UC.hex2bin(UC.dec2hex(int(temp)))

def resetpsw(n):
	temp = UC.hex2dec(UC.bin2hex(UC.PSW[2:]))
	if n == 0 and UC.PSW[9] == '1':
		temp -= 1
	elif n == 1 and UC.PSW[8] == '1':
		temp -= 2
	elif n == 2 and UC.PSW[7] == '1':
		temp -= 4
	elif n == 3 and UC.PSW[6] == '1':
		temp -= 8
	elif n == 4 and UC.PSW[5] == '1':
		temp -= 16
	elif n == 5 and UC.PSW[4] == '1':
		temp -= 32
	elif n == 6 and UC.PSW[3] == '1':
		temp -= 64
	elif n == 7 and UC.PSW[2] == '1':
		temp -= 128
	UC.PSW = '0b'+UC.hex2bin(UC.dec2hex(int(temp)))

def cpl2(value):
	temp1 = ''
	temp2 = UC.hex2bin(value)
	for n in range(0,len(temp2)):
		if temp2[n] == '0':
			temp1 += '1'
		else:
			temp1 += '0'
	temp1 = UC.incr(UC.bin2hex(temp1),1)
	return temp1
