## Followed https://www.youtube.com/watch?v=tbhYxd2sfAE as a guide

import nmap

nm = nmap.PortScanner() # Initialize the PortScanner object

target = input("Enter target IP address: ")
options = input("Enter scan options (e.g., -sS for SYN scan): ")

nm.scan(target, arguments=options) # Perform the scan with the specified options

for host in nm.all_hosts(): # Iterate through all discovered hosts, the outer loop
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for pro in nm[host].all_protocols(): # Iterate through all protocols (e.g., tcp, udp) for each host, the inner loop
        print("Protocol: %s" % pro)
        port_info = nm[host][pro]
        for port, state in port_info.items(): # Iterate through all ports and their states for each protocol, inner most loop
            print("Port: %s\tState: %s" % (port, state['state']))
