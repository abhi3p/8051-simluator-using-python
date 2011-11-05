#!/usr/bin/env python

opcode = []

opc_dict = {'CJNER2#-': 'BA', 'ADDA@R1': '27', 'ADDA@R0': '26', 'ACALL-': 'F1', 'MOVAR5': 'ED', 'MOVR7A': 'FF', 'MOVX@DPTRA': 'F0', 'MOVR3#': '7B', 'CJNER1#-': 'B9', 'XCHDA@R0': 'D6', 'DIVAB': '84', 'MOVR3-': 'AB', 'MOV@R0#': '76', 'DJNZR1-': 'D9', 'ANL-#': '53', 'CJNER0#-': 'B8', 'LJMP-': '02', 'RETI': '32', 'JNC-': '50', 'MOVR4A': 'FC', 'ANLA@R1': '57', 'CJNEA#-': 'B4', 'ANL-A': '52', 'ANLA@R0': '56', 'INCR5': '0D', 'INCR4': '0C', 'INCR3': '0B', 'INCR2': '0A', 'INCR1': '09', 'INCR0': '08', 'MOVXA@R1': 'E3', 'MOVXA@R0': 'E2', 'MOV-@R0': '86', 'MOVR4#': '7C', 'MOVR1-': 'A9', 'JC-': '40', 'ORLC-': 'A0', 'INC@R0': '06', 'INC@R1': '07', 'AJMP-': 'E1', 'MOVR4-': 'AC', 'MOV-R2': '8A', 'DJNZR2-': 'DA', 'XCHDA,@R1': 'D7', 'MOVX@R1A': 'F3', 'POP-': 'D0', 'MOVC-': 'A2', 'SUBBAR4': '9C', 'MOVR3A': 'FB', 'served': 'A5', 'XCHA@R1': 'C7', 'CJNER7#-': 'BF', 'JB--': '20', 'MOVR7-': 'AF', 'XCHA-': 'C5', 'MOVR6-': 'AE', 'XCHAR0': 'C8', 'MOVX@R0A': 'F2', 'MOVR5#': '7D', 'SUBBAR5': '9D', 'JNB--': '30', 'MOVR5-': 'AD', 'MOVR2-': 'AA', 'MOV@R1A': 'F7', 'MOV-A': 'F5', 'MOV-C': '92', 'MOV@R0A': 'F6', 'DJNZR3-': 'DB', 'MOVR6A': 'FE', 'DJNZ--': 'D5', 'MOVR0A': 'F8', 'MOVCA@A+PC': '83', 'MOVA#': '74', 'MOVA-': 'E5', 'ORLA#': '44', 'SUBBA@R1': '97', 'MOV-#': '75', 'MOV@R0-': 'A6', 'SUBBA@R0': '96', 'ADDCA@R1': '37', 'ORLAR3': '4B', 'ORLAR0': '48', 'ORLAR1': '49', 'ORLAR6': '4E', 'ORLAR7': '4F', 'ORLAR4': '4C', 'ORLAR5': '4D', 'XRLAR3': '6B', 'XRLAR2': '6A', 'XRLAR1': '69', 'XRLAR0': '68', 'XRLAR7': '6F', 'XRLAR6': '6E', 'XRLAR5': '6D', 'XRLAR4': '6C', 'DEC@R0': '16', 'DEC@R1': '17', 'XCHAR7': 'CF', 'MOVAR4': 'EC', 'MOVAR3': 'EB', 'MOVAR2': 'EA', 'MOVAR1': 'E9', 'XRLA-': '65', 'MOVR5A': 'FD', 'JMP@A+DPTR': '73', 'CLR-': 'C2', 'SUBBA#': '94', 'SUBBA-': '95', 'XCHA@R0': 'C6', 'NOP': '00', 'MULAB': 'A4', 'DJNZR4-': 'DC', 'MOV-R3': '8B', 'ANLAR1': '59', 'RRCA': '13', 'SUBBAR1': '99', 'MOV-R1': '89', 'RET': '22', 'CLRC': 'C3', 'ORLAR2': '4A', 'CLRA': 'E4', 'MOV-R0': '88', 'MOV-R4': '8C', 'MOV@R1-': 'A7', 'MOV-@R1': '87', 'ADDCA@R0': '36', 'MOVR7#': '7F', 'MOV-R7': '8F', 'CJNER4#-': 'BC', 'MOV@R1#': '77', 'CJNER6#-': 'BE', 'MOV-R6': '8E', 'JZ-': '60', 'MOV-R5': '8D', 'ANLAR7': '5F', 'SJMP-': '80', 'RRA': '03', 'MOV--': '85', 'MOVR2A': 'FA', 'ORLA-': '45', 'MOVR6#': '7E', 'DJNZR5-': 'DD', 'MOVR0-': 'A8', 'MOVA@R1': 'E7', 'CJNEA--': 'B5', 'MOVR0#': '78', 'JBC--': '10', 'MOVCA@A+DPTR': '93', 'ADDCA#': '34', 'ADDCA-': '35', 'MOVDPTR#': '90', 'CPLA': 'F4', 'ANLA#': '54', 'ANLA-': '55', 'CJNER5#-': 'BD', 'RLA': '23', 'CPLC': 'B3', 'DJNZR6-': 'DE', 'CJNER3#-': 'BB', 'XRLA#': '64', 'MOVAR6': 'EE', 'DECR3': '1B', 'DECR2': '1A', 'DECR1': '19', 'DECR0': '18', 'DECR7': '1F', 'DECR6': '1E', 'DECR5': '1D', 'DECR4': '1C', 'ANLAR0': '58', 'INCR7': '0F', 'ANLAR2': '5A', 'ANLAR3': '5B', 'ANLAR4': '5C', 'ANLAR5': '5D', 'ANLAR6': '5E', 'INCR6': '0E', 'JNZ-': '70', 'DECA': '14', 'MOVR1#': '79', 'ADDCAR4': '3C', 'ADDCAR5': '3D', 'ADDCAR6': '3E', 'ADDCAR7': '3F', 'ADDCAR0': '38', 'ADDCAR1': '39', 'ADDCAR2': '3A', 'ADDCAR3': '3B', 'MOVAR0': 'E8', 'ORL-#': '43', 'SETBC': 'D3', 'XRLA@R0': '66', 'MOVA@R0': 'E6', 'DAA': 'D4', 'XRL-#': '63', 'PUSH-': 'C0', 'INCA': '04', 'SWAPA': 'C4', 'CJNE@R1#-': 'B7', 'DJNZR7-': 'DF', 'ADDAR2': '2A', 'ADDAR3': '2B', 'ADDAR0': '28', 'ADDAR1': '29', 'ADDAR6': '2E', 'ADDAR7': '2F', 'ADDAR4': '2C', 'ADDAR5': '2D', 'XCHAR2': 'CA', 'XCHAR3': 'CB', 'RLCA': '33', 'XCHAR1': 'C9', 'XCHAR6': 'CE', 'XRL-A': '62', 'XCHAR4': 'CC', 'XCHAR5': 'CD', 'MOVR2#': '7A', 'MOVAR7': 'EF', 'SETB-': 'D2', 'INC-': '05', 'LCALL-': '12', 'DEC-': '15', 'DJNZR0-': 'D8', 'ORLA@R1': '47', 'ORLA@R0': '46', 'INCDPTR': 'A3', 'CJNE@R0#-': 'B6', 'MOVR1A': 'F9', 'MOVXA@DPTR': 'E0', 'ANLC-': 'B0', 'ADDA#': '24', 'XRLA@R1': '67', 'SUBBAR6': '9E', 'SUBBAR7': '9F', 'SUBBAR0': '98', 'ADDA-': '25', 'SUBBAR2': '9A', 'SUBBAR3': '9B', 'CPL-': 'B2', 'ORL-A': '42'}

# print opc_dict, opc_dict['NOP'], opc_dict['MOVR7A']

codes = ['ADD','MOV','SUB','MUL','CJNE','INC']
regis = ['A','B','C','R0','R1','R2','R3','R4','R5','R6','R7','@R0','@R1','@DPTR','@A+DPTR','@A+PC']

instr1 = 'ADD A, #10'
instr2 = 'MOV A, R1'
instr3 = 'MOV A, @R1'
instr4 = 'MOV 20, #25'
instr5 = 'INC A'
instr6 = 'CJNE R7, #10, 20'

def split(instr):
	temp = instr.split(':')
	if len(temp) == 1:
		temp = instr.split(',')
		if len(temp) == 1:
			return instr.split(' ')
		elif len(temp) == 2:
			return temp[0].split(' ') + [temp[1].strip()]
		elif len(temp) == 3:
			return temp[0].split(' ') + [temp[1].strip()] + [temp[2].strip()]
	else:
		print "Label"

#def exdata(adata):
	

def decode(inst):
	instsplit = split(inst)
	temp2 = []
	opctemp = []
	print instsplit
	if instsplit[0] in codes:
		temp = instsplit[0]
		for n in range(1,len(instsplit)):
			if instsplit[n] in regis:
				temp = temp + instsplit[n]
			elif instsplit[n][0] == '#':
				temp = temp + '#'
				if len(instsplit[n]) == 3:
					temp2.append(instsplit[n][1:3])
				elif len(instsplit[n]) == 4:
					temp2.append(instsplit[n][2:4])
			else:
				temp = temp + '-'
				temp2.append(instsplit[n])
				
	else:
		print "Error"

	opctemp += [opc_dict[temp]] + temp2
	return opctemp

opcode += decode(instr6)
print opcode

