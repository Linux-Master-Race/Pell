from subprocess import *
import os
import sys
import getpass
import handler
from confloader import PellConfig

if __name__ == "__main__":
    sh = handler.shell()
    config = PellConfig()

    while 1:
        try:
            sh.userinput(config.get_option("prompt", "pell {0} {1} "))
        except (KeyboardInterrupt, EOFError) as e:
            print("")
