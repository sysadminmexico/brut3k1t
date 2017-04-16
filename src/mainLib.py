 # -*- coding: utf-8 -*-
################################################################
# TODO: Seperate method to read and seperate words in wordlist.
# TODO: Wordlist generator
# TODO: More protocols. Fix twitter bruteforce.
# TODO: problems persist when using different SMTP ports.
################################################################

'''
mainLib.py - Core methods and global variables that occur after user parsing and initial
             output.
'''


# Comes with Python. These should be core libraries.

import socket, os, requests
from time import sleep
from random import *
from subprocess import call

# New stuff! Should be installed thru requirements.txt.

import smtplib, argparse, paramiko, mechanize
from xmpp import *
from ftplib import FTP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf8')

################################################################
# Global variables and configurations!!
################################################################

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


def get_args():
    parser = argparse.ArgumentParser(description='Server-side bruteforce module written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', help="Provide a service being attacked. Several protocols and services are supported")
    required.add_argument('-u', '--username', dest='username', help='Provide a valid username for service/protocol being executed')
    required.add_argument('-w', '--wordlist', dest='password', help='Provide a wordlist or directory to a wordlist')
    parser.add_argument('-a', '--address', dest='address', help='Provide host address for specified service. Required for certain protocols')
    parser.add_argument('-p', '--port', type=int, dest='port', help='Provide port for host address for specified service. If not specified, will be automatically set')
    parser.add_argument('-d', '--delay', type=int, dest='delay', help='Provide the number of seconds the program delays as each password is tried')
    parser.add_argument('--proxy', dest='proxy', help="Providing a proxy for anonymization and avoiding time-outs")

    args = parser.parse_args()

    man_options = ['username', 'password']
    for m in man_options:
        if not args.__dict__[m]:
            print R + "[!] You have to specify a username AND a wordlist! [!]" + W
            exit()

    service = args.service
    username = args.username
    wordlist = args.password
    address = args.address
    port = args.port
    delay = args.delay
    proxy = args.proxy

    if delay is None:
        delay = 1


    return service, username, wordlist, address, port, delay, proxy

def proxyServer(proxy):
    proxy = open(proxy, 'r')
    for i in proxy.readlines():
        proxyaddr = i.strip("\n")
        try:
            proxies = {"http" : "http://"+str(proxyaddr)}
            r = requests.get("http://google.com", proxies=proxies)
            print G + "[✓]" + W + (" Proxy %s is found! " % proxyaddr)
        except requests.exceptions.ProxyError:
            print R + "[X]" + W + (" Proxy %s is NOT found!" % proxyaddr)

        proxy.close()
