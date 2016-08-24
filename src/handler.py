# Shell class
import subprocess
import os
import sys
import getpass
import readline
import glob


class shell():

    def __init__(self):
        self.reserved = ["exit", "cd", "export"]

    def getFormattedCWD(self):
        out = os.getcwd()
        out = out.replace(os.path.expanduser("~"), "~")
        return out

    def userinput(self, ps1):
        if getpass.getuser() in ["root", "toor"]:
            usrsym = "#"
        else:
            usrsym = "$"
        # Formats {0} to the current directory and {1} to the current user.
        prompt = ps1.format(self.getFormattedCWD(), usrsym)
        data = input(prompt)
        self.process(data)

    def process(self, data):
        tokens = data.split()
        if(len(tokens) <= 0):  # If there is any input.
            return  # Exit function.

        # If command is not reserved for the shell.
        if(tokens[0] not in self.reserved):
            try:
                subprocess.call(tokens)  # Runs program.
            except FileNotFoundError:  # If it cannot find the program.
                print("File or command not found.")
            return

        if(tokens[0] == "cd"):
            if(len(tokens) >= 2):
                try:
                    # PEP8 made sure this variable name was awful
                    # It also made this one line into 2
                    hd = tokens[1].replace("~", os.path.expanduser("~"))
                    os.chdir(hd)
                except:
                    print("Directory does not exist.")
            else:
                os.chdir(os.path.expanduser("~"))
        elif(tokens[0] == "exit"):
            sys.exit(0)

        class Test:

            def __init__(self, data):
                self.data = data
