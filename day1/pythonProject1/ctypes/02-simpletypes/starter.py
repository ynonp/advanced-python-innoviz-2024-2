from ctypes import *
from ctypes.util import find_library

# Update this line to work on Windows
libc = cdll.LoadLibrary(find_library("c"))

# None -> NULL
print(libc.time(None))

# Bytes -> const char *
libc.printf(b"Hello %d %d world\n", 10, 20)

# int -> long/int/short
libc.srand(10)



