import ctypes
import ctypes.util

libc_location_linux = ctypes.util.find_library("c")

# For Windows:
# libc_location_windows = ctypes.util.find_msvcrt()
# print(libc_location_windows)

print(libc_location_linux)

libc = ctypes.cdll.LoadLibrary(libc_location_linux)
libc.printf(b"Hello World\n")


