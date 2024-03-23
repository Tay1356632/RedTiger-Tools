from Config.Util import *
from Config.Config import *
import subprocess
import time
import socket
Title("Ip Pinger")

hostname = input(color.RED + f"\n{INPUT} Ip -> " + color.RESET)
try:
    port_input = input(color.RED + f"{INPUT} Port (enter for default) -> " + color.RESET)
    if port_input.strip():
        port = int(port_input)
    else:
        port = 80  
    
    bytes_input = input(color.RED + f"{INPUT} Bytes (enter for default) -> " + color.RESET)
    if bytes_input.strip():
        bytes = int(bytes_input)
    else:
        bytes = 64
except:
    ErrorNumber()

def ping_ip(ip_address, port, bytes):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        start_time = time.time() 
        sock.connect((ip_address, port))
        data = b'\x00' * bytes
        sock.sendall(data)
        end_time = time.time() 
        elapsed_time = (end_time - start_time) * 1000 
        print(f'{color.RED}Ping to {color.WHITE}{hostname}{color.RED}: time={color.WHITE}{elapsed_time:.2f}ms{color.RED} port={color.WHITE}{port}{color.RED} bytes={color.WHITE}{bytes}{color.RED} status={color.WHITE}succeed{color.RED}')
    except:
        elapsed_time = 0
        print(f'{color.RED}Ping to {color.WHITE}{hostname}{color.RED}: time={color.WHITE}{elapsed_time}ms{color.RED} port={color.WHITE}{port}{color.RED} bytes={color.WHITE}{bytes}{color.RED} status={color.WHITE}fail{color.RED}')

while True:
    ping_ip(hostname, port, bytes)