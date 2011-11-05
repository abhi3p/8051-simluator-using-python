#!/usr/bin/env python
from Baseclass import *

#Hex
#Code  Bytes   Mnemonic Operands
#01	2	AJMP	addr11
#02	3	LJMP	addr16
#20	3	JB	bit, offset
#21	2	AJMP	addr11
#30	3	JNB	bit, offset
#40	2	JC	offset
#41	2	AJMP	addr11
#50	2	JNC	offset
#60	2	JZ	offset
#61	2	AJMP	addr11
#70	2	JNZ	offset
#73	1	JMP	@A+DPTR
#80	2	SJMP	offset
#81	2	AJMP	addr11
#A1	2	AJMP	addr11
#B4	3	CJNE	A, #immed, offset
#B5	3	CJNE	A, direct, offset
#B6	3	CJNE	@R0, #immed, offset
#B7	3	CJNE	@R1, #immed, offset
#B8	3	CJNE	R0, #immed, offset
#B9	3	CJNE	R1, #immed, offset
#BA	3	CJNE	R2, #immed, offset
#BB	3	CJNE	R3, #immed, offset
#BC	3	CJNE	R4, #immed, offset
#BD	3	CJNE	R5, #immed, offset
#BE	3	CJNE	R6, #immed, offset
#BF	3	CJNE	R7, #immed, offset
#C1	2	AJMP	addr11
#D5	3	DJNZ	direct, offset
#D8	2	DJNZ	R0, offset
#D9	2	DJNZ	R1, offset
#DA	2	DJNZ	R2, offset
#DB	2	DJNZ	R3, offset
#DC	2	DJNZ	R4, offset
#DD	2	DJNZ	R5, offset
#DE	2	DJNZ	R6, offset
#DF	2	DJNZ	R7, offset
#E1	2	AJMP	addr11

ROM = ['01','10','02','10','11','20','10','11','21','10','30','10','11','40','10','41','10','50','10','60','10','61','10', '70','10','73','80','10','81','10','A1','10','B4','12','13','B5','12','13','B6','12','13','B7','12','13','B8','12','13',
'B9','12','13','BA','12','13','BB','12','13','BC','12','13','BD','12','13','BE','12','13','BF','12','13',
'C1','10','D5','12','13','D8','10','D9','10','DA','10','DB','10','DC','10','DD','10','DE','10','DF','10','E1','10']

#PMD = [36,32,36,40,36,64,40,41,42,43,44,45,46,47]

def OP_02(pcntr):
	"""LJMP 3 byte istruction with 2 byte of address"""
	pcntr=pcntr+1
	addr1=UC.ROM[pcntr]
	pcntr=pcntr+1
	addr2=UC.ROM[pcntr]
	UC.hex2dec(UC.ROM[pcntr])
	pcntr=pcntr+1
	return pcntr
def OP_(pcntr):
	"""JMP"""
	pcntr=pcntr+1
	addr1=UC.ROM[pcntr]
	pcntr=pcntr+1
	addr2=UC.ROM[pcntr]
	UC.hex2dec(UC.ROM[pcntr])
	pcntr=pcntr+1
	return pcntr
def OP_(pcntr):
	"""JMP"""
	pcntr=pcntr+1
	addr1=UC.ROM[pcntr]
	pcntr=pcntr+1
	addr2=UC.ROM[pcntr]
	UC.hex2dec(UC.ROM[pcntr])
	pcntr=pcntr+1
	return pcntr
def OP_(pcntr):
	"""JMP"""
	pcntr=pcntr+1
	addr1=UC.ROM[pcntr]
	pcntr=pcntr+1
	addr2=UC.ROM[pcntr]
	UC.hex2dec(UC.ROM[pcntr])
	pcntr=pcntr+1
	return pcntr
def OP_(pcntr):
	"""JMP"""
	pcntr=pcntr+1
	addr1=UC.ROM[pcntr]
	pcntr=pcntr+1
	addr2=UC.ROM[pcntr]
	UC.hex2dec(UC.ROM[pcntr])
	pcntr=pcntr+1
	return pcntr



















while BaseObj8051.PC_cntr < len(ROM):
	if ROM[UC.PC] == '02':
		adr1 = int(BaseObj8051.A,16)
		opr2 = BaseObj8051.hex2dec(PM[BaseObj8051.PC_cntr+1])
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		print BaseObj8051.A
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 2



#code = 'LOOP: MOV A, #10H'
#if code!=code.split(':')[0]:
#   label=code.split(':')[0]


