#!/usr/bin/env python
from Baseclass import *

PM = ['24','20','24','28','24','40','28','29','2A','2B','2C','2D','2E','2F']
#PMD = [36,32,36,40,36,64,40,41,42,43,44,45,46,47]

def ADD(opr1,opr2):
	return opr1+opr2

while BaseObj8051.PC_cntr < len(PM):
	if PM[BaseObj8051.PC_cntr] == '24':
		opr1 = int(BaseObj8051.A,16)
		opr2 = BaseObj8051.hex2dec(PM[BaseObj8051.PC_cntr+1])
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		print BaseObj8051.A
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 2

	if PM[BaseObj8051.PC_cntr] == '28':
		opr1 = int(BaseObj8051.A,16)
		opr2 = int(BaseObj8051.R0,16)
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 1

	if PM[BaseObj8051.PC_cntr] == '29':
		opr1 = int(BaseObj8051.A,16)
		opr2 = int(BaseObj8051.R1,16)
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 1

	if PM[BaseObj8051.PC_cntr] == '2A':
		opr1 = int(BaseObj8051.A,16)
		opr2 = int(BaseObj8051.R2,16)
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 1

	if PM[BaseObj8051.PC_cntr] == '2B':
		opr1 = int(BaseObj8051.A,16)
		opr2 = int(BaseObj8051.R3,16)
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 1

	if PM[BaseObj8051.PC_cntr] == '2C':
		opr1 = int(BaseObj8051.A,16)
		opr2 = int(BaseObj8051.R4,16)
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 1

	if PM[BaseObj8051.PC_cntr] == '2D':
		opr1 = int(BaseObj8051.A,16)
		opr2 = int(BaseObj8051.R5,16)
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 1

	if PM[BaseObj8051.PC_cntr] == '2E':
		opr1 = int(BaseObj8051.A,16)
		opr2 = int(BaseObj8051.R6,16)
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 1

	if PM[BaseObj8051.PC_cntr] == '2F':
		opr1 = int(BaseObj8051.A,16)
		opr2 = int(BaseObj8051.R7,16)
		ans = ADD(opr1,opr2)
		BaseObj8051.A = hex(ans)
		BaseObj8051.PC_cntr = BaseObj8051.PC_cntr + 1
		print BaseObj8051.A
		print BaseObj8051.PC_cntr
