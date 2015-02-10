"""
Skeleton for unit tests for the web-access module
"""

import socket
from threading import Thread
from netaddr import EUI, IPAddress

from web_access.models import Request
from web_access import utils as wa_utils
import unittest

def socket_listener(return_val):
    if not isinstance(return_val,list):
        raise ValueError('return_val should be a list')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((wa_utils.HOST, wa_utils.PORT))
    s.listen(1)
    conn, addr = s.accept()
    while 1:
        data = conn.recv(1024)
        if not data: break
        return_val.append(data)
    conn.close()

def set_up_data():
        # model1: Request
        # TODO: R=web_access.models.Request()
        return dict([
                     #('R', R)
                     ])

class WebAccessTests(unittest.TestCase):
    def setUp(self):
        pass

    # TODO
    #def test_models(self):
        #data_dicts = set_up_data()
        #self.assertTrue(web_access.models.Request(data_dicts['R']))

    # TODO
    #def test_for_foreignkey_in_Book_objects(self):
        #data_dicts = set_up_data()
        #self.assertEqual(data_dicts['R'].trainee, "test trainee name")

    # TODO
    #def test_unicode_functions(self):
        #data_dicts = set_up_data()
        #self.assertEqual('TODO', str(data_dicts['R']))

    def test_util_functions(self):
        """
        Tests for web_access.utils
        """
        
        # use the loopback address for the test
        wa_utils.HOST = '127.0.0.1'
        
        # start a thread to listen for the socket connection
        return_val=[]
        thread = Thread(target = socket_listener,args=(return_val,))
        thread.start()
        
        #call the function
        wa_utils.send_raw(EUI('00:00:00:00:00:00'),0)
        
        #wait for the server connection to close
        thread.join()
        result=''.join(return_val)
        self.assertEqual('00:00:00:00:00:00 0', result, 'send_raw failed! %s'
                         % (result))
        
        gateway = wa_utils.get_default_gateway()
        self.assert_(not gateway is None, "Unable to get default gateway to "\
                     "test get_mac")
        self.assert_(not wa_utils.get_mac(gateway) is None,
                     "get_mac failed!")

    def tearDown(self):
        pass

