 # -*- coding: utf-8 -*-
import socket, os, requests
from time import sleep
from random import *
from subprocess import call

import smtplib, argparse, paramiko, mechanize, telnetlib, ftplib
from xmpp import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

reload(sys)
sys.setdefaultencoding('utf8')

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

TIMEOUT = "Please wait a few minutes before you try again."

header = """

  _                _   _____ _    _ _
 | |__  _ __ _   _| |_|___ /| | _/ | |_
 | '_ \| '__| | | | __| |_ \| |/ / | __|
 | |_) | |  | |_| | |_ ___) |   <| | |_
 |_.__/|_|   \__,_|\__|____/|_|\_\_|\__|
    Written by: @ex0dus-0x
 """


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
            
        proxy.close()
