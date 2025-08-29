#   Brady Gerard
#   8/29
#   Secure login program. Uses set username and password
#   Username: Jimbo
#   Password: P4LmTR3E!!!!!!!

from sha256py import Sha256
import os
import time
import sys
from termcolor import colored, cprint
import msvcrt
import hmac
import string

# Alows for limiting the size of user input
# This section aided by ChatGPT
# "how to stop users from inputing too many characters in python" "how to stop users from inputing certain charaters"
# Code produced by the two prompts were combined and altered to work for this situation
ALLOWED_CHARS = string.ascii_letters + string.digits + "_" + "!" + "@" + "#" + "$" + "*"

def get_filtered_input(prompt, max_length):
    print(prompt, end='', flush=True)
    input_chars = []

    while True:
        ch = msvcrt.getwch()

        if ch in ('\r', '\n'):
            break
        elif ch == '\b':  
            if input_chars:
                input_chars.pop()
                print('\b \b', end='', flush=True)
        elif ch in ALLOWED_CHARS:
            if len(input_chars) < max_length:
                input_chars.append(ch)
                print(" ", end='', flush=True)

    print()  
    return ''.join(input_chars)

# Hashes
username_hash = "1d078c5ead2dd5e262fab30187c07b3894fac0151d511bf8724c801ada620ec8"
password_hash = "9b9a99fe072d11f5614d1edbf4f52cfe697b2215c4d72dc192c143d0ec560530"

# Input loop
attempts = 0
while attempts < 9:
    
    # Get username
    os.system('cls')
    cprint("Alowed Characters: A-Z a-z 1-9 _!@#$*", "magenta")
    cprint("Input is hidden", "magenta")
    username = Sha256(get_filtered_input("Username: ", 15)).hexdigest()

    # Get password
    os.system('cls')
    cprint("Alowed Characters: A-Z a-z 1-9 _!@#$*", "magenta")
    cprint("Input is hidden", "magenta")
    password = Sha256(get_filtered_input("Password: ", 25)).hexdigest()

    # Check username and password
    os.system('cls')
    if(hmac.compare_digest(password, password_hash) and hmac.compare_digest(password, password_hash)):
        cprint("Login Successful", "green")
        time.sleep(3)
        break
    else:
        cprint("Username and/or Password Incorect", "red")
        attempts += 1
    time.sleep(2)

    # Time out for too many attempts
    os.system('cls')
    if(attempts == 3):
        cprint("Try Again in 5 Minuts", "red")
        cprint("Attempts Will Resume Shortly", "red")
        time.sleep(300)
    elif(attempts == 6):
        cprint("Try Again in 30 Minuts", "red")
        cprint("Attempts Will Resume Shortly", "red")
        time.sleep(1800)
    elif(attempts == 9):
        cprint("Account Locked", "red")
        time.sleep(5)
        os.system('cls')
        sys.exit()
    

# Clean up
os.system('cls')