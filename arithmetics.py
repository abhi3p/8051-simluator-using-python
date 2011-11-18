#!/usr/bin/env python
from Baseclass import *
from psw import *

def addacc(lsb,msb):
	if lsb[0] != '0':
		setpsw(6)
		msb = UC.dec2hex(int(UC.hex2dec(msb)+1))
		if msb[0] != '0':
			setpsw(7)
			UC.A = msb[1]+lsb[1]
		else:
			UC.A = msb[1]+lsb[1]
	else:
		if msb[0] != '0':
			setpsw(7)
			UC.A = msb[1]+lsb[1]
		else:
			UC.A = msb[1]+lsb[1]

def OP_04(pcntr):
	#--- INC A ---#
	UC.A = UC.incr(UC.A,1)
	pcntr += 1
	return pcntr

def OP_05(pcntr):
	#--- INC data addr ---#
	pcntr += 1
	temp = UC.hex2dec(UC.ROM[pcntr])
	UC.RAM[temp] = UC.incr(UC.RAM[temp],1)
	pcntr += 1
	return pcntr

def OP_06(pcntr):
	#--- INC @R0 ---#
	temp = UC.hex2dec(UC.R0)
	UC.RAM[temp] = UC.incr(UC.RAM[temp],1)
	pcntr += 1
	return pcntr

def OP_07(pcntr):
	#--- INC @R1 ---#
	temp = UC.hex2dec(UC.R1)
	UC.RAM[temp] = UC.incr(UC.RAM[temp],1)
	pcntr += 1
	return pcntr

def OP_08(pcntr):
	#--- INC R0 ---#
	UC.R0 = UC.incr(UC.R0,1)
	pcntr += 1
	return pcntr

def OP_09(pcntr):
	#--- INC R1 ---#
	UC.R1 = UC.incr(UC.R1,1)
	pcntr += 1
	return pcntr

def OP_0A(pcntr):
	#--- INC R2 ---#
	UC.R2 = UC.incr(UC.R2,1)
	pcntr += 1
	return pcntr

def OP_0B(pcntr):
	#--- INC R3 ---#
	UC.R3 = UC.incr(UC.R3,1)
	pcntr += 1
	return pcntr

def OP_0C(pcntr):
	#--- INC R4 ---#
	UC.R4 = UC.incr(UC.R4,1)
	pcntr += 1
	return pcntr

def OP_0D(pcntr):
	#--- INC R5 ---#
	UC.R5 = UC.incr(UC.R5,1)
	pcntr += 1
	return pcntr

def OP_0E(pcntr):
	#--- INC R6 ---#
	UC.R6 = UC.incr(UC.R6,1)
	pcntr += 1
	return pcntr

def OP_0F(pcntr):
	#--- INC R7 ---#
	UC.R7 = UC.incr(UC.R7,1)
	pcntr += 1
	return pcntr

def OP_14(pcntr):
	#--- DEC A ---#
	UC.A = UC.decr(UC.A,1)
	pcntr += 1
	return pcntr

def OP_15(pcntr):
	#--- DEC data addr ---#
	pcntr += 1
	temp = UC.hex2dec(UC.ROM[pcntr])
	UC.RAM[temp] = UC.decr(UC.RAM[temp],1)
	pcntr += 1
	return pcntr

def OP_16(pcntr):
	#--- DEC @R0 ---#
	temp = UC.hex2dec(UC.R0)
	UC.RAM[temp] = UC.decr(UC.RAM[temp],1)
	pcntr += 1
	return pcntr

def OP_17(pcntr):
	#--- DEC @R1 ---#
	temp = UC.hex2dec(UC.R1)
	UC.RAM[temp] = UC.decr(UC.RAM[temp],1)
	pcntr += 1
	return pcntr

def OP_18(pcntr):
	#--- DEC R0 ---#
	UC.R0 = UC.decr(UC.R0,1)
	pcntr += 1
	return pcntr

def OP_19(pcntr):
	#--- DEC R1 ---#
	UC.R1 = UC.decr(UC.R1,1)
	pcntr += 1
	return pcntr

def OP_1A(pcntr):
	#--- DEC R2 ---#
	UC.R2 = UC.decr(UC.R2,1)
	pcntr += 1
	return pcntr

def OP_1B(pcntr):
	#--- DEC R3 ---#
	UC.R3 = UC.decr(UC.R3,1)
	pcntr += 1
	return pcntr

def OP_1C(pcntr):
	#--- DEC R4 ---#
	UC.R4 = UC.decr(UC.R4,1)
	pcntr += 1
	return pcntr

def OP_1D(pcntr):
	#--- DEC R5 ---#
	UC.R5 = UC.decr(UC.R5,1)
	pcntr += 1
	return pcntr

def OP_1E(pcntr):
	#--- DEC R6 ---#
	UC.R6 = UC.decr(UC.R6,1)
	pcntr += 1
	return pcntr

def OP_1F(pcntr):
	#--- DEC R7 ---#
	UC.R7 = UC.decr(UC.R7,1)
	pcntr += 1
	return pcntr

def OP_24(pcntr):
	#--- ADD A,#data ---#
	pcntr += 1
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.ROM[pcntr][1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.ROM[pcntr][0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_25(pcntr):
	#--- ADD A,data addr ---#
	pcntr += 1
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.ROM[pcntr])][1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.ROM[pcntr])][0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_26(pcntr):
	#--- ADD A,@R0 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.R0)][1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.R0)][0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_27(pcntr):
	#--- ADD A,@R1 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.R1)][1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.R1)][0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_28(pcntr):
	#--- ADD A,R0 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R0[1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R0[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1		
	return pcntr

def OP_29(pcntr):
	#--- ADD A,R1 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R1[1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R1[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_2A(pcntr):
	#--- ADD A,R2 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R2[1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R2[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_2B(pcntr):
	#--- ADD A,R3 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R3[1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R3[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_2C(pcntr):
	#--- ADD A,R4 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R4[1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R4[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_2D(pcntr):
	#--- ADD A,R5 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R5[1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R5[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_2E(pcntr):
	#--- ADD A,R6 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R6[1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R6[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_2F(pcntr):
	#--- ADD A,R7 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R7[1])))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R7[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_34(pcntr):
	#--- ADDC A,#data ---#
	pcntr += 1
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.ROM[pcntr][1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.ROM[pcntr][0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_35(pcntr):
	#--- ADDC A,data addr ---#
	pcntr += 1
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.ROM[pcntr])][1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.ROM[pcntr])][0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_36(pcntr):
	#--- ADDC A,@R0 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.R0)][1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.R0)][0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_37(pcntr):
	#--- ADDC A,@R1 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.R1)][1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.RAM[UC.hex2dec(UC.R1)][0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_38(pcntr):
	#--- ADDC A,R0 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R0[1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R0[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_39(pcntr):
	#--- ADDC A,R1 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R1[1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R1[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_3A(pcntr):
	#--- ADDC A,R2 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R2[1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R2[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_3B(pcntr):
	#--- ADDC A,R3 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R3[1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R3[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_3C(pcntr):
	#--- ADDC A,R4 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R4[1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R4[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_3D(pcntr):
	#--- ADDC A,R5 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R5[1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R5[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_3E(pcntr):
	#--- ADDC A,R6 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R6[1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R6[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_3F(pcntr):
	#--- ADDC A,R7 ---#
	lsbsum = UC.dec2hex(int(UC.hex2dec(UC.A[1])+UC.hex2dec(UC.R7[1])))
	if UC.PSW[2] == '1':
		lsbsum = UC.dec2hex(int(UC.hex2dec(lsbsum)+1))
	msbsum = UC.dec2hex(int(UC.hex2dec(UC.A[0])+UC.hex2dec(UC.R7[0])))
	addacc(lsbsum,msbsum)
	pcntr += 1
	return pcntr

def OP_84(pcntr):
	#--- DIV AB ---#
	if UC.RAM[UC.hex2dec('F0')] == '00':
		setpsw(2)
	else:
		temp = UC.dec2hex(int(UC.hex2dec(UC.A)/UC.hex2dec(UC.RAM[UC.hex2dec('F0')])))
		UC.RAM[UC.hex2dec('F0')] = UC.dec2hex(int(UC.hex2dec(UC.A)%UC.hex2dec(UC.RAM[UC.hex2dec('F0')])))
		UC.A = temp
	pcntr += 1
	return pcntr

def OP_94(pcntr):
	#--- SUBB A,#data ---#
	pcntr += 1
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.ROM[pcntr]))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.ROM[pcntr]))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_95(pcntr):
	#--- SUBB A,data addr ---#
	pcntr += 1
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.RAM[UC.hex2dec(UC.ROM[pcntr])]))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.RAM[UC.hex2dec(UC.ROM[pcntr])]))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_96(pcntr):
	#--- SUBB A,@R0 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.RAM[UC.hex2dec(UC.R0[pcntr])]))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.RAM[UC.hex2dec(UC.R0[pcntr])]))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_97(pcntr):
	#--- SUBB A,@R1 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.RAM[UC.hex2dec(UC.R1[pcntr])]))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.RAM[UC.hex2dec(UC.R1[pcntr])]))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_98(pcntr):
	#--- SUBB A,R0 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.R0))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.R0))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_99(pcntr):
	#--- SUBB A,R1 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.R1))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.R1))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_9A(pcntr):
	#--- SUBB A,R2 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.R2))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.R2))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_9B(pcntr):
	#--- SUBB A,R3 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.R3))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.R3))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_9C(pcntr):
	#--- SUBB A,R4 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.R4))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.R4))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_9D(pcntr):
	#--- SUBB A,R5 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.R5))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.R5))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_9E(pcntr):
	#--- SUBB A,R6 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.R6))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.R6))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_9F(pcntr):
	#--- SUBB A,R7 ---#
	temp = int(UC.hex2dec(UC.A)-UC.hex2dec(UC.R7))
	if temp >= 0:
		UC.A = UC.dec2hex(temp)
		resetpsw(7)
	else:
		UC.A = UC.dec2hex(int(UC.hex2dec(UC.A)+UC.hex2dec(cpl2(UC.R7))))
		setpsw(7)
	pcntr += 1
	return pcntr

def OP_A3(pcntr):
	#--- INC DPTR ---#
	return pcntr

def OP_A4(pcntr):
	#--- MUL AB ---#
	mult = UC.dec2hex(int(UC.hex2dec(UC.A)*UC.hex2dec(UC.RAM[UC.hex2dec('F0')])))
	if len(mult) == 2:
		UC.A = mult
		UC.RAM[UC.hex2dec('F0')] = UC.dec2hex(0)
	elif len(mult) == 3:
		UC.A = mult[1:]
		UC.RAM[UC.hex2dec('F0')] = '0'+mult[0]
	elif len(mult) == 4:
		UC.A = mult[2:]
		UC.RAM[UC.hex2dec('F0')] = mult[:2]
	else:
		setpsw(2)
	pcntr += 1
	return pcntr
