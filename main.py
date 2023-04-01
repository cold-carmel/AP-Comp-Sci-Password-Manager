import random
import time
import os
from getpass import getpass
import math

accLoop = True
asciiNums = []

def createAccount():
    print(f'Are you sure? Creation of a new account wipes all data of the previous account.')
    time.sleep(5)
    confirm = input('Type out: "New Account" (case-sensitive) in order to create a new accout\n')
    if confirm != 'New Account':
        return
    else:
        os.system('cls')
        # os.remove('MasterPass.txt')
        # os.remove('UserPassData.txt')
        # os.remove('WebsiteData.txt')
        print('removed files')
        while True:
            newPass = input('Input the new Master Password for the new account:\n')
            os.system('cls')
            confirm = input('Confirm the Master Password by typing the same one again:\n')
            if newPass == confirm:
                mPass = open('Masterpass.txt', 'w')
                mPass.write(newPass)
                print('Success! New account created.')

                os.system('cls')
                break
            else:
                os.system('cls')
                print('The passwords do not match up.')
                continue

def encrypt(data):
    asciiList = []
    for i in data:
        asciiList.append(hex(ord(i)).removeprefix('0x'))
        asciiList.append(chr(random.randint(71, 122)))
        asciiList.append(chr(random.randint(71, 122)))
    encryptData = ''.join(asciiList)
    return encryptData
    
def decrypt(data):
    data = list(data)
    junk = False
    joinList = []
    decryptedData = ''
    while len(data) > 0:
        if junk == False:
            joinList.append(data[0])
            joinList.append(data[1])
            data.pop(0)
            data.pop(0)
            junk = True
        if junk == True:
            data.pop(0)
            data.pop(0)
            junk = False
    while len(joinList) > 0:
        asciiHex = joinList[0] + joinList[1]
        asciiVal = chr(int(asciiHex, 16))
        decryptedData = str(f'{decryptedData}{asciiVal}')
        joinList.pop(0)
        joinList.pop(0)
    return decryptedData

# login sequence
while True:
    newAcc = input('Are you a new user?\n[Y] Yes, I am a new user\n[N] No, I am not a new user\n')
    newAcc.lower()
    if newAcc not in {'y', 'n'}:
        print('invalid input')
        continue
    if newAcc == 'y':
        createAccount()
        continue
    if newAcc == 'n':
        break
passInput = input('Please input the Master Password:\n')
masterPass = encrypt(passInput)
print(masterPass)
tempDecrypt = decrypt(masterPass)
print(tempDecrypt)
