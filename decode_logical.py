#!/usr/bin/python 
from Baseclass import *
form pylab import *

####################### AND operations #############################
## ANL(AND Logical)
# ANL data addr,A : 52
# ANL data addr,#data : 53
# ANL A,#data : 54
# ANL A,data addr: 55 
# ANL A,@R0: 56 
# ANL A,@R1: 57 
# ANL A,R0: 58
# ANL A,R1: 59 
# ANL A,R2: 5A 
# ANL A,R4: 5C  
# ANL A,R5: 5D 
# ANL A,R6: 5E 
# ANL A,R7: 5F   

# ANL data addr,A : 52
#if (opcode[UC.ROM] =='52'):
#	opr1=UC.ROM[PC+1]
#	opr2=UC.A


# ANL data addr,A : 52	
# Eg. ANL 40h,A
# (direct) = (direct) AND A
#def op_52(PC):
#	PC=PC+1
#	UC.ROM[P  C]=UC.ROM[PC] and UC.A
#	PC=PC+1
#	length=2
#	cycles=1
#	return PC

# ANL data addr,#data : 53 ##### Rewrite This ######  
#def op_53(PC):
#	PC=PC+1
#	temp1=UC.ROM[PC]
#	PC=PC+1
#	temp2=UC.ROM[PC]
#	PC=PC+1
	#value at temp1temp2 + UC.ROM[PC+1]
#	length=3
#	cycles=1
#	return PC

# ANL A,#data : 54   
def OP_54(pcntr):

	""" ANL A,#data """ 
	pcntr=pcntr+1
	UC.A=hex2dec(UC.A) & hex2dec(UC.ROM[pcntr])
	dec2hex(UC.A)
	pcntr=pcntr+1
	#length=2
	#cycles=1
	return PC
 
# ANL A,data addr: 55   	### Rewrite ### 
def op_55(PC):
	#temp=value at address
	A=A and temp
	length=2
	cycles=1
	PC=PC+length
	return PC

# ANL A,@R0: 56               ### Rewrite ### 
def op_56(PC):                      
	#temp=value of address stored in R0
	A=A and temp
	length=1
	cycles=1
	PC=PC+length
	return PC

# ANL A,@R1: 57    ### Rewrite ### 
def op_57(PC,):
	#temp=value of address stored in R1
	A=A and temp
	length=1
	cycles=1
	PC=PC+length
	return PC

# ANL A,R0: 58   
def op_58(PC):
	UC.A = UC.A and UC.R0
	length=1
	cycles=1
	PC=PC+length
	return PC

# ANL A,R1: 59   
def op_59(PC):
	UC.A = UC.A and UC.R1
	length=1
	cycles=1
	PC=PC+length
	return PC 

# ANL A,R2: 5A   
def op_5A(PC):
	UC.A = UC.A and UC.R2
	length=1
	cycles=1	
	PC=PC+length
	return PC

# ANL A,R3: 5B   
def op_5B(PC,):
	UC.A = UC.A and UC.R3
	length=1
	cycles=1
	PC=PC+length
	return PC

# ANL A,R4: 5C   
def op_5C(PC):
	UC.A = UC.A and UC.R4
	length=1
	cycles=1
	PC=PC+length
	return PC

# ANL A,R5: 5D   
def op_5D(PC):
	UC.A = UC.A and UC.R5
	length=1
	cycles=1
	PC=PC+length
	return PC

# ANL A,R6: 5E   
def op_5E(PC):
	UC.A = UC.A and UC.R6
	length=1
	cycles=1
	PC=PC+length
	return PC

# ANL A,R7: 5F   
def op_5F(PC):
	UC.A = UC.A and UC.R0
	length=1
	cycles=1
	PC=PC+length
	return PC

####################### OR Operations #############################
## ORL (OR Logical)
# ORL data addr,A : 42  
def op_52(PC):
	#temp=value at address
	temp=temp and A
	#address=temp
	length=2
	cycles=1
	PC=PC+length
	return PC

# ORL data addr,#data : 43   
def op_43(PC,):
	#temp=value at address
	temp=temp and data
	#address=temp
	length=3
	cycles=1
	PC=PC+length
	return PC

# ORL A,#data : 44   
def op_44(PC,):
	A=A and data
	length=2
	cycles=1
	PC=PC+length
	return PC
 
# ORL A,data addr: 45   
def op_45(PC,):
	#temp=value at address
	A=A and temp
	length=2
	cycles=1
	PC=PC+length
	return PC

# ORL A,@R0: 46   
def op_46(PC,):
	#temp=value of address stored in R0
	A=A and temp
	length=1
	cycles=1
	PC=PC+length
	return PC

# ORL A,@R1: 47   
def op_47(PC,):
	#temp=value of address stored in R1
	A=A and temp
	length=1
	cycles=1
	PC=PC+length
	return PC

# ORL A,R0: 48   
def op_48(PC,):
	A=A and R0
	length=1
	cycles=1
	PC=PC+length
	return PC

# ORL A,R1: 49   
def op_49(PC,):
	A=A and R1
	length=1
	cycles=1
	PC=PC+length
	return PC 

# ORL A,R2: 4A   
def op_4A(PC,):
	A=A and R2
	length=1
	cycles=1
	PC=PC+length
	return PC

# ORL A,R3: 4B   
def op_4B(PC,):
	A=A and R3
	length=1
	cycles=1
	PC=PC+length
	return PC

# ORL A,R4: 4C   
def op_4C(PC,):
	A=A and R4
	length=1
	cycles=1
	PC=PC+length
	return PC

# ORL A,R5: 4D   
def op_4D(PC,):
	A=A and R5
	length=1
	cycles=1
	PC=PC+length
	return PC

# ORL A,R6: 4E   
def op_4E(PC,):
	A=A and R6
	length=1
	cycles=1
	PC=PC+length
	return PC

# ORL A,R7: 4F   
def op_4F(PC,):
	A=A and R0
	length=1
	cycles=1
	PC=PC+length
	return PC

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



