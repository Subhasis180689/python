import os
cwd = os.getcwd()
cwd
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print (f)
