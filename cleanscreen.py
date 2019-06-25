"""
CleanScreen by Daniel Dybing, 2019. 

This program adds a list of predefined domains and IP addresses to the hosts file on Windows computers. 
These sites are typically well-known porn, malware or other unwanted websites. 

"""
import subprocess
import os
import sys
import shutil
import json
from datetime import date


# Open domain list file
domainlist = open("domainlist.txt", 'r').readlines()

def deployList():
    # Deploy the list to hosts file.
    with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'a') as hostsfile:
        hostsfile.write('\n\n\n# Entries added by CleanScreen at {}\n\n\n'.format(date.today()))
        for domain in domainlist:
            hostsfile.write('127.0.0.1 {}'.format(domain))
            hostsfile.write('127.0.0.1 {}'.format(domain[4:]))
        

def clearConsole():
    # Clear the console window
    os.system('cls')

def enableIIS():
        process = subprocess.Popen('powershell.exe Enable-WindowsOptionalFeature -online -FeatureName IIS-WebServerRole -norestart')
        process.wait()
        print('Added IIS-WebServerRole feature!')
        process2 = subprocess.Popen(['powershell', 'New-WebBinding', '-Name', '"Default Web Site"',
        '-IP', '"*"', '-Port', '443', '-Protocol', 'https'])
        process2.wait()
        print('Added IIS binding for HTTPS')

def finalMessage():
        input('DONE! Press ENTER to exit.')


def copyLocalSite():
        shutil.copyfile('index.html', 'C:\\inetpub\\wwwroot\\index.html')
        print('index-file copied')
#######################
deployList()
enableIIS()
copyLocalSite()
clearConsole()
finalMessage()
#######################

