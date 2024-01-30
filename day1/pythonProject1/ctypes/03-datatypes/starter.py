from ctypes import *
from ctypes.util import find_library

libc = cdll.LoadLibrary(find_library('c'))

# Fail - pow wants doubles
print(libc.pow(2, 3))

# Works - use c_double, returns c_double
libc.pow.restype = c_double
libc.pow.argtypes = [c_double, c_double]
print(libc.pow(c_double(2), c_double(3)))

