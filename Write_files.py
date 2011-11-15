from Baseclass import *
from decoder import *

####### This file is used to file writing operation for GUI purpose #########
def Write_files():
	f=open('register.txt','w')
	f.write('Accumulator A \t = \t')
	f.write(UC.A)
	f.write('\nRegistor R0 \t = \t')
	f.write(UC.R0)
	f.write('\nRegistor R1 \t = \t')
	f.write(UC.R1)
	f.write('\nRegistor R2 \t = \t')
	f.write(UC.R2)
	f.write('\nRegistor R3 \t = \t')
	f.write(UC.R3)
	f.write('\nRegistor R4 \t = \t')
	f.write(UC.R4)
	f.write('\nRegistor R5 \t = \t')
	f.write(UC.R5)
	f.write('\nRegistor R6 \t = \t')
	f.write(UC.R6)
	f.write('\nRegistor R7 \t = \t')
	f.write(UC.R7)

	f.write('\nProgram Status Word (PSW) \t = \t')
	f.write(UC.PSW)

	f.write('\nProgram Counter PC \t = \t')
	f.write(str(UC.PC))
	f.close()

	f=open('opcode_write.txt','w')
	f.write('Address\t')
	f.write('\tOpcodes\n')

	for i in range(0,len(UC.ROM)):
		f.write(UC.dec2hex(i))
		f.write('\t=\t')
		f.write(UC.ROM[i])
		f.write('\n')

	f.close()





