#Shell class
import subprocess
import os
import sys
import getpass
import readline
import glob
import tty
import termios

class char_handle:
    #Reads terminal input and returns the first char. allowing individual keypresses to 
    #register rather than full strings.
    def get_char(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def process_char(self, char):
        #This code goes through chars indiviually. 
        #Allowing things like tab completion and any plugin to work in individual keypresses.

        if char == "\x7f":
            return("backspace")
        if char == "\r":
            return("newline")
        else:
            return('non_interrupt')

class shell():

    def __init__(self):
        self.reserved = ["exit", "cd", "export"]
        self.return_chars= ['\r', '\n']
        self.operators=['>', '>>', '|', '<', '&', ';']
        self.unix_char=char_handle()
    def getFormattedCWD(self):
        out = os.getcwd()
        out = out.replace("/home/" + getpass.getuser(), "~")
        return out

    def userinput(self, ps1):
        prompt = ps1.format(self.getFormattedCWD(), getpass.getuser()) #Formats {0} to the current directory and {1} to the current user.
        data=[]
        #Clears any printed items on the line.
        print("\033[K", end='\r', flush=True)
        #prints out the prompt.
        print(prompt, end='\r', flush=True)
        while 1:
            #Get keypress
            keypress=self.unix_char.get_char()      
            #Evaluate keypress to see if anything needs to be done
            retcode = self.unix_char.process_char(keypress)
            if retcode == "backspace":              
                #Removes last char in data as long as it's not empty
                if len(data) > 0:
                    del data[-1]
            if retcode == "newline":
                #on enter, process the command
                print("") # Forces newline for readability
                self.process(''.join(data))
                return(1)
            #if keypress not needed to interrupt, add to data
            if retcode == "non_interrupt":
                data.append(keypress)
            print("\033[K", end='\r', flush=True)
            #prints clears line and prints data
            print(
                prompt
                + ''.join(data), end='\r', flush=True
                )


    def execute(self, command, mode='default'):
        try:
            if mode == '|':
                #Executes command and redirects io, returns p for further use
                p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
                return p
            if mode == '>':
                pass
            else:
                subprocess.call(command) #Runs program.
        except FileNotFoundError: #If it cannot find the program.
            print("File or command not found.")
            return


    def process(self, data):
        tokens = data.split()
        if(len(tokens) <= 0): #If there is any input.
            return #Exit function.

        if(tokens[0] not in self.reserved): 
            #If command is not reserved for the shell.
            command=[] #building the command array for execution
            for token in tokens:
                if(token not in self.operators):
                    command.append(token)
                else:
                    pass
            self.execute(command)
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
