#!/usr/bin/env python
from Baseclass import *

#opcode = []
#--- Dictionary of opcodes ---#
opc_dict = {'CJNER2#-': 'BA', 'ADDA@R1': '27', 'ADDA@R0': '26', 'ACALL-': 'F1', 'MOVAR5': 'ED', 'MOVR7A': 'FF', 'MOVX@DPTRA': 'F0', 'MOVR3#': '7B', 'CJNER1#-': 'B9', 'XCHDA@R0': 'D6', 'DIVAB': '84', 'MOVR3-': 'AB', 'MOV@R0#': '76', 'DJNZR1-': 'D9', 'ANL-#': '53', 'CJNER0#-': 'B8', 'RETI': '32', 'JNC-': '50', 'MOVR4A': 'FC', 'CJNEA#-': 'B4', 'ANL-A': '52', 'ANLA@R0': '56', 'INCR5': '0D', 'INCR4': '0C', 'INCR3': '0B', 'INCR2': '0A', 'INCR1': '09', 'INCR0': '08', 'MOVXA@R1': 'E3', 'MOVXA@R0': 'E2', 'MOV-@R0': '86', 'MOVR4#': '7C', 'MOVR1-': 'A9', 'JC-': '40', 'ORLC-': 'A0', 'INC@R0': '06', 'INC@R1': '07', 'AJMP-': 'E1', 'MOVR4-': 'AC', 'MOV-R2': '8A', 'DJNZR2-': 'DA', 'XCHDA@R1': 'D7', 'MOVX@R1A': 'F3', 'POP-': 'D0', 'MOVC-': 'A2', 'SUBBAR4': '9C', 'MOVR3A': 'FB', 'XCHA@R1': 'C7', 'CJNER7#-': 'BF', 'JB--': '20', 'MOVR7-': 'AF', 'XCHA-': 'C5', 'MOVR6-': 'AE', 'XCHAR0': 'C8', 'MOVX@R0A': 'F2', 'MOVR5#': '7D', 'SUBBAR5': '9D', 'JNB--': '30', 'MOVR5-': 'AD', 'MOVR2-': 'AA', 'MOV@R1A': 'F7', 'MOV-A': 'F5', 'MOV-C': '92', 'MOV@R0A': 'F6', 'DJNZR3-': 'DB', 'MOVR6A': 'FE', 'DJNZ--': 'D5', 'MOVR0A': 'F8', 'MOVCA@A+PC': '83', 'MOVA#': '74', 'MOVA-': 'E5', 'LJMP--': '02', 'ORLA#': '44', 'SUBBA@R1': '97', 'MOV-#': '75', 'MOV@R0-': 'A6', 'SUBBA@R0': '96', 'ADDCA@R1': '37', 'ORLAR3': '4B', 'ORLAR0': '48', 'ORLAR1': '49', 'ORLAR6': '4E', 'ORLAR7': '4F', 'ORLAR4': '4C', 'ORLAR5': '4D', 'XRLAR3': '6B', 'XRLAR2': '6A', 'XRLAR1': '69', 'XRLAR0': '68', 'XRLAR7': '6F', 'XRLAR6': '6E', 'XRLAR5': '6D', 'XRLAR4': '6C', 'DEC@R0': '16', 'DEC@R1': '17', 'XCHAR7': 'CF', 'MOVAR4': 'EC', 'MOVAR3': 'EB', 'MOVAR2': 'EA', 'MOVAR1': 'E9', 'XRLA-': '65', 'MOVR5A': 'FD', 'JMP@A+DPTR': '73', 'CLR-': 'C2', 'SUBBA#': '94', 'SUBBA-': '95', 'XCHA@R0': 'C6', 'NOP': '00', 'MULAB': 'A4', 'DJNZR4-': 'DC', 'MOV-R3': '8B', 'ANLAR1': '59', 'RRCA': '13', 'SUBBAR1': '99', 'MOV-R1': '89', 'RET': '22', 'CLRC': 'C3', 'ORLAR2': '4A', 'CLRA': 'E4', 'MOV-R0': '88', 'MOV-R4': '8C', 'MOV@R1-': 'A7', 'MOV-@R1': '87', 'ADDCA@R0': '36', 'MOVR7#': '7F', 'MOV-R7': '8F', 'CJNER4#-': 'BC', 'MOV@R1#': '77', 'CJNER6#-': 'BE', 'MOV-R6': '8E', 'JZ-': '60', 'MOV-R5': '8D', 'ANLAR7': '5F', 'SJMP-': '80', 'RRA': '03', 'MOV--': '85', 'MOVR2A': 'FA', 'ORLA-': '45', 'MOVR6#': '7E', 'DJNZR5-': 'DD', 'MOVR0-': 'A8', 'DEC-': '15', 'CJNEA--': 'B5', 'MOVR0#': '78', 'JBC--': '10', 'MOVCA@A+DPTR': '93', 'ADDCA#': '34', 'ADDCA-': '35', 'MOVDPTR#': '90', 'CPLA': 'F4', 'ANLA#': '54', 'ANLA-': '55', 'CJNER5#-': 'BD', 'RLA': '23', 'CPLC': 'B3', 'DJNZR6-': 'DE', 'CJNER3#-': 'BB', 'XRLA#': '64', 'MOVAR6': 'EE', 'DECR3': '1B', 'DECR2': '1A', 'DECR1': '19', 'DECR0': '18', 'DECR7': '1F', 'DECR6': '1E', 'DECR5': '1D', 'DECR4': '1C', 'ANLAR0': '58', 'ANLA@R1': '57', 'ANLAR2': '5A', 'ANLAR3': '5B', 'ANLAR4': '5C', 'ANLAR5': '5D', 'ANLAR6': '5E', 'INCR6': '0E', 'JNZ-': '70', 'DECA': '14', 'MOVR1#': '79', 'ADDCAR4': '3C', 'ADDCAR5': '3D', 'ADDCAR6': '3E', 'ADDCAR7': '3F', 'ADDCAR0': '38', 'ADDCAR1': '39', 'ADDCAR2': '3A', 'ADDCAR3': '3B', 'MOVAR0': 'E8', 'ORL-#': '43', 'SETBC': 'D3', 'XRLA@R0': '66', 'MOVA@R0': 'E6', 'DAA': 'D4', 'XRL-#': '63', 'PUSH-': 'C0', 'INCA': '04', 'SWAPA': 'C4', 'CJNE@R1#-': 'B7', 'DJNZR7-': 'DF', 'ADDAR2': '2A', 'ADDAR3': '2B', 'ADDAR0': '28', 'ADDAR1': '29', 'ADDAR6': '2E', 'ADDAR7': '2F', 'ADDAR4': '2C', 'ADDAR5': '2D', 'XCHAR2': 'CA', 'XCHAR3': 'CB', 'RLCA': '33', 'XCHAR1': 'C9', 'XCHAR6': 'CE', 'XRL-A': '62', 'XCHAR4': 'CC', 'XCHAR5': 'CD', 'MOVR2#': '7A', 'MOVAR7': 'EF', 'SETB-': 'D2', 'INCR7': '0F', 'INC-': '05', 'MOVA@R1': 'E7', 'LCALL--': '12', 'DJNZR0-': 'D8', 'ORLA@R1': '47', 'ORLA@R0': '46', 'INCDPTR': 'A3', 'CJNE@R0#-': 'B6', 'MOVR1A': 'F9', 'MOVXA@DPTR': 'E0', 'ANLC-': 'B0', 'ADDA#': '24', 'XRLA@R1': '67', 'SUBBAR6': '9E', 'SUBBAR7': '9F', 'SUBBAR0': '98', 'ADDA-': '25', 'SUBBAR2': '9A', 'SUBBAR3': '9B', 'CPL-': 'B2', 'ORL-A': '42'}

#--- SFR Dictionary ---#
sfrs_dict = {'B': 'F0', 'P0': '80', 'P1': '90', 'P2': 'A0', 'P3': 'B0', 'PSW': 'D0', 'SP': '81', 'DPL': '82', 'DPH': '83'}

#--- SFR List ---#
sfrs_list = ['B','P0','P1','P2','P3','PSW','SP','DPL','DPH']

#--- All possible nemonics ---#
codes = ['NOP', 'AJMP', 'LJMP', 'RR', 'INC', 'JBC', 'ACALL', 'LCALL', 'RRC', 'DEC', 'JB', 'RET', 'RL', 'ADD', 'JNB', 'RETI', 'RLC', 'ADDC', 'JC', 'ORL', 'JNC', 'ANL', 'JZ', 'XRL', 'JNZ', 'JMP', 'MOV', 'SJMP', 'MOVC', 'DIV', 'SUBB', 'MUL', 'CPL', 'CJNE', 'PUSH', 'CLR', 'SWAP', 'XCH', 'POP', 'SETB', 'DA', 'XCHD', 'DJNZ', 'MOVX']

#--- Registers ---#
regis = ['A','C','R0','R1','R2','R3','R4','R5','R6','R7','@R0','@R1','DPTR','@DPTR','@A+DPTR','@A+PC','AB']

#--- Label empty list and dictionary ---#
label_list = []
label_dict = {}
#-----------------------------------------------------------------------------------------------------------------------#

def splitcs(instrcs):
	#--- Split 'MOV A,#24' into ['MOV','A','#24'] ---#
	temp = instrcs.split(',')
	if len(temp) == 1:
		return instrcs.strip().split(' ')
	elif len(temp) == 2:
		return temp[0].strip().split(' ') + [temp[1].strip()]
	elif len(temp) == 3:
		return temp[0].strip().split(' ') + [temp[1].strip()] + [temp[2].strip()]

def splitinst(instr):
	#--- Split 'LABEL : MOV A,#24' into ['MOV','A','#24'] ---#
	temp = instr.split(':')
	if len(temp) == 1:
		return splitcs(temp[0])
	else:
		label_list.append(temp[0].strip())
		label_dict[temp[0].strip()] = UC.dec2hex(len(opcode))
		return splitcs(temp[1].strip())

def decode(instruction):
	instsplit = splitinst(instruction.upper())
	#--- Decode the splitted instruction ['MOV','A','7A'] to ['E5','7A'] ---#
	print instsplit
	temp2 = []
	opctemp = []
	if len(instsplit) == 1:
		opctemp += [opc_dict[instsplit[0]]]
#		print opctemp
		return opctemp
	elif instsplit[0] in codes:
		temp = instsplit[0]
		for n in range(1,len(instsplit)):
			if instsplit[n] in regis:
				temp = temp + instsplit[n]
			elif instsplit[n][0] == '#':
				temp = temp + '#'
				if len(instsplit[n]) == 3:
					temp2.append(instsplit[n][1:3])
				elif len(instsplit[n]) == 4:	#--- decode data of kind #0F3 ---#
					temp2.append(instsplit[n][2:4])
				elif len(instsplit[n]) == 5:	#--- For DPTR ---#
					temp2.append(instsplit[n][1:3])
					temp2.append(instsplit[n][3:5])
				elif len(instsplit[n]) == 6:	#--- decode data of kind #0F334 for DPTR ---#
					temp2.append(instsplit[n][2:4])
					temp2.append(instsplit[n][4:6])
				else:
					print "Error typing data " + instsplit[n]	#--- Error in data ---#
			else:
				temp = temp + '-'
				if instsplit[n] in sfrs_list:	#--- Decode SFR ---#
					temp2.append(sfrs_dict[instsplit[n]])
				elif instsplit[n] in label_list:
					temp2.append(label_dict[instsplit[n]])
				elif len(instsplit[n]) == 2:
					temp2.append(instsplit[n])
				elif len(instsplit[n]) == 3:	#--- decode code addr of kind 0F3 ---#
					temp2.append(instsplit[n][1:3])
				else:
					print "Error typing address " + instsplit[n]	#---- Error in address ---#

		opctemp += [opc_dict[temp]] + temp2
#		print opctemp
		return opctemp
	else:
		print "Error"

#allinstrlist = ['INC 7A','NOP', 'AJMP 4E', 'LJMP 4E,2E', 'RR A', 'INC A', 'INC 7A', 'INC @R0', 'INC @R1', 'INC R0', 'INC R1', 'INC R2', 'INC R3', 'INC R4', 'INC R5', 'INC R6', 'INC R7', 'JBC F3,4E', 'ACALL 4E', 'LCALL 4E,2E', 'RRC A', 'DEC A', 'DEC 7A', 'DEC @R0', 'DEC @R1', 'DEC R0', 'DEC R1', 'DEC R2', 'DEC R3', 'DEC R4', 'DEC R5', 'DEC R6', 'DEC R7', 'JB F3,4E', 'AJMP 4E', 'RET', 'RL A', 'ADD A,#25', 'ADD A,7A', 'ADD A,@R0', 'ADD A,@R1', 'ADD A,R0', 'ADD A,R1', 'ADD A,R2', 'ADD A,R3', 'ADD A,R4', 'ADD A,R5', 'ADD A,R6', 'ADD A,R7', 'JNB F3,4E', 'ACALL 4E', 'RETI', 'RLC A', 'ADDC A,#25', 'ADDC A,7A', 'ADDC A,@R0', 'ADDC A,@R1', 'ADDC A,R0', 'ADDC A,R1', 'ADDC A,R2', 'ADDC A,R3', 'ADDC A,R4', 'ADDC A,R5', 'ADDC A,R6', 'ADDC A,R7', 'JC 4E', 'AJMP 4E', 'ORL 7A,A', 'ORL 7A,#25', 'ORL A,#25', 'ORL A,7A', 'ORL A,@R0', 'ORL A,@R1', 'ORL A,R0', 'ORL A,R1', 'ORL A,R2', 'ORL A,R3', 'ORL A,R4', 'ORL A,R5', 'ORL A,R6', 'ORL A,R7', 'JNC 4E', 'ACALL 4E', 'ANL 7A,A', 'ANL 7A,#25', 'ANL A,#25', 'ANL A,7A', 'ANL A,@R0', 'ANL A,@R1', 'ANL A,R0', 'ANL A,R1', 'ANL A,R2', 'ANL A,R3', 'ANL A,R4', 'ANL A,R5', 'ANL A,R6', 'ANL A,R7', 'JZ 4E', 'AJMP 4E', 'XRL 7A,A', 'XRL 7A,#25', 'XRL A,#25', 'XRL A,7A', 'XRL A,@R0', 'XRL A,@R1', 'XRL A,R0', 'XRL A,R1', 'XRL A,R2', 'XRL A,R3', 'XRL A,R4', 'XRL A,R5', 'XRL A,R6', 'XRL A,R7', 'JNZ 4E', 'ACALL 4E', 'ORL C,F3', 'JMP @A+DPTR', 'MOV A,#25', 'MOV 7A,#25', 'MOV @R0,#25', 'MOV @R1,#25', 'MOV R0,#25', 'MOV R1,#25', 'MOV R2,#25', 'MOV R3,#25', 'MOV R4,#25', 'MOV R5,#25', 'MOV R6,#25', 'MOV R7,#25', 'SJMP 4E', 'AJMP 4E', 'ANL C,F3', 'MOVC A,@A+PC', 'DIV AB', 'MOV 7A,7A', 'MOV 7A,@R0', 'MOV 7A,@R1', 'MOV 7A,R0', 'MOV 7A,R1', 'MOV 7A,R2', 'MOV 7A,R3', 'MOV 7A,R4', 'MOV 7A,R5', 'MOV 7A,R6', 'MOV 7A,R7', 'MOV DPTR,#25', 'ACALL 4E', 'MOV F3,C', 'MOVC A,@A+DPTR', 'SUBB A,#25', 'SUBB A,7A', 'SUBB A,@R0', 'SUBB A,@R1', 'SUBB A,R0', 'SUBB A,R1', 'SUBB A,R2', 'SUBB A,R3', 'SUBB A,R4', 'SUBB A,R5', 'SUBB A,R6', 'SUBB A,R7', 'ORL C,F3', 'AJMP 4E', 'MOV C,F3', 'INC DPTR', 'MUL AB', 'MOV @R0,7A', 'MOV @R1,7A', 'MOV R0,7A', 'MOV R1,7A', 'MOV R2,7A', 'MOV R3,7A', 'MOV R4,7A', 'MOV R5,7A', 'MOV R6,7A', 'MOV R7,7A', 'ANL C,F3', 'ACALL 4E', 'CPL F3', 'CPL C', 'CJNE A,#25,4E', 'CJNE A,7A,4E', 'CJNE @R0,#25,4E', 'CJNE @R1,#25,4E', 'CJNE R0,#25,4E', 'CJNE R1,#25,4E', 'CJNE R2,#25,4E', 'CJNE R3,#25,4E', 'CJNE R4,#25,4E', 'CJNE R5,#25,4E', 'CJNE R6,#25,4E', 'CJNE R7,#25,4E', 'PUSH 7A', 'AJMP 4E', 'CLR F3', 'CLR C', 'SWAP A', 'XCH A,7A', 'XCH A,@R0', 'XCH A,@R1', 'XCH A,R0', 'XCH A,R1', 'XCH A,R2', 'XCH A,R3', 'XCH A,R4', 'XCH A,R5', 'XCH A,R6', 'XCH A,R7', 'POP 7A', 'ACALL 4E', 'SETB F3', 'SETB C', 'DA A', 'DJNZ 7A,4E', 'XCHD A,@R0', 'XCHD A,@R1', 'DJNZ R0,4E', 'DJNZ R1,4E', 'DJNZ R2,4E', 'DJNZ R3,4E', 'DJNZ R4,4E', 'DJNZ R5,4E', 'DJNZ R6,4E', 'DJNZ R7,4E', 'MOVX A,@DPTR', 'AJMP 4E', 'MOVX A,@R0', 'MOVX A,@R1', 'CLR A', 'MOV A,7A', 'MOV A,@R0', 'MOV A,@R1', 'MOV A,R0', 'MOV A,R1', 'MOV A,R2', 'MOV A,R3', 'MOV A,R4', 'MOV A,R5', 'MOV A,R6', 'MOV A,R7', 'MOVX @DPTR,A', 'ACALL 4E', 'MOVX @R0,A', 'MOVX @R1,A', 'CPL A', 'MOV 7A,A', 'MOV @R0,A', 'MOV @R1,A', 'MOV R0,A', 'MOV R1,A', 'MOV R2,A', 'MOV R3,A', 'MOV R4,A', 'MOV R5,A', 'MOV R6,A', 'MOV R7,A']

ainstr1 = 'MOV A,R1'
ainstr2 = 'MOV A,#23'
ainstr3 = 'MOV 0F2,#0F1'
ainstr4 = 'MOV @R0,#0f4'
ainstr5 = 'MOV r1,#020'
ainstr6 = 'MOV psw,r0'
ainstr7 = 'MOV p1,c'
ainstr8 = ' label : mov @r0,B '
ainstr9 = 'MOV r1,0f2'
ainstr10 = 'MOV A,B'
ainstr11 = 'MOV A,r1'
ainstr12 = 'MOV B,A'
ainstr13 = 'MOV @r0,A'
ainstr14 = 'MOV r0,A'
ainstr15 = 'movx @DPTR,A'
ainstr16 = 'mov DPTR,#0e321'
ainstr17 = 'MOV r1,DPH'
ainstr18 = 'SJMP label'
allinstrlist = ['NOP', 'AJMP 4E', 'LJMP 4E,2E', 'sameer:  MOV A,B', 'SJMP sameer', 'label : MOV DPTR,#e231', 'MOV r1,DPH', 'SJMP label']

#for ainstr in allinstrlist:
#	opcode += decode(ainstr)
#print opcode, label_list, label_dict
