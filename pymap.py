# This is a nmap python version, still in construction.

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation toll")
print("----------------------------------------------")

ip_addr = input("Please enter the IP Address you want to scan: ")
print(f"The IP Address entered is: {ip_addr}")
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan\n""")
print(f"You have selected options: {resp}")

if resp == '1':
    print(f"Nmap Version: {scanner.nmap_version()}")
    scanner.scan(ip_addr, '1-1024', '-V -sS')
    print(scanner.scaninfo())
    print(f"Ip Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open ports: {scanner[ip_addr]['tcp'].keys()}")

elif resp == '2':
    print(f"Nmap Version: {scanner.nmap_version()}")
    scanner.scan(ip_addr, '1-1024', '-V -sU')
    print(scanner.scaninfo())
    print(f"Ip Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open ports: {scanner[ip_addr]['udp'].keys()}")

elif resp == '3':
    print(f"Nmap Version: {scanner.nmap_version()}")
    scanner.scan(ip_addr, '1-1024', '-V -sS -sC -A -O')
    print(scanner.scaninfo())
    print(f"Ip Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open ports: {scanner[ip_addr]['udp'].keys()}")

else:
    print("Please, enter a valid option")
    
    
