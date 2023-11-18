import colorama
from colorama import Fore, Back, Style
import subprocess
import requests
import threading
import nmap
import time

colorama.init(autoreset=True)

import subprocess

def print_title():
    version = "Version 1.0.0"
    title = '''
    |  __ \  __ \               ___|           _)       |   
    | |   | |   |  _ \   __| \___ \   __|  __| | __ \  __|  
    | |   | |   | (   |\__ \       | (    |    | |   | |   
    |____/ ____/ \___/ ____/ _____/ \___|_|   _| .__/ \__|  
                                                _|         
    Creator : dinerbone._ 

    This is a program for ethical hacking on websites. Version 1.0.0.
    '''
    print(Back.BLACK + Fore.CYAN + title)
    print(Back.BLACK + Fore.RED + version)

def DDOS():
    print_title()

    url = input("Url --> ")
    # Sending multiple requests using threading
    def Ddos():
        requests.get(url)
    threads = []
    for _ in range(3):  # Sending three requests concurrently
        thread = threading.Thread(target=Ddos)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def Scan():
    ip = input("IP --> ")
    nmScan = nmap.PortScanner()

    # Scan ports in the range 0-8080
    nmScan.scan(ip, '0-8080')

    # Print the scan results
    for host in nmScan.all_hosts():
        print('Host : %s (%s)' % (host, nmScan[host].hostname()))
        print('State : %s' % nmScan[host].state())
        for proto in nmScan[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            ports = list(nmScan[host][proto].keys())
            ports.sort()
            for port in ports:
                print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
principal_title = '''
                __                  _______            __   _______         .__                                                       .__                       __         .__   
  _____ _____  |  | _______ _______ \   _  \___  __  _/  |_ \   _  \   ____ |  |   ______            ____ ___  _________   ___________|__| _____   ____   _____/  |______  |  |  
 /     \\__  \ |  |/ /\__  \\_  __ \/  /_\  \  \/ /  \   __\/  /_\  \ /  _ \|  |  /  ___/  ______  _/ __ \\  \/  /\____ \_/ __ \_  __ \  |/     \_/ __ \ /    \   __\__  \ |  |  
|  Y Y  \/ __ \|    <  / __ \|  | \/\  \_/   \   /    |  |  \  \_/   (  <_> )  |__\___ \  /_____/  \  ___/ >    < |  |_> >  ___/|  | \/  |  Y Y  \  ___/|   |  \  |  / __ \|  |__
|__|_|  (____  /__|_ \(____  /__|    \_____  /\_/     |__|   \_____  /\____/|____/____  >           \___  >__/\_ \|   __/ \___  >__|  |__|__|_|  /\___  >___|  /__| (____  /____/
      \/     \/     \/     \/              \/                      \/                 \/                \/      \/|__|        \/               \/     \/     \/          \/    
Dev : Marak0v
Version 1.0.2-Open Source
-experimental branch
'''
print(Back.BLACK + Fore.CYAN + principal_title)
menu = {
    '1': "DDOS",
    '2': "Nmap",
    '3': "Credit",
    '4': "under contruction",
    '5': "Exit"  # Added comma here
}

while True:
    options = list(menu.keys())
    options.sort()
    for entry in options:
        print(entry, menu[entry])

    selection = input("Please Select: ")
    if selection == '1':
        DDOS()
    elif selection == '2':
        Scan()
    elif selection == '3':
        print('''
Code made by Makar0v
Contact me on discord dinerbone._
It's a simple Tools box made in around
2 hours with a 20-minute break, so it's not perfect,
but you can use the code in your project :)

Ps: There can be some error
It's an open-source program,
so you can check for any
rats or malware. I spent some time coding this,
so please don't assume it's a RAT because it's not. Thank you!
        ''')
        time.sleep(10)
    elif selection == '4':
        print("sorry nothing here")
        time.sleep(10)
    elif selection == '5':
        break
    else:
        print("Unknown Option Selected!")
