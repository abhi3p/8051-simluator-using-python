#!/usr/bin/python
from Read_Code import *
from runner import *
from Write_files import *
from GUI import *

filename='test-div-mul.asm'
Read_Code(filename)
runner()
Write_files()
GUI(filename)
