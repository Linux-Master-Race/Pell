#Shell class
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
        out = out.replace("/home/" + getpass.getuser(), "~")
        return out

    def userinput(self, ps1):
        print(getpass.getuser())
        if getpass.getuser() in ["root", "toor"]:
            usrsym = "#"
        else:
            usrsym = "$"
        prompt = ps1.format(self.getFormattedCWD(), usrsym) #Formats {0} to the current directory and {1} to the current user.
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
