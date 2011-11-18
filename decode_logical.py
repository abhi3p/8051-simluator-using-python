#!/usr/bin/python 
from Baseclass import *

####################### AND OPerations #############################
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

# ANL data addr,A : 52				## Uncomment if we will use ###
#def OP_52(pcntr):
#	""" ANL data addr,A """
#	pcntr=pcntr+1
#	temp=UC.Data[UC.ROM[pcntr]]
#	UC.Data[UC.ROM[pcntr]]=UC.hex2dec(temp)& UC.hex2dec(UC.A)
#	UC.Data[UC.ROM[pcntr]]=UC.dec2hex(UC.Data[UC.ROM[pcntr]]) 
#	pcntr=pcntr+1
#	return pcntr

# ANL data addr,#data : 53			## Uncomment if we will use ###
#def OP_53(pcntr):
#	""" ANL data addr,#data """"
#	pcntr=pcntr+1
#	temp1=UC.Data[UC.ROM[pcntr]]
#	temp_pcntr=pcntr
#	pcntr=pcntr+1
#	temp2=UC.ROM[pcntr]
#	UC.Data[UC.ROM[temp_pcntr]]=UC.hex2dec(temp1) & UC.hex2dec(temp2) 
#	UC.Data[UC.ROM[temp_pcntr]]=UC.dec2hex(UC.Data[UC.ROM[temp_pcntr]])
#	return pcntr


# ANL A,#data : 54   
def OP_54(pcntr):
	""" ANL A,#data """ 
	pcntr=pcntr+1
	UC.A=UC.hex2dec(UC.A) & UC.hex2dec(UC.ROM[pcntr])
	UC.A=UC.dec2hex(UC.A)
	pcntr=pcntr+1
	#length=2
	#cycles=1
	return pcntr

# ANL A,data addr : 55				## Uncomment if we use ###
#def OP_55(pcntr):
#	""" ANL A, data addr """
#	pcntr=pcntr+1
#	temp1=UC.Data[UC.ROM[pcntr]]
#	UC.A=UC.hex2dec(UC.A) & UC.hex2dec(temp1)
#	UC.A=UC.dec2hex(UC.A)
#	return pcntr

#ANL A,@R0: 56					## Uncomment if we use ###
#def OP_56(pcntr):
#	""" ANL A, @R0"""
#	temp1=UC.Data[UC.R0]
#	UC.A=UC.hex2dec(UC.A) & UC.hex2dec(temp1)
#	UC.A=UC.dec2hex(UC.A)
#	pcntr=pcntr+1
#	return pcntr

#ANL A,@R0: 57					## Uncomment if we use ###
#def OP_57(pcntr):
#	""" ANL A, @R0"""
#	temp1=UC.Data[UC.R1]
#	UC.A=UC.hex2dec(UC.A) & UC.hex2dec(temp1)
#	UC.A=UC.dec2hex(UC.A)
#	pcntr=pcntr+1
#	return pcntr

# ANL A,R0: 58   
def OP_58(pcntr):
	""" ANL A,R0 """
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R0)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R1: 59   
def OP_59(pcntr):
	""""ANL A,R1"""  
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R1)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R2: 5A   
def OP_5A(pcntr):
	"""ANL A,R2"""
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R2)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R3: 5B   
def OP_5B(pcntr):
	"""ANL A,R3"""
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R3)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R4: 5C   
def OP_5C(pcntr):
	"""ANL A,R4"""	
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R4)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R5: 5D   
def OP_5D(pcntr):
	"""ANL A,R5"""	
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R5)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R6: 5E   
def OP_5E(pcntr):
	"""ANL A,R6"""
        UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R6)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ANL A,R7: 5F   
def OP_5F(pcntr):
	"""ANL A,R7"""
	UC.A = UC.hex2dec(UC.A) & UC.hex2dec(UC.R7)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

####################### OR OPerations #############################
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
	""" ORL A,#data """
	pcntr=pcntr+1
	UC.A=UC.hex2dec(UC.A) | UC.hex2dec(UC.ROM[pcntr])
	UC.A=UC.dec2hex(UC.A)
	pcntr=pcntr+1
	#length=2
	#cycles=1
	return pcntr


# ORL A,R0: 48   
def OP_48(pcntr):
	""" ORL A,R0 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R0)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R1: 49   
def OP_49(pcntr):
	""" ORL A,R1 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R1)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R2: 4A   
def OP_4A(pcntr):
	""" ORL A,R2 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R2)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R3: 4B   
def OP_4B(pcntr):
	""" ORL A,R3 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R3)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R4: 4C   
def OP_4C(pcntr):
	""" ORL A,R4 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R4)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R5: 4D   
def OP_4D(pcntr):
	""" ORL A,R5 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R5)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R6: 4E   
def OP_4E(pcntr):
	""" ORL A,R6 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R6)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# ORL A,R7: 4F   
def OP_4F(pcntr):
	""" ORL A,R7 """
	UC.A = UC.hex2dec(UC.A) | UC.hex2dec(UC.R7)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

####################### XOR OPerations #############################
## XRL(Exclusive OR Logical)
# XRL data addr,A : 62  
# XRL data addr,#data : 63  
# XRL A,#data : 64    
# XRL A,data addr: 65   
# XRL A,@R0: 66   
# XRL A,@R1: 67   
# XRL A,R0: 68   
# XRL A,R1: 69
# XRL A,R2: 6A  
# XRL A,R3: 6B   
# XRL A,R4: 6C   
# XRL A,R5: 6D   
# XRL A,R6: 6E   
# XRL A,R7: 6F 


# XRL data addr,A : 62  
#def OP_62(pcntr):
	#return pcntr

# XRL data addr,#data : 63   
#def OP_63(pcntr):
	#return pcntr

# XRL A,#data : 64   
def OP_64(pcntr):
	""" XRL A,#data """
	pcntr=pcntr+1
	UC.A=UC.hex2dec(UC.A) | UC.hex2dec(UC.ROM[pcntr])
	UC.A=UC.dec2hex(UC.A)
	pcntr=pcntr+1
	#length=2
	#cycles=1
	return pcntr
 
# XRL A,data addr: 65   
#def OP_65(pcntr):
#	return pcntr

# XRL A,@R0: 66   
#def OP_66(pcntr):
#	return pcntr

# XRL A,@R1: 67   
#def OP_67(pcntr):
#	return pcntr

# XRL A,R0: 68   
def OP_68(pcntr):
	""" XRL A,R0 """ 
	UC.A = UC.hex2dec(UC.A) ^ UC.hex2dec(UC.R0)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# XRL A,R1: 69   
def OP_69(pcntr):
	""" XRL A,R1 """ 
	UC.A = UC.hex2dec(UC.A) ^ UC.hex2dec(UC.R1)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# XRL A,R2: 6A   
def OP_6A(pcntr):
	""" XRL A,R2 """ 
	UC.A = UC.hex2dec(UC.A) ^ UC.hex2dec(UC.R2)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# XRL A,R3: 6B   
def OP_6B(pcntr):
	""" XRL A,R2 """ 
	UC.A = UC.hex2dec(UC.A) ^ UC.hex2dec(UC.R3)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# XRL A,R4: 6C   
def OP_6C(pcntr):
	""" XRL A,R4 """ 
	UC.A = UC.hex2dec(UC.A) ^ UC.hex2dec(UC.R4)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# XRL A,R5: 6D   
def OP_6D(pcntr):
	""" XRL A,R5 """ 
	UC.A = UC.hex2dec(UC.A) ^ UC.hex2dec(UC.R5)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# XRL A,R6: 6E   
def OP_6E(pcntr):
	""" XRL A,R6 """ 
	UC.A = UC.hex2dec(UC.A) ^ UC.hex2dec(UC.R6)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

# XRL A,R7: 6F   
def OP_6F(pcntr):
	""" XRL A,R2 """ 
	UC.A = UC.hex2dec(UC.A) ^ UC.hex2dec(UC.R7)
	UC.A=UC.dec2hex(UC.A)	
	#length=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

############## Clear Accumulator #####################
# CLR A: E4
def OP_E4(pcntr):
	""" CLR A """
	UC.A=0
	UC.A=UC.dec2hex(UC.A)	
	pcntr=pcntr+1
	#lenght=1
	#cycles=1
	return pcntr

############# Complement Accumulator ######################
# CPL A : F4
def OP_F4(pcntr):
	""" CPL A """ 
	temp1=UC.hex2bin(UC.A)
	temp2=[]	
	for n in range(0,len(temp1)):
		temp2.append(temp1[n])
		
	for n in range(0,len(temp2)):
		if (temp2[n]=='0'):
			temp2[n]='1'
		elif(temp2[n]=='1'):
			temp2[n]='0'
	
	temp3=''.join(temp2)
	UC.A=UC.bin2hex(temp3)
	#lenght=1
	#cycles=1
	pcntr=pcntr+1
	return pcntr

################## Rotate Instruction #####################
# Rotate Accumulator left
# RL A:23
def OP_23(pcntr):
	""" RL A """
	UC.A=UC.hex2dec(UC.A)
	UC.A=2*UC.A
	UC.A=UC.dec2hex(UC.A)	
	pcntr=pcntr+1

	#temp=A
	#if (temp[2]==1):
	#	A<<1	
	#	A=A|0x01
	#else:
	#	A<<1
	#length=1	
	
	return pcntr

# Rotate Accumulator left through the carry
# RLC A: 33
def OP_33(pcntr):
	""" RLC A """ 
	temp1=UC.hex2bin(UC.A)
	temp2=UC.hex2dec(UC.A)
	temp2=temp2*2
	if UC.PSW[0]==1:
		temp2=temp2|1
	elif UC.PSW[0]==0:
		temp2=temp2|0
	UC.A=UC.dec2hex(temp2)
	UC.PSW[0]=temp1[0]
	pcntr=pcntr+1
	#temp=bin(A)
	#if (CY==1):
	#	A<<1
	#	A=A|0x01
	#elif (CY==0):
	#	A<<1
	#	A=A|0x00
	#CY=temp[2]	
	return pcntr

# Rotate Accumulator right
# RR A:03
def OP_03(pcntr):
	""" RR A """
	UC.A=UC.hex2dec(UC.A)
	UC.A=UC.A/2
	UC.A=UC.dec2hex(UC.A)	
	pcntr=pcntr+1

	#temp=bin(A)
	#if (temp[-1]==1):
	#	A>>1
	#	A=A|0x10
	#else:
	#	A>>1
	return pcntr

# Rotate Accumulator right through the carry
# RRC A: 13
def OP_13(pcntr):
	""" RRC A """
	temp1=UC.hex2bin(UC.A)
	temp2=UC.hex2dec(UC.A)
	temp2=temp2/2
	if UC.PSW[0]==1:
		temp2=temp2|16
	elif UC.PSW[0]==0:
		temp2=temp2|00
	UC.A=UC.dec2hex(temp2)
	UC.PSW[0]=temp1[len(temp1)-1]
	pcntr=pcntr+1

#	temp=bin(A)
#	if (CY==1):
#		A>>1
#		A=A|0x10
#	elif (CY==0):
#		A>>1
#		A=A|0x00
#	CY=temp[-1]	
	return pcntr


# Swap nibbles within the accumulator
# SWAP A: C4 
def OP_C4(pcntr):
	""" SWAP A """
	temp1=UC.hex2bin(UC.A)
	temp2=temp1[4:]+temp1[0:4]
	UC.A=UC.bin2hex(temp2)
	pcntr=pcntr+1	
	return pcntr



