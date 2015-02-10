#!/usr/bin/python

################################################################################
# Hack to get this to work from command line for testing
################################################################################
if __name__== "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    settingsPath = "ap.settings.local"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settingsPath)
################################################################################

from netaddr import EUI, IPAddress, mac_unix
from ipware.ip import get_real_ip

import re
import socket
import subprocess

""" web-access utils.py
This module contains web-access request specific Python functions for
communicating with the firewall.

"""

# TODO: Move these either to the database or wherever app specific settings
# should be 
HOST = 'netguard' # hostname or ip address of the firewall (add to /etc/hosts)
PORT = 12345      # server port of application which listens for commands on the
    #             # firewall.

def send_raw(mac,minutes):
    """
    This function sends a string over a TCP socket to the firewall.
    """
    if not isinstance(mac,EUI):
        raise ValueError("mac expected to be EUI")
    if not isinstance(minutes,int):
        raise ValueError("minutes expected to be int")
    mac.dialect = mac_unix
    mac.dialect.word_fmt = '%.2X' 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    s.connect((HOST, PORT))
    s.sendall('%s %d' % (str(mac),minutes))
    s.close()

def get_ip(request):
    ip = get_real_ip(request)
    return None if ip is None else IPAddress(ip)

def get_mac(ipaddress):
    """
    This function
    """
    if not isinstance(ipaddress,IPAddress):
        raise ValueError("expected ipaddress to be of type netaddr.IPAddress")
    p = subprocess.Popen(['arp','-n',str(ipaddress)])
    p.join()
    p = subprocess.Popen(['arp','-n',str(ipaddress)], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    matches = re.search('\s([a-zA-Z0-9]{1,2}(?::[a-zA-Z0-9]{1,2}){5})\s',result,re.MULTILINE)
    if matches is None:
        return None
    mac = EUI(matches.group(1))
    mac.dialect = mac_unix
    mac.dialect.word_fmt = '%.2X' 
    return mac

def get_default_gateway():
    """
    this function was written to make it possible to test get_mac
    """
    p = subprocess.Popen(['ip','route'], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    matches = re.search('^default via (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*$',result,re.MULTILINE)
    if matches is None:
        return None
    return IPAddress(matches.group(1))
    
if __name__== "__main__":
    gateway = get_default_gateway()
    if not gateway is None:
        print str(get_mac(gateway))
