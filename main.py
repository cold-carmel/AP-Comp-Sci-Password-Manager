import random
import time
import os
from getpass import getpass
import math

accLoop = True
asciiNums = []

def createAccount():
    print('Are you sure? Creation of a new account wipes all data of the previous account.')
    time.sleep(5)
    confirm = input('Type out: "New Account" (case-sensitive) in order to create a new accout\n')
    if confirm != 'New Account':
        return
    else:
        os.system('cls')
        os.remove('MasterPass.txt')
        os.remove('UserPassData.txt')
        os.remove('WebsiteData.txt')
        print('removed files')
        while True:
            newPass = getpass('Input the new Master Password for the new account:\n')
            os.system('cls')
            confirm = getpass('Confirm the Master Password by typing the same one again:\n')
            if newPass == confirm:
                open('MasterPass.txt', 'x')
                open('UserPassData.txt', 'x')
                open('WebsiteData.txt', 'x')
                mPass = open('MasterPass.txt', 'w')
                mPass.write(encrypt(newPass))
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
    return str(encryptData)
    
def decrypt(data):
    data = list(str(data))
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
        else:
            data.pop(0)
            data.pop(0)
            junk = False
    while len(joinList) > 0:
        asciiHex = joinList[0] + joinList[1]
        asciiVal = chr(int(asciiHex, 16))
        decryptedData = str(f'{decryptedData}{asciiVal}')
        joinList.pop(0)
        joinList.pop(0)
    return str(decryptedData)

def mainMenu():
  os.system('cls')
  while True:
    menuSelection = str(input('''What whould you like to do?
    [1] Create new entry
    [2] View an entry
    [3] Delete an entry
    [4] Exit
    '''))
    if menuSelection not in {'1', '2', '3', '4'}:
      print('Invalid input')
      continue
    elif menuSelection == '1':
      return 'new'
    elif menuSelection == '2':
      return 'view'
    elif menuSelection == '3':
      return 'delete'
    else:
      exit()
# login sequence   
 

while True:
    newAcc = input('Are you a new user?\n[Y] Yes, I am a new user\n[N] No, I am not a new user\n').lower()
    if newAcc not in {'y', 'n'}:
        print('invalid input')
        continue
    if newAcc == 'y':
        createAccount()
        continue
    if newAcc == 'n':
        break
os.system('cls')
while True:
  passInput = getpass('Please input the Master Password:\n')
  if passInput == decrypt(open('MasterPass.txt', 'r').read()):
    print('Logging in')
    time.sleep(0.5)
    print('Logging in.')
    time.sleep(0.5)
    print('Logging in..')
    time.sleep(0.5)
    print('Logging in...')
    time.sleep(0.5)
    break
  else:
    print('Incorrect password, please try again.')
    time.sleep(1)
    os.system('cls')
menuSelect = mainMenu()
if menuSelect == 'new':
  passDataRead = open('UserPassData.txt', 'r')
  print(passDataRead)
  passDatatemp = passDataRead.read()
  print(passDatatemp)
  passData = decrypt(passDatatemp)
  print(passData)
  passDict = eval(passData)
  print(passDict)
  print(f'passDataRead: {passData}')
  passDataWrite = open('UserPassData.txt', 'w')
  websiteInput = input('What website is the password for?\n').lower()
  websiteUsername = input(f'What is the Username for {websiteInput}?\n')
  websitePassword = getpass(f'What is the Password for {websiteInput}?\n')
  print(passData)
  print(passDict)
  newPassDict = {'website' : websiteInput,
                'username' : websiteUsername,
                'password' : websitePassword}
  passDict[websiteInput] = newPassDict
  print(passDict)
  passDataWrite.write(encrypt(str(passDict)))
  print('Password data saved!')
  time.sleep(2)
  mainMenu()

