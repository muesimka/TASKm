import os
import getpass
import socket
import sys
import platform
import datetime

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]

now = datetime.datetime.now()
sys_in = sys.path
print(f"{os_name} \n "
      f"{os_version} \n "
      f"{os_arch} \n "
      f"{now.year} \n "
      f"{now.month} \n "
      f"{now.day} \n "
      f"{now.hour} \n ")

os_processor = platform.processor()
print(f"{os_processor} \n ")

ip_address = socket.gethostbyname(socket.gethostname())
print(f"{ip_address} \n")

username = getpass.getuser()
print(f"{username} \n")