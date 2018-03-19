import nmap
import sys

nm = nmap.PortScanner()
target = str(sys.argv)
nm.scan(target, arguments='-O -sV')
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for os_class in nm[host]['osmatch']:
        for os in os_class['osclass']:
            print('OS : %s, \tver: %s' % (os['osfamily'], os['osgen']))
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto) 
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s \tservice: %s'  % (port, nm[host][proto][port]['state'], nm[host][proto][port]['product']))



