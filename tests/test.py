#!/usr/bin/python

import sys

sys.path.append('../')

from src.main import *
from src.header import *

from core.protocols import *
from core.xmpp import *
from core.web import *


def test():
    sys.stdout.write("Test successful!")