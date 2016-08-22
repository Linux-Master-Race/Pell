import subprocess
import os
import sys

reserved = ["set", "exit"]
run = True
while(run):
    data = input("pell {0}$ ".format(os.getcwd()))
    tokens = data.split()
    if(tokens[0] not in reserved):
        print(subprocess.check_output(tokens).decode('utf-8'))
    else:
        if(tokens[0] == "exit"):
            sys.exit("exit")
