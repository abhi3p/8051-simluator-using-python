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

def OP_02(pcntr):
	"""LJMP 3 byte istruction with 2 byte of address"""
	pcntr=pcntr+1
	addr1=UC.ROM[pcntr]
	pcntr=pcntr+1
	addr2=UC.ROM[pcntr]
	adr=adr1+adr2
	pcntr=UC.hex2dec(adr)
	return pcntr

def OP_20(pcntr):
	"""JB 3 byte istruction with 2 byte of address"""
	pcntr=pcntr+1
	addr1=UC.ROM[pcntr]
	pcntr=pcntr+1
	addr2=UC.ROM[pcntr]
	adr=adr1+adr2
	pcntr=UC.hex2dec(adr)
	return pcntr

def OP_30(pcntr):
	"""JNB 3 byte istruction with 2 byte of address"""
	pcntr=pcntr+1
	addr1=UC.ROM[pcntr]
	pcntr=pcntr+1
	addr2=UC.ROM[pcntr]
	adr=adr1+adr2
	pcntr=UC.hex2dec(adr)
	return pcntr

def OP_40(pcntr):
	"""JC 2 byte instruction with one byte of offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	pcntr=pcntr+UC.hex2dec(offset)
	return pcntr

def OP_50(pcntr):
	"""JNC 2 byte instruction with one byte of offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	pcntr=pcntr+UC.hex2dec(offset)
	return pcntr

def OP_60(pcntr):
	"""JZ 2 byte instruction with one byte of offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	pcntr=pcntr+UC.hex2dec(offset)
	return pcntr

def OP_70(pcntr):
	"""JNZ 2 byte instruction with one byte of offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	pcntr=pcntr+UC.hex2dec(offset)
	return pcntr

def OP_73(pcntr):
	"""JMP- unconditional 1 byte jump which takes address of A+DPTR"""
	pcntr=UC.hex2dec(A+DPTR)
	return pcntr

def OP_80(pcntr):
	"""SJMP 2 byte instruction with one byte of offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	pcntr=pcntr+UC.hex2dec(offset)
	return pcntr

def OP_B4(pcntr):
	"""CJNE 3 byte instruction with A and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if A!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_B5B6B7(pcntr):
	"""JMP"""
	pcntr=pcntr+1
	pcntr=pcntr+1
	return pcntr
#B8	3	CJNE	R0, #immed, offset

def OP_B8(pcntr):
	"""CJNE 3 byte instruction with R0 and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if R0!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_B9(pcntr):
	"""CJNE 3 byte instruction with R1 and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if R1!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_BA(pcntr):
	"""CJNE 3 byte instruction with R2 and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if R2!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_BB(pcntr):
	"""CJNE 3 byte instruction with R3 and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if R3!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_BC(pcntr):
	"""CJNE 3 byte instruction with R4 and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if R4!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_BD(pcntr):
	"""CJNE 3 byte instruction with R5 and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if R5!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_BE(pcntr):
	"""CJNE 3 byte instruction with R6 and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if R6!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_BF(pcntr):
	"""CJNE 3 byte instruction with R7 and data comparison and offset to PC"""
	pcntr=pcntr+1
	immed_data=UC.ROM[pcntr]
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	if R7!=immed_data:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_D5(pcntr):

def OP_D8(pcntr):
	"""DJNZ 2 byte instruction with comparison of decremented R0 with zero and offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	decr0=UC.hex2dec(R0)-1
	R0=UC.dec2hex(decr0)
	if UC.hex2dec(R0)!=0:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_D9(pcntr):
	"""DJNZ 2 byte instruction with comparison of decremented R1 with zero and offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	decr1=UC.hex2dec(R1)-1
	R1=UC.dec2hex(decr1)
	if UC.hex2dec(R1)!=0:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_DA(pcntr):
	"""DJNZ 2 byte instruction with comparison of decremented R2 with zero and offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	decr2=UC.hex2dec(R2)-1
	R2=UC.dec2hex(decr2)
	if UC.hex2dec(R2)!=0:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_DB(pcntr):
	"""DJNZ 2 byte instruction with comparison of decremented R3 with zero and offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	decr3=UC.hex2dec(R3)-1
	R3=UC.dec2hex(decr3)
	if UC.hex2dec(R3)!=0:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_DC(pcntr):
	"""DJNZ 2 byte instruction with comparison of decremented R4 with zero and offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	decr4=UC.hex2dec(R4)-1
	R4=UC.dec2hex(decr4)
	if UC.hex2dec(R4)!=0:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_DD(pcntr):
	"""DJNZ 2 byte instruction with comparison of decremented R5 with zero and offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	decr5=UC.hex2dec(R5)-1
	R5=UC.dec2hex(decr5)
	if UC.hex2dec(R5)!=0:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_DE(pcntr):
	"""DJNZ 2 byte instruction with comparison of decremented R6 with zero and offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	decr6=UC.hex2dec(R6)-1
	R6=UC.dec2hex(decr6)
	if UC.hex2dec(R6)!=0:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr

def OP_DF(pcntr):
	"""DJNZ 2 byte instruction with comparison of decremented R7 with zero and offset to PC"""
	pcntr=pcntr+1
	offset=UC.ROM[pcntr]
	decr7=UC.hex2dec(R7)-1
	R7=UC.dec2hex(decr7)
	if UC.hex2dec(R7)!=0:
            pcntr=pcntr+UC.hex2dec(offset)
	else:
	    pcntr=pcntr+1
	return pcntr




