#!/usr/bin/python 
from decoder import *
from Baseclass import *

def Read_Code(filename):
	f=open(filename)
	asm_code=f.read().strip().upper()
	print asm_code
	asm_code_list=asm_code
	#print asm_code_list
	asm_code_list=asm_code_list.splitlines()
	print asm_code_list
	
	f.close()
	opcodes=[]
	
#	count=0
#	for n in asm_code_list:
#		if (asm_code_list[count]==''):
#			pass
#		else:
#			opcode+=decode(n,len(opcode),count+1)
#		if UC.flag == 1:
#			break		
#		count=count+1
	opcodes = decoderinst(asm_code_list)
	print opcodes
	
	for n in range(0,len(opcodes)):
		UC.ROM[n]=opcodes[n]

	UC.PC=len(opcodes)
	print UC.ROM[0:20]
	print UC.PC
	
	if UC.flag == 0:
		UC.logcnt=UC.logcnt+1
		UC.log[UC.logcnt]="Program completed successfully"
		print UC.log[UC.logcnt]
