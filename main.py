import random
import time
import os
from getpass import getpass
import pyperclip as pc
import platform


accLoop = True
asciiNums = []


def createAccount():
    print('Are you sure? Creation of a new account wipes all data of the previous account.')
    time.sleep(3)
    confirm = input('Type out: "New Account" (case-sensitive) in order to create a new accout\n')
    if confirm != 'New Account':
        return
    else:
        clearConsole()
        os.remove('MasterPass.txt')
        os.remove('UserPassData.txt')
        print('removed files')
        while True:
            newPass = getpass('Input the new Master Password for the new account:\n', show='•')
            clearConsole()
            confirm = getpass('Confirm the Master Password by typing the same one again:\n', show='•')
            if newPass == confirm:
                open('MasterPass.txt', 'x')
                open('UserPassData.txt', 'x')
                mPass = open('MasterPass.txt', 'w')
                mPass.write(encrypt(newPass))
                passDataSetup = open('UserPassData.txt', 'w')
                passDataSetup.write('7b567d27')
                print('Success! New account created.')

                clearConsole()
                break
            else:
                clearConsole()
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
  clearConsole()
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
      print('viewing?')
      return 'view'
    elif menuSelection == '3':
      return 'del'
    else:
      exit()
  
def clearConsole():
  operatingSystem = platform.system()
  if operatingSystem == 'Windows':
    return os.system('cls')
  else:
    return os.system('clear')

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
clearConsole()
while True:
  passInput = getpass('Please input the Master Password:\n', show='•')
  if passInput == decrypt(open('MasterPass.txt', 'r').read()):
    clearConsole()
    print('Logging in')
    time.sleep(0.5)
    clearConsole()
    print('Logging in.')
    time.sleep(0.5)
    clearConsole()
    print('Logging in..')
    time.sleep(0.5)
    clearConsole()
    print('Logging in...')
    time.sleep(0.5)
    clearConsole()
    break
  else:
    print('Incorrect password, please try again.')
    time.sleep(1)
    clearConsole()

while True:
  menuSelect = mainMenu()
  clearConsole()
  if menuSelect == 'new':
    passDataRead = open('UserPassData.txt', 'r')
    passData = passDataRead.read()
    passData = decrypt(passData)
    passDict = eval(passData)
    while True:
      websiteInput = input('What Website is the password for?\n').lower()
      if websiteInput in passDict:
          print(f'The website {websiteInput} already has an input. If you would like to edit it, delete it and create a new one')
          time.sleep(3)
          break
      clearConsole()
      websiteUsername = input(f'What is the Username for {websiteInput}?\n')
      websitePassword = getpass(f'What is the Password for {websiteInput}?\n', show='•')
      newPassDict = {'website' : websiteInput,
                    'username' : websiteUsername,
                    'password' : websitePassword}
      passDict[websiteInput] = newPassDict
      passDataWrite = open('UserPassData.txt', 'w')
      passDataWrite.write(encrypt(str(passDict)))
      print('Password data saved!')
      time.sleep(2)
      passDataWrite.close()
      passDataRead.close()
      break
  if menuSelect == 'view':
    passDataRead = open('UserPassData.txt', 'r')
    passData = passDataRead.read()
    passData = decrypt(passData)
    passDict = eval(passData)
    websiteList = []
    for i in passDict:
       websiteList.append(i)
    while True:
      clearConsole()    
      print('Select one:')
      for num, website in enumerate(websiteList):
        print(f'[{num+1}] {website}')
      print('[B] Go back')
      menuSelect = input()
      if menuSelect == 'B':
        break
      try:
         menuSelect = int(menuSelect)
      except ValueError:
         print('Invalid input')
         continue
      if menuSelect > len(websiteList) or menuSelect < 1:
        print('Invalid Input')
        continue
      else:
        clearConsole()
        websitePassReq = websiteList[menuSelect-1]
        username = passDict[websitePassReq]['username']
        password = passDict[websitePassReq]['password']
        pc.copy(password)
        print(f'Website: {websitePassReq}\nUsername: {username}\nPassword: Copied to clipboard')
        print('Click enter when you are finished')
        getpass('')
        passDataRead.close()
        break
  if menuSelect == 'del':
    passDataRead = open('UserPassData.txt', 'r')
    passData = passDataRead.read()
    passData = decrypt(passData)
    passDict = eval(passData)
    websiteList = []
    for i in passDict:
       websiteList.append(i)
    while True:
      print('Select one to delete:')
      for num, website in enumerate(websiteList):
        print(f'[{num+1}] {website}')
      print('[B] Go back')
      menuSelect = input()
      if menuSelect == 'B':
        goBack = True
        break
      goBack = False
      try:
         menuSelect = int(menuSelect)
      except ValueError:
         print('Invalid input')
         continue
      if menuSelect > len(websiteList) or menuSelect < 1:
        print('Invalid Input')
        continue
      else:
        break
      if goBack == False:
        confirm = input('Are you sure you want to delete this? This action can not be undone.\n(Type "Yes" to confirm)\n')
        if confirm != 'Yes':
          print('Aborting...')
          time.sleep(2)
    else:
      websitePassDel = websiteList[menuSelect-1]
      del passDict[websitePassDel]
      passDataWrite = open('UserPassData.txt', 'w')
      passDataWrite.write(encrypt(str(passDict)))
      passDataWrite.close()
      print('Entry Deleted!')
      time.sleep(2)
    passDataRead.close()
