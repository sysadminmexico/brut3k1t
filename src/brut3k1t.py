#!/usr/bin/python
from src.main import *
from src.header import *

from core.protocols import *
from core.xmpp import *
from core.web import *

class Bruteforce:
    def __init__(self, service, username, wordlist, address, port, delay):
        
        self.service = service
        self.username = username
        self.wordlist = wordlist
        self.address = address 
        self.port = port
        self.delay = delay

    '''    
    def proxyServer(self, proxy):
        proxy = open(proxy, 'r')
        for i in proxy.readlines():
            proxyaddr = i.strip("\n")
            try:
                proxies = {"http" : "http://" + str(proxyaddr) }
                r = requests.get("http://google.com", proxies=proxies)
                print G + "[v]" + W + (" Proxy %s is found! " % proxyaddr)
            except requests.exceptions.ProxyError:
                print R + "[X]" + W + (" Proxy %s is NOT found!" % proxyaddr)
                
            proxy.close()'''
    
