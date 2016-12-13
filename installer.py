from time import sleep
import os, sys


# Global variables for color
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

installer_head = """
  ___________________
< brut3k1t installer! >
  -------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/
                 ||----w |
                 ||     ||
    """

# Unix/Linux-based distros
def linux_build():

    print O + "[*] Updating..." + W
    sleep(1.5)
    os.system("sudo apt-get update")
    print O + "[*] Installing essential packages... [*]" + W
    sleep(1.5)
    os.system("sudo apt-get install python python-pip python-setuptools python-selenium firefoxdriver")
    print O + "[*] Installing pip modules [*]" + W
    sleep(1.5)
    os.system("sudo pip install -r requirements.txt")
    print G + "[!] Done installing dependences! [!]" + O
    print"[*] Make symlinks and installation directories [*]"
    os.system("mkdir /opt/brut3k1t && cp ~/Code/brut3k1t /opt/brut3k1t")
    os.symlink("/usr/bin/brut3k1t", "/opt/brut3k1t/brut3k1t.py")
  
    
# OS X / Darwin
def osx_build():
    print O + "[*] Installing Homebrew [*]" + W 
    sleep(1.5)
    os.system("""/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" """)
    os.system("brew install python selenium-server-standalone")
    os.system("sudo wget https://bootstrap.pypa.io/get-pip.py")
    os.system ("sudo python get_pip.py")
    print O + "[*] Installing pip modules"
    sleep(1.5)
    os.system("sudo pip install -r requirements.txt")
    print G + "[!] Done installing dependences! [!]" + O
    print"[*] Make symlinks and installation directories [*]"
    os.system("mkdir /opt/brut3k1t")
    os.symlink("/usr/bin/brut3k1t", "/opt/brut3k1t/brut3k1t.py")

print installer_head

while True:
    print "Select an Operating System"
    print "=============================="
    print "(1) Unix/Linux-based Distros"
    print "(2) Mac OS X / Darwin"
    print "=============================="
    getos = raw_input()
    if getos == "1":
        linux_build()
    elif getos == "2":
        osx_build()

    print G + "brut3k1t installer! To start, press Enter. Will create a symlink for easier access" + W
    raw_input()


    