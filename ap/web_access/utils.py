#!/usr/bin/python

from netaddr import EUI, mac_unix

import socket

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
