#!/usr/bin/env python
from Baseclass import *

def setpsw(n):
	temp = UC.hex2dec(UC.bin2hex(UC.PSW[2:]))
	if n == 0:
		temp += 1
	elif n == 1:
		temp += 2
	elif n == 2:
		temp += 4
	elif n == 3:
		temp += 8
	elif n == 4:
		temp += 16
	elif n == 5:
		temp += 32
	elif n == 6:
		temp += 64
	elif n == 7:
		temp += 128
	else:
		print "Invalid bit number"
	UC.PSW = '0b'+UC.hex2bin(UC.dec2hex(int(temp)))

def OP_04(pcntr):
	#--- INC A ---#
	UC.A = UC.incr(UC.A,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_05(pcntr):
	#--- INC data addr ---#
	pcntr += 1
	temp = UC.hex2dec(pcntr)
	UC.RAM[temp] += 1
	pcntr += 1
	return(pcntr)

def OP_06(pcntr):
	#--- INC @R0 ---#
	temp = UC.hex2dec(UC.R0)
	UC.RAM[temp] += 1
	pcntr += 1
	return(pcntr)

def OP_07(pcntr):
	#--- INC @R1 ---#
	temp = UC.hex2dec(UC.R1)
	UC.RAM[temp] += 1
	pcntr += 1
	return(pcntr)

def OP_08(pcntr):
	#--- INC R0 ---#
	UC.R0 = UC.incr(UC.R0,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_09(pcntr):
	#--- INC R1 ---#
	UC.R1 = UC.incr(UC.R1,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_0A(pcntr):
	#--- INC R2 ---#
	UC.R2 = UC.incr(UC.R2,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_0B(pcntr):
	#--- INC R3 ---#
	UC.R3 = UC.incr(UC.R3,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_0C(pcntr):
	#--- INC R4 ---#
	UC.R4 = UC.incr(UC.R4,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_0D(pcntr):
	#--- INC R5 ---#
	UC.R5 = UC.incr(UC.R5,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_0E(pcntr):
	#--- INC R6 ---#
	UC.R6 = UC.incr(UC.R6,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_0F(pcntr):
	#--- INC R7 ---#
	UC.R7 = UC.incr(UC.R7,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_14(pcntr):
	#--- DEC A ---#
	UC.A = UC.decr(UC.A,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_15(pcntr):
	#--- DEC data addr ---#
	return(pcntr)

def OP_16(pcntr):
	#--- DEC @R0 ---#
	return(pcntr)

def OP_17(pcntr):
	#--- DEC @R1 ---#
	return(pcntr)

def OP_18(pcntr):
	#--- DEC R0 ---#
	UC.R0 = UC.decr(UC.R0,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_19(pcntr):
	#--- DEC R1 ---#
	UC.R1 = UC.decr(UC.R1,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_1A(pcntr):
	#--- DEC R2 ---#
	UC.R2 = UC.decr(UC.R2,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_1B(pcntr):
	#--- DEC R3 ---#
	UC.R3 = UC.decr(UC.R3,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_1C(pcntr):
	#--- DEC R4 ---#
	UC.R4 = UC.decr(UC.R4,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_1D(pcntr):
	#--- DEC R5 ---#
	UC.R5 = UC.decr(UC.R5,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_1E(pcntr):
	#--- DEC R6 ---#
	UC.R6 = UC.decr(UC.R6,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_1F(pcntr):
	#--- DEC R7 ---#
	UC.R7 = UC.decr(UC.R7,1)
	pcntr = pcntr + 1
	return(pcntr)

def OP_24(pcntr):
	#--- ADD A,#data ---#
	pcntr = pcntr + 1
	lsbsum = UC.dec2hex(int(add(UC.hex2dec(UC.A[1]),UC.hex2dec(UC.ROM[pcntr][1]))))
	fstnibb = add(UC.UC.A[1],)
	return(pcntr)

def OP_25(pcntr):
	#--- ADD A,data addr ---#
	return(pcntr)

def OP_26(pcntr):
	#--- ADD A,@R0 ---#
	return(pcntr)

def OP_27(pcntr):
	#--- ADD A,@R1 ---#
	return(pcntr)

def OP_28(pcntr):
	#--- ADD A,R0 ---#
	return(pcntr)

def OP_29(pcntr):
	#--- ADD A,R1 ---#
	return(pcntr)

def OP_2A(pcntr):
	#--- ADD A,R2 ---#
	return(pcntr)

def OP_2B(pcntr):
	#--- ADD A,R3 ---#
	return(pcntr)

def OP_2C(pcntr):
	#--- ADD A,R4 ---#
	return(pcntr)

def OP_2D(pcntr):
	#--- ADD A,R5 ---#
	return(pcntr)

def OP_2E(pcntr):
	#--- ADD A,R6 ---#
	return(pcntr)

def OP_2F(pcntr):
	#--- ADD A,R7 ---#
	return(pcntr)

def OP_34(pcntr):
	#--- ADDC A,#data ---#
	return(pcntr)

def OP_35(pcntr):
	#--- ADDC A,data addr ---#
	return(pcntr)

def OP_36(pcntr):
	#--- ADDC A,@R0 ---#
	return(pcntr)

def OP_37(pcntr):
	#--- ADDC A,@R1 ---#
	return(pcntr)

def OP_38(pcntr):
	#--- ADDC A,R0 ---#
	return(pcntr)

def OP_39(pcntr):
	#--- ADDC A,R1 ---#
	return(pcntr)

def OP_3A(pcntr):
	#--- ADDC A,R2 ---#
	return(pcntr)

def OP_3B(pcntr):
	#--- ADDC A,R3 ---#
	return(pcntr)

def OP_3C(pcntr):
	#--- ADDC A,R4 ---#
	return(pcntr)

def OP_3D(pcntr):
	#--- ADDC A,R5 ---#
	return(pcntr)

def OP_3E(pcntr):
	#--- ADDC A,R6 ---#
	return(pcntr)

def OP_3F(pcntr):
	#--- ADDC A,R7 ---#
	return(pcntr)

def OP_84(pcntr):
	#--- DIV AB ---#
	return(pcntr)

def OP_94(pcntr):
	#--- SUBB A,#data ---#
	return(pcntr)

def OP_95(pcntr):
	#--- SUBB A,data addr ---#
	return(pcntr)

def OP_96(pcntr):
	#--- SUBB A,@R0 ---#
	return(pcntr)

def OP_97(pcntr):
	#--- SUBB A,@R1 ---#
	return(pcntr)

def OP_98(pcntr):
	#--- SUBB A,R0 ---#
	return(pcntr)

def OP_99(pcntr):
	#--- SUBB A,R1 ---#
	return(pcntr)

def OP_9A(pcntr):
	#--- SUBB A,R2 ---#
	return(pcntr)

def OP_9B(pcntr):
	#--- SUBB A,R3 ---#
	return(pcntr)

def OP_9C(pcntr):
	#--- SUBB A,R4 ---#
	return(pcntr)

def OP_9D(pcntr):
	#--- SUBB A,R5 ---#
	return(pcntr)

def OP_9E(pcntr):
	#--- SUBB A,R6 ---#
	return(pcntr)

def OP_9F(pcntr):
	#--- SUBB A,R7 ---#
	return(pcntr)

def OP_A3(pcntr):
	#--- INC DPTR ---#
	return(pcntr)

def OP_A4(pcntr):
	#--- MUL AB ---#
	return(pcntr)

UC.A = '2B'
pc = OP_04(0)
print UC.A, pc
setpsw(7)
print UC.PSW
