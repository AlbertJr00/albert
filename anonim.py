import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("XD.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/AlbertJr00/files/main/anonim_enc.cpython-311.so -o")
    if path.isfile("dump.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/AlbertJr00/files/main/anonim_enc.cpython-311.so -o anonim_enc.cpython-311.so")
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
os.system('chmod 777 XD && ./XD')

