from Tkinter import *
import string
import Tkinter
import Pmw
from Baseclass import *
from decoder import *

######## GUI FILE #############
def GUI():
	class MyApp:
		def __init__(self, parent):
		
			self.myParent = parent 
			self.myContainer1 = Frame(parent) 
			self.myContainer1.pack()
	
			# top frame
			self.top_frame = Frame(self.myContainer1) 
			self.top_frame.pack(side=TOP,
				fill=BOTH, 
				expand=YES,
				)  

			#bottom frame
			self.bottom_frame = Frame(self.myContainer1, 
				borderwidth=5,  relief=RAISED,
				height=500, 
				background="gray",
				)   
			self.bottom_frame.pack(side=TOP,
				fill=BOTH, 
				expand=YES,
				)  

				
			# left_frame        
			self.left_frame = Frame(self.top_frame, background="gray",
				borderwidth=5,  relief=RAISED,
				height=500, 
				width=320, 
				)
			self.left_frame.pack(side=LEFT,
				fill=BOTH, 
				expand=YES,
				)  


			### right_frame 
			self.right_frame = Frame(self.top_frame, background="gray",
				borderwidth=5,  relief=RAISED,
				width=320,
				)
			self.right_frame.pack(side=RIGHT,
				fill=BOTH, 
				expand=YES,
				)  

			### center_frame RIGHT
			self.center_frame1 = Frame(self.top_frame, background="gray",
				borderwidth=5,  relief=RAISED,
				width=320,
				)
			self.center_frame1.pack(side=RIGHT,
				fill=BOTH, 
				expand=YES,
				)  		
			### centre_frame LEFT
			self.center_frame2 = Frame(self.top_frame, background="gray",
				borderwidth=5,  relief=RAISED,
				width=320,
				)
			self.center_frame2.pack(side=LEFT,
				fill=BOTH, 
				expand=YES,
				)  		
			### Left Frame Contents: Assembly Language Code" 
			fixedFont = Pmw.logicalfont('Times', sizeIncr=-1, weight='bold')
			self.st = Pmw.ScrolledText(self.left_frame,
			labelpos = 'n',
			label_text='Assembly Language Code',
			label_font=('Times', 15),
			usehullsize = 1,
			hull_width = 320,
			hull_height = 500,
			text_wrap='none',
			text_font = fixedFont,

			text_padx = 4,
			text_pady = 4,
			)
			self.st.importfile('test.asm');
			self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)
			

			# Prevent users' modifying text and headers
			self.st.configure(
		    	text_state = 'disabled',

			)				

			### Right Frame Frame Contents: Registers and Memory Contents" 
			fixedFont = Pmw.logicalfont('Times', sizeIncr=-1, weight='bold')
			self.st = Pmw.ScrolledText(self.right_frame,
			labelpos = 'n',
			label_text='Registers & Memory Contents',
			label_font=('Times', 15),

			usehullsize = 1,
			hull_width = 320,
			hull_height = 500,
			text_wrap='none',
			text_font = fixedFont,

			text_padx = 4,
			text_pady = 4,
			)
			self.st.importfile('register.txt');
			self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)

			# Prevent users' modifying text and headers
			self.st.configure(
		    	text_state = 'disabled',

			)


			### Center Frame Contents: Registers and Memory Contents" 
			fixedFont = Pmw.logicalfont('Times', sizeIncr=-1, weight='bold')
			self.st = Pmw.ScrolledText(self.center_frame1,
			labelpos = 'n',
			label_text='RAM',
			label_font=('Times', 15),

			usehullsize = 1,
			hull_width = 320,
			hull_height = 500,
			text_wrap='none',
			text_font = fixedFont,

			text_padx = 4,
			text_pady = 4,
			)
			self.st.importfile('ram_write.txt');
			self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)

			# Prevent users' modifying text and headers
			self.st.configure(
		    	text_state = 'disabled',

			)
		
			### Center Frame Contents: Registers and Memory Contents" 
			fixedFont = Pmw.logicalfont('Times', sizeIncr=-1, weight='bold')
			self.st = Pmw.ScrolledText(self.center_frame2,
			labelpos = 'n',
			label_text='Program Memory & Opcodes',
			label_font=('Times', 15),

			usehullsize = 1,
			hull_width = 320,
			hull_height = 500,
			text_wrap='none',
			text_font = fixedFont,

			text_padx = 4,
			text_pady = 4,
			)
			self.st.importfile('opcode_write.txt');
			self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)

			# Prevent users' modifying text and headers
			self.st.configure(
		    	text_state = 'disabled',

			)			
			
			### Bottom Frame Contents: Registers and Memory Contents" 
			fixedFont = Pmw.logicalfont('Times', sizeIncr=-1, weight='bold')
			self.st = Pmw.ScrolledText(self.bottom_frame,
			labelpos = 'n',
			label_text='Log Messages',
			label_font=('Times', 15),

			usehullsize = 1,
			hull_width = 1400,
			hull_height = 500,
			text_wrap='none',
			text_font = fixedFont,

			text_padx = 4,
			text_pady = 4,
			)
			self.st.importfile('log_write.txt');
			self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)

			# Prevent users' modifying text and headers
			self.st.configure(
		    	text_state = 'disabled',

			)
			

	root = Tk()
	root.title('8051 Simulator')
	myapp = MyApp(root)
	root.mainloop()
