path.append('src/')
from mainLib import *
from time import sleep
import os

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

print installer_head
print G + "brut3k1t installer! To start, press Enter. Will create a symlink for easier access" + W
raw_input()

print O + "[*] Updating..." + W
sleep(1.5)
os.system("sudo apt-get update")
print O + "[*] Installing essential packages... [*]" + W
sleep(1.5)
os.system("sudo apt-get install python python-pip python-setuptools python-selenium firefoxdriver")
print O + "[*] Installing pip modules [*]" + W
sleep(1.5)
os.system("sudo pip install -r requirements.txt")
