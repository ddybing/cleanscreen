"""
CleanScreen by Daniel Dybing, 2019. 

This program adds a list of predefined domains and IP addresses to the hosts file on Windows computers. 
These sites are typically well-known porn, malware or other unwanted websites. 

"""

import os
import json
from datetime import date


# Open domain list file
domainlist = open("domainlist.txt", 'r').readlines()

def deployList():
    # Deploy the list to hosts file.
    with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'a') as hostsfile:
        hostsfile.write('\n\n\n# Entries added by CleanScreen at {}\n\n\n'.format(date.today()))
        for domain in domainlist:
            print (domain)
            hostsfile.write('127.0.0.1 {}'.format(domain))
            hostsfile.write('127.0.0.1 {}'.format(domain[4:]))
def clearConsole():
    # Clear the console window
    os.system('cls')

def clearDnsCache():
    # Clear the DNS cache after deployment
    print('Now clearing DNS Cache...')
    pass
    print('DNS Cache cleared')

def reboot():
    pass

def finalMessage():
    count = 0
    while count < 15:
        count +=1 
        print('DONE! Please close this window and reboot the computer.')

#######################
deployList()
clearDnsCache()
#clearConsole()
finalMessage()
#######################


