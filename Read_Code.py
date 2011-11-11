#!/usr/bin/python 
from decoder import *
from Baseclass import *
from pylab import *

def Read_Code():
	f=open('test.asm')
	asm_code=f.read()
	asm_code_list=asm_code.splitlines()
	print asm_code
	f.close()

	opcode=[]

	for n in asm_code_list:
		opcode+=decode(n)

	print opcode

	for n in range(0,len(opcode)):
		UC.ROM[n]=opcode[n]

	UC.PC=len(opcode)
	print UC.ROM[0:20]
	print UC.PC

### Check
