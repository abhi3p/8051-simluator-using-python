#!/usr/bin/python
from Read_Code import *
from runner import *
from Write_files import *
from GUI import *
import sys

filename = sys.argv[1]
Read_Code(filename)
runner()
Write_files()
GUI(filename)
