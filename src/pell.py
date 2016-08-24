from subprocess import *
import os
import sys
import getpass
import handler
import confloader

sh = handler.shell()
config = confloader.PellConfig()
config.parse_conf()

while 1:
    try:
        sh.userinput(config.getNode("appearance", "ps1"))
    except (KeyboardInterrupt, EOFError) as e:
        print("")
