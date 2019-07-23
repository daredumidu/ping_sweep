import os

ip_range = raw_input("Enter IP range (eg: 192.168.1.0/24):")

#os.system('nmap -sn -PS ' + ip_range)
#os.system('nmap -sn -PS -oG - ' + ip_range)

""" nmap command for ping sweep
nmap -sn -PS 192.168.1.0/24
nmap -sn -PS -oG - 192.168.1.0/24 | awk '{print $2}' 	 
nmap -sn -PS -oG - 192.168.1.0/24 | awk '{print $2}' > result.txt"""

os.system('nmap -sn -PS -oG - %s | awk \'{print $2}\' > hosts.txt' % ip_range)
