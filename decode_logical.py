#!/usr/bin/python 
from Baseclass import *
form pylab import *

####################### AND operations #############################
## ANL(AND Logical)
# ANL data addr,A : 52 	 Not done
# ANL data addr,#data : 53	Not done
# ANL A,#data : 54  Not done
# ANL A,data addr: 55 Not done 
# ANL A,@R0: 56 Not done
# ANL A,@R1: 57 Not done
# ANL A,R0: 58
# ANL A,R1: 59 
# ANL A,R2: 5A 
# ANL A,R4: 5C  
# ANL A,R5: 5D 
# ANL A,R6: 5E 
# ANL A,R7: 5F   

# ANL A,#data : 54   
def OP_54(pcntr):
	""" ANL A,#data """ 
	pcntr=pcntr+1
	UC.A=UC.hex2dec(UC.A) & UC.hex2dec(UC.ROM[pcntr])
	UC.dec2hex(UC.A)
	pcntr=pcntr+1
	#length=2
	#cycles=1
	return PC
 
# ANL A,R0: 58   
def OP_58(pcntr):
	""" ANL A,R0 """
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R0)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R1: 59   
def OP_59(pcntr):
	""""ANL A,R1"""  
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R1)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R2: 5A   
def OP_5A(pcntr):
	"""ANL A,R2"""
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R2)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R3: 5B   
def OP_5B(pcntr):
	"""ANL A,R3"""
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R3)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R4: 5C   
def OP_5C(pcntr):
	"""ANL A,R4"""	
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R4)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R5: 5D   
def OP_5D(pcntr):
	"""ANL A,R5"""	
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R5)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R6: 5E   
def OP_5E(pcntr):
	"""ANL A,R6"""
        UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R6)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R7: 5F   
def OP_5F(PC):
	"""ANL A,R7"""
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R7)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

####################### OR Operations #############################
## ORL (OR Logical)
# ORL data addr,A : 42  
# ORL data addr,#data : 43  
# ORL A,#data : 44    
# ORL A,data addr: 45   
# ORL A,@R0: 46   
# ORL A,@R1: 47   
# ORL A,R0: 48   
# ORL A,R1: 49
# ORL A,R2: 4A  
# ORL A,R3: 4B   
# ORL A,R4: 4C   
# ORL A,R5: 4D   
# ORL A,R6: 4E   
# ORL A,R7: 4F      



# ORL A,#data : 44   
def OP_44(pcntr):
	pcntr=pcntr+1
	UC.A=UC.hex2dec(UC.A) | UC.hex2dec(UC.ROM[pcntr])
	UC.dec2hex(UC.A)
	pcntr=pcntr+1
	#length=2
	#cycles=1
	return PC


# ORL A,R0: 48   
def OP_48(pcntr):
	""" ORL A,R0 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R0)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R1: 49   
def OP_49(pcntr):
	""" ORL A,R1 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R1)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R2: 4A   
def OP_4A(pcntr):
	""" ORL A,R2 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R2)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R3: 4B   
def OP_4B(pcntr):
	""" ORL A,R3 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R3)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R4: 4C   
def OP_4C(pcntr):
	""" ORL A,R4 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R4)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R5: 4D   
def OP_4D(pcntr):
	""" ORL A,R5 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R5)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R6: 4E   
def OP_4E(pcntr):
	""" ORL A,R6 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R6)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R7: 4F   
def OP_4F(pcntr):
	""" ORL A,R7 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R7)
	UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

####################### XOR operations #############################
## XRL(Exclusive OR Logical)

# XRL data addr,A : 62  
def op_62(PC,):
	#temp=value at address
	temp=temp and A
	#address=temp
	length=2
	cycles=1
	PC=PC+length
	return PC

# XRL data addr,#data : 63   
def op_63(PC,):
	#temp=value at address
	temp=temp and data
	#address=temp
	length=3
	cycles=1
	PC=PC+length
	return PC

# XRL A,#data : 64   
def op_64(PC,):
	A=A and data
	length=2
	cycles=1
	PC=PC+length
	return PC
 
# XRL A,data addr: 65   
def op_65(PC,):
	#temp=value at address
	A=A and temp
	length=2
	cycles=1
	PC=PC+length
	return PC

# XRL A,@R0: 66   
def op_66(PC,):
	#temp=value of address stored in R0
	A=A and temp
	length=1
	cycles=1
	PC=PC+length
	return PC

# XRL A,@R1: 67   
def op_67(PC,):
	#temp=value of address stored in R1
	A=A and temp
	length=1
	cycles=1
	PC=PC+length
	return PC

# XRL A,R0: 68   
def op_68(PC,):
	A=A and R0
	length=1
	cycles=1
	PC=PC+length
	return PC

# XRL A,R1: 69   
def op_69(PC,):
	A=A and R1
	length=1
	cycles=1
	PC=PC+length
	return PC 

# XRL A,R2: 6A   
def op_6A(PC,):
	A=A and R2
	length=1
	cycles=1
	PC=PC+length
	return PC

# XRL A,R3: 6B   
def op_6B(PC,):
	A=A and R3
	length=1
	cycles=1
	PC=PC+length
	return PC

# XRL A,R4: 6C   
def op_6C(PC,):
	A=A and R4
	length=1
	cycles=1
	PC=PC+length
	return PC

# XRL A,R5: 6D   
def op_6D(PC,):
	A=A and R5
	length=1
	cycles=1
	PC=PC+length
	return PC

# XRL A,R6: 6E   
def op_6E(PC,):
	A=A and R6
	length=1
	cycles=1
	PC=PC+length
	return PC

# XRL A,R7: 6F   
def op_6F(PC,):
	A=A and R0
	length=1
	cycles=1
	PC=PC+length
	return PC

### Clear Accumulator ###
# CLR A: E4

def op_E4(PC):
	A=0
	lenght=1
	cycles=1
	PC=PC+length
	return PC

### Complement Accumulator ########
# CPL A : F4
def op_F4(PC):
	~A
	lenght=1
	cycles=1
	PC=PC+length
	return PC

### Rotate Instruction #######
# Rotate Accumulator left
# RL A:23
def op_23(PC):
	temp=bin(A)
	if (temp[2]==1):
		A<<1	
		A=A|0x01
	else:
		A<<1
	return PC

# Rotate Accumulator left through the carry
# RLC A: 33
def op_33(PC):
	temp=bin(A)
	if (CY==1):
		A<<1
		A=A|0x01
	elif (CY==0):
		A<<1
		A=A|0x00
	CY=temp[2]	
	return PC

# Rotate Accumulator right
# RR A:03
def op_03(PC):
	temp=bin(A)
	if (temp[-1]==1):
		A>>1
		A=A|0x10
	else:
		A>>1
	return PC

# Rotate Accumulator right through the carry
# RRC A: 13
def op_13(PC):
	temp=bin(A)
	if (CY==1):
		A>>1
		A=A|0x10
	elif (CY==0):
		A>>1
		A=A|0x00
	CY=temp[-1]	
	return PC


# Swap nibbles within the accumulator
# SWAP A: C4 
def op_C4(PC):
	temp=bin(A)
	new=[]
	
	
	return PC



