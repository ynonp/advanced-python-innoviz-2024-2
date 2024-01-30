from ctypes import *
from ctypes.util import find_library
import time

# Windows:
#libc = cdll.msvcrt
#print(libc.rand())

# Load ANY c DLL:
# dll = cdll.LoadLibrary(/path/to/DLL)

# Linux:
libc_location = find_library('c')
print(libc_location)

libc = cdll.LoadLibrary(libc_location)
