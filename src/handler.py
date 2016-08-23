#Shell class
import subprocess
import os
import sys
import getpass
from rl import completer
from rl import generator
import readline
import glob

class shell():
    def __init__(self):
        self.reserved = ["exit", "cd", "export"]

    def complete(self, text):
        for x in self.reserved:
            yield x
        for directory in os.environ.get("PATH").split(':'):
            directory = os.path.expanduser(directory)
            if os.path.isdir(directory):
                for name in os.listdir(directory):
                    if name.startswith(text):
                        if(os.access(os.path.join(directory, name), os.R_OK|os.X_OK)):
                            yield name


    def getFormattedCWD(self):
        out = os.getcwd()
        out = out.replace("/home/" + getpass.getuser(), "~")
        return out

    def userinput(self, ps1):
        prompt = ps1.format(self.getFormattedCWD(), getpass.getuser()) #Formats {0} to the current directory and {1} to the current user.
        completer.completer = generator(self.complete)
        completer.parse_and_bind('TAB: complete')
        data = input(prompt)
        self.process(data)

    def process(self, data):
        tokens = data.split()
        if(len(tokens) <= 0): #If there is any input.
            return #Exit function.
        if(tokens[0] not in self.reserved): #If command is not reserved for the shell.
            try:
                subprocess.call(tokens) #Runs program.
            except FileNotFoundError: #If it cannot find the program.
                print("File or command not found.")
            return

        if(tokens[0] == "cd"):
            if(len(tokens) >= 2):
                try:
                    os.chdir(tokens[1].replace("~", "/home/" + getpass.getuser()))
                except:
                    print("Directory does not exist.")
            else:
                os.chdir("/home/" + getpass.getuser())
        elif(tokens[0] == "exit"):
            sys.exit(0)
        class Test:
            def __init__(self, data):
                self.data = data
