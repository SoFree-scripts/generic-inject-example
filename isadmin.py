import ctypes, os, getpass
try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

print (is_admin)


print( getpass.getuser())


import platform
print ( platform.architecture() )


import ctypes.util

print (ctypes.util.find_library("kernel32"))