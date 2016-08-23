import subprocess 

while True:
    command = input("PELL~> ") # We can add a configurable prompt later
    subprocess.call(['/bin/' + command]) # Just a test, this lets you run things in /bin such as ls
