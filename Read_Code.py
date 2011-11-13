#!/usr/bin/python 
from decoder import *
from Baseclass import *
from pylab import *

f=open('test.asm')
asm_code=f.read()
print asm_code
asm_code_list=asm_code.strip()
#print asm_code_list
asm_code_list=asm_code_list.splitlines()
print asm_code_list

f.close()
opcode=[]

count=0
for n in asm_code_list:
	if (asm_code_list[count]==''):
		pass
	else:
		opcode+=decode(n)

	count=count+1
print opcode

for n in range(0,len(opcode)):
	UC.ROM[n]=opcode[n]

UC.PC=len(opcode)
print UC.ROM[0:20]
print UC.PC

