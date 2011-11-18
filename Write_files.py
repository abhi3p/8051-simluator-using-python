from Baseclass import *
from decoder import *

####--- This file is used to file writing operation for GUI purpose ---#####
def Write_files():
	f=open('register.txt','w')
	f.write('Accumulator A \t = \t')
	f.write(UC.A)
	f.write('\nRegisters')	
	f.write('\nB \t = \t')
	f.write(UC.RAM[UC.hex2dec('F0')])
	f.write('\nR0 \t = \t')
	f.write(UC.R0)
	f.write('\nR1 \t = \t')
	f.write(UC.R1)
	f.write('\nR2 \t = \t')
	f.write(UC.R2)
	f.write('\nR3 \t = \t')
	f.write(UC.R3)
	f.write('\nR4 \t = \t')
	f.write(UC.R4)
	f.write('\nR5 \t = \t')
	f.write(UC.R5)
	f.write('\nR6 \t = \t')
	f.write(UC.R6)
	f.write('\nR7 \t = \t')
	f.write(UC.R7)

	f.write('\nProgram Status Word\t = \t')
	f.write(UC.PSW)

	f.write('\nProgram Counter PC \t = \t')
	f.write(str(UC.PC))
	f.close()

	f=open('opcode_write.txt','w')
	f.write('    Address\t')
	f.write('\tOpcodes\n')

	## Program Counter and OPCODES
	for i in range(0,len(UC.ROM)):
		f.write('      ')
		f.write(UC.dec2hex(i))
		f.write(' \t \t  ')
		f.write(UC.ROM[i])
		f.write('\n')
	f.close()

	## RAM
	f=open('ram_write.txt','w')
	f.write('                 Address\t')
	f.write('\t        Data\n')

	for i in range(0,len(UC.RAM)):
		f.write('                  ')
		f.write(UC.dec2hex(i))
		f.write(' \t       \t         ')
		f.write(UC.RAM[i])
		f.write('\n')


	f.close()

	## Log File
	f=open('log_write.txt','w')
	for i in range(0,UC.logcnt+1):
		f.write(UC.log[i])
		f.write('\n')
	f.close()
