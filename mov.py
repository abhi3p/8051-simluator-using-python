#!/usr/bin/python
from Baseclass import *
from pylab import *

def OP_74(pcntr):
	""" MOV A, #data"""
	pcntr=pcntr+1
	UC.A=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_75(pcntr):
	""" MOV dataaddr,#data"""
	pcntr=pcntr+1
	temp=UC.hex2dec(pcntr)
	pcntr=pcntr+1
	UC.RAM[temp]=UC.ROM[pcntr]
	pcntr=pcntr+1
	return pcntr

def OP_76(pcntr):
	""" MOV @R0, #data"""
	temp=UC.hex2dec(UC.R0)
	pcntr=pcntr+1
	UC.RAM[temp]=UC.ROM[pcntr]
	pcntr=pcntr+1
	return pcntr	
	
def OP_77(pcntr):
	""" MOV @R1,#data"""
	temp=UC.hex2dec(UC.R1)
	pcntr=pcntr+1
	UC.RAM[temp]=UC.ROM[pcntr]
	pcntr=pcntr+1
	return pcntr

def OP_78(pcntr):
	""" MOV R0, #data"""
	pcntr=pcntr+1
	UC.R0=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_79(pcntr):
	""" MOV R1, #data"""
	pcntr=pcntr+1
	UC.R1=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_7A(pcntr):
	""" MOV R2, #data"""
	pcntr=pcntr+1
	UC.R3=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_7B(pcntr):
	""" MOV R3, #data"""
	pcntr=pcntr+1
	UC.R3=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_7C(pcntr):
	""" MOV R4, #data"""
	pcntr=pcntr+1
	UC.R4=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_7D(pcntr):
	""" MOV R5, #data"""
	pcntr=pcntr+1
	UC.R5=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_7E(pcntr):
	""" MOV R6, #data"""
	pcntr=pcntr+1
	UC.R6=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_7F(pcntr):
	""" MOV R7, #data"""
	pcntr=pcntr+1
	UC.R7=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_83(pcntr):
	""" MOVC A,@A+PC"""
	tempA=UC.hex2dec(UC.A)
	tempPC=UC.hex2dec(UC.PC)
	UC.A=UC.RAM[tempA+tempPC]
	pcntr=pcntr+1
	return pcntr

def OP_85(pcntr):
	""" MOV dataaddr, dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.PC[pcntr])
	pcntr=pcntr+1
	temp2=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp1]=UC.RAM[temp2]
	pcntr=pcntr+1
	return(pcntr)

def OP_86(pcntr):
	""" MOV dataaddr, @R0"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.PC[pcntr])
	temp2=UC.hex2dec(UC.R0)
	UC.RAM[temp1]=UC.RAM[temp2]
	pcntr=pcntr+1
	return(pcntr)
	

def OP_87(pcntr):
	""" MOV dataaddr, @R1"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.PC[pcntr])
	temp2=UC.hex2dec(UC.R1)
	UC.RAM[temp1]=UC.RAM[temp2]
	pcntr=pcntr+1
	return(pcntr)

def OP_88(pcntr):
	""" MOV dataaddr, R0"""
	pcntr=pcntr+1
	temp=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp]=UC.R0
	pcntr=pcntr+1
	return pcntr

def OP_89(pcntr):
	""" MOV dataaddr, R1"""
	pcntr=pcntr+1
	temp=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp]=UC.R1
	pcntr=pcntr+1
	return pcntr

def OP_8A(pcntr):
	""" MOV dataaddr, R2"""
	pcntr=pcntr+1
	temp=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp]=UC.R2
	pcntr=pcntr+1
	return pcntr

def OP_8B(pcntr):
	""" MOV dataaddr, R3"""
	pcntr=pcntr+1
	temp=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp]=UC.R3
	pcntr=pcntr+1
	return pcntr

def OP_8C(pcntr):
	""" MOV dataaddr, R4"""
	pcntr=pcntr+1
	temp=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp]=UC.R4
	pcntr=pcntr+1
	return pcntr

def OP_8D(pcntr):
	""" MOV dataaddr, R5"""
	pcntr=pcntr+1
	temp=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp]=UC.R5
	pcntr=pcntr+1
	return pcntr

def OP_8E(pcntr):
	""" MOV dataaddr, R6"""
	pcntr=pcntr+1
	temp=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp]=UC.R6
	pcntr=pcntr+1
	return pcntr

def OP_8F(pcntr):
	""" MOV dataaddr, R7"""
	pcntr=pcntr+1
	temp=UC.hex2dec(UC.PC[pcntr])
	UC.RAM[temp]=UC.R7
	pcntr=pcntr+1
	return pcntr

def OP_90(pcntr):
	""" MOV DPTR, #data"""
	pcntr=pcntr+1
	temp1=UC.PC[pcntr]
	pcntr=pcntr+1
	temp2=UC.PC[pcntr]
	temp3=temp1+temp2
	UC.DPTR=temp3
	pcntr=pcntr+1
	return pcntr	

def OP_92(pcntr):
	""" MOV bitaddr,C"""

def OP_93(pcntr):
	""" MOVC A,@A+DTPR"""
	tempA=UC.hex2dec(UC.A)
	tempDPTR=UC.hex2dec(UC.DPTR)
	UC.A=UC.RAM[tempA+tempDPTR]
	pcntr=pcntr+1
	return pcntr

def OP_A2(pcntr):
	""" MOV C,bitaddr"""


def OP_A5(pcntr):
	""" MOV B, #data. Not present in the actual opcode. Have added. JUGAAAD"""
	pcntr=pcntr+1
	pcntr=pcntr+1			#MOV B,#data is a 3 byte instruction
	UC.A=UC.ROM[pcntr]
	pcntr=pcntr+1
	return(pcntr)

def OP_A6(pcntr):
	""" MOV @R0,data"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.R0)
	UC.RAM[temp1]=UC.ROM[pcntr]
	pcntr=pcntr+1
	return pcntr

def OP_A7(pcntr):
	""" MOV @R1, data"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.R1)
	UC.RAM[temp1]=UC.ROM[pcntr]
	pcntr=pcntr+1
	return pcntr

def OP_A8(pcntr):
	"""MOV R0,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.R0=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr	

def OP_A9(pcntr):
	"""MOV R1,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.R1=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_AA(pcntr):
	"""MOV R2,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.R2=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_AB(pcntr):
	"""MOV R3,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.R3=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_AC(pcntr):
	"""MOV R4,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.R4=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_AD(pcntr):
	"""MOV R5,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.R5=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_AE(pcntr):
	"""MOV R6,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.R6=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_AF(pcntr):
	"""MOV R7,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.R7=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_E2(pcntr):
	"""MOVX A,@R0"""
	tempR0=UC.hex2dec(UC.R0)
	UC.A=UC.MEM[tempR0]
	pcntr=pcntr+1
	return pcntr

def OP_E3(pcntr):
	"""MOVX A,@R1"""
	tempR1=UC.hex2dec(UC.R1)
	UC.A=UC.MEM[tempR1]
	pcntr=pcntr+1
	return pcntr

def OP_E5(pcntr):
	"""MOV A,dataaddr"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.A=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_E6(pcntr):
	"""MOV A,@R0"""
	temp1=UC.hex2dec(UC.R0)
	UC.A=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_E7(pcntr):
	"""MOV A,@R1"""
	temp1=UC.hex2dec(UC.R1)
	UC.A=UC.RAM[temp1]
	pcntr=pcntr+1
	return pcntr

def OP_E8(pcntr):
	""" MOV A,R0"""
	UC.A = UC.R0
	pcntr=pcntr+1
	return(pcntr)


def OP_E9(pcntr):
	""" MOV A,R1"""
	UC.A = UC.R1
	pcntr=pcntr+1
	return(pcntr)

def OP_EA(pcntr):
	""" MOV A,R2"""
	UC.A = UC.R2
	pcntr=pcntr+1
	return(pcntr)

def OP_Eb(pcntr):
	""" MOV A,R3"""
	UC.A = UC.R3
	pcntr=pcntr+1
	return(pcntr)

def OP_EC(pcntr):
	""" MOV A,R4"""
	UC.A = UC.R4
	pcntr=pcntr+1
	return(pcntr)

def OP_ED(pcntr):
	""" MOV A,R5"""
	UC.A = UC.R5
	pcntr=pcntr+1
	return(pcntr)

def OP_EE(pcntr):
	""" MOV A,R6"""
	UC.A = UC.R6
	pcntr=pcntr+1
	return(pcntr)

def OP_EF(pcntr):
	""" MOV A,R7"""
	UC.A = UC.R7
	pcntr=pcntr+1
	return(pcntr)

def OP_F0(pcntr):
	"""MOVX @DPTR,A"""
	tempDPTR=UC.hex2dec(UC.DPTR)
	UC.MEM[tempDPTR]=UC.A
	pcntr=pcntr+1
	return pcntr

def OP_F2(pcntr):
	"""MOVX @R0,A"""
	tempR0=UC.hex2dec(UC.R0)
	UC.MEM[tempR0]=UC.A
	pcntr=pcntr+1
	return pcntr

def OP_F3(pcntr):
	"""MOVX @R1, A"""
	tempR1=UC.hex2dec(UC.R0)
	UC.MEM[tempR1]=UC.A
	pcntr=pcntr+1
	return pcntr

def OP_F5(pcntr):
	"""MOV dataaddr,A"""
	pcntr=pcntr+1
	temp1=UC.hex2dec(UC.ROM[pcntr])
	UC.RAM[temp1]=UC.A
	pcntr=pcntr+1
	return pcntr


def OP_F6(pcntr):
	"""MOV @R0,A"""
	temp1=UC.hex2dec(UC.R0)
	UC.RAM[temp1]=UC.A
	pcntr=pcntr+1

def OP_F7(pcntr):
	"""MOV @R1,A"""
	temp1=UC.hex2dec(UC.R1)
	UC.RAM[temp1]=UC.A
	pcntr=pcntr+1

def OP_F8(pcntr):
	"""MOV R0,A"""
	UC.R0=UC.A
	pcntr=pcntr+1
	return pcntr

def OP_F9(pcntr):
	"""MOV R1,A"""
	UC.R1=UC.A
	pcntr=pcntr+1
	return pcntr

def OP_FA(pcntr):
	"""MOV R2,A"""
	UC.R2=UC.A
	pcntr=pcntr+1
	return pcntr


def OP_FB(pcntr):
	"""MOV R3,A"""
	UC.R3=UC.A
	pcntr=pcntr+1
	return pcntr


def OP_FC(pcntr):
	"""MOV R4,A"""
	UC.R4=UC.A
	pcntr=pcntr+1
	return pcntr


def OP_FD(pcntr):
	"""MOV R5,A"""
	UC.R5=UC.A
	pcntr=pcntr+1
	return pcntr


def OP_FE(pcntr):
	"""MOV R6,A"""
	UC.R6=UC.A
	pcntr=pcntr+1
	return pcntr


def OP_FF(pcntr):
	"""MOV R7,A"""
	UC.R7=UC.A
	pcntr=pcntr+1
	return pcntr



	










#UC.R7=UC.dec2hex(14)
#UC.ROM[13] = UC.dec2hex(0)
#UC.ROM[14] = UC.dec2hex(1)

#pcntr=OP_8F(12)


#print UC.R7
#print pcntr
#print UC.MEM[1,0]
