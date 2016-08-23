import subprocess
import os
import sys
import getpass
import handler


sh = handler.shell()




while 1:
    try:
        sh.userinput("pell {0} $ ")
    except (KeyboardInterrupt, EOFError) as e:
        print("")
