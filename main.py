import random
import time
import os
import pwinput
import getpass
import pyperclip as pc
import platform

accLoop = True
asciiNums = []

def createAccount():
    print('Are you sure? Creation of a new account wipes all data of the previous account.') # this confirms with the user they want to make a new account
    time.sleep(2)
    confirm = input('Type out: "New Account" (case-sensitive) in order to create a new account\n') # type in confirmation
    if confirm != 'New Account':
        clearConsole()
        return
    else:
        clearConsole()
        if os.path.exists('MasterPass.txt') == True: # if the file exists, it removes it
          os.remove('MasterPass.txt')
        if os.path.exists('UserPassData.txt') == True: # if the file exists, it removes it
          os.remove('UserPassData.txt')
        while True:
            newPass = pwinput.pwinput('Input the new Master Password for the new account:\n') # creates the password for the new account
            clearConsole()
            confirm = pwinput.pwinput('Confirm the Master Password by typing the same one again:\n') # confirms the password with the user
            if newPass == confirm: # if both inputs match, write the encrypted master password to the MasterPass.txt file
                open('MasterPass.txt', 'x') # creates a new file used to store the Master Password
                open('UserPassData.txt', 'x') # creates a new file used to store the password data
                mPass = open('MasterPass.txt', 'w') # opens the 'MasterPass.txt' file
                mPass.write(encrypt(newPass)) # writes the encrypted Master Password to the file
                passDataSetup = open('UserPassData.txt', 'w') # opens the 'UserPassData.txt' file
                passDataSetup.write('7b567d27') # this string of text adds the necessary data to the UserPassData.txt file to make an encrypted dictionary
                print('Success! New account created.')
                time.sleep(2)
                clearConsole()
                break
            else:
                clearConsole()
                print('The passwords do not match up.') # if the confirm password doesn't match, try again
                continue

def encrypt(data):
    asciiList = []
    for i in data:
        asciiList.append(hex(ord(i)).removeprefix('0x')) # grabs the number of the character in the ascii table, convert the number it it's hex equivalent, removes the 0x that comes with converting to the hex, and adds that value to a list
        asciiList.append(chr(random.randint(71, 122))) # adds 2 random characters to further enhance the encryption method
        asciiList.append(chr(random.randint(71, 122)))
    encryptData = ''.join(asciiList) # joins all the characters in the list together into a string
    return str(encryptData)
   
def decrypt(data):
    data = list(str(data)) # takes the input of data (ex: 70KH61qf73bh73_d) and turns it into a list (ex: ['7','0','K','H','6','1','q','f','7','3','b','h','7','3','_','d'])
    junk = False
    realData = []
    decryptedData = ''
    while len(data) > 0: # runs until there are no items left in the data list
        if junk == False:
            realData.append(data[0]) # grabs the first value of the data (ex: '7') and adds it to a new list to return the decrypted data
            realData.append(data[1]) # grabs the second value of the data (ex: '0') and adds it to a new list to return the decrypted data
            data.pop(0) # removes the 2 values it just added to the new list from data
            data.pop(0) # contines the comment above
            junk = True # flips the mode from grab real data to remove junk data
        else:
            data.pop(0) # removes the 2 junk data characters from the data list
            data.pop(0) # continues the comment above
            junk = False # flips the mode from remove junk data to grab real data
    while len(realData) > 0:
        asciiHex = realData[0] + realData[1] # grabs the first 2 characters of the real data list
        asciiVal = chr(int(asciiHex, 16)) # converts the hex value into an int, grabs the ascii value corresponding with the int
        decryptedData = str(f'{decryptedData}{asciiVal}') # creates a string combining the previous decrypted data and the new decrypted data
        realData.pop(0) # removes the 2 characters the program just handled from the list
        realData.pop(0)
    return str(decryptedData)

def mainMenu(): # this is the function that brings the user to the selection menu to actually do things in the program
  while True:
    clearConsole()
    menuSelection = str(input('''What would you like to do?
    [1] Create new entry
    [2] View an entry
    [3] Delete an entry
    [4] Exit
    '''))
    if menuSelection not in {'1', '2', '3', '4'}: # if an answer that isn't 1, 2, 3, or 4 is picked, it prompts the user back to the selection menu
      print('Invalid input')
      time.sleep(1.5)
      continue
    elif menuSelection == '1':
      return 'new'
    elif menuSelection == '2':
      return 'view'
    elif menuSelection == '3':
      return 'del'
    else:
      exit()
 
def clearConsole(): # this function clears the console for Windows, macOS, and Linux
  operatingSystem = platform.system()
  if operatingSystem == 'Windows':
    return os.system('cls')
  else:
    return os.system('clear')

def openPassData():
  passDataRead = open('UserPassData.txt', 'r') # opens the UserPassData.txt file
  passData = passDataRead.read() # assigns the data in the list to 'passData'
  passData = decrypt(passData) # decrypts the data to be usable
  passDataRead.close() # closes the file to prevent possible corruption
  return eval(passData) # turns the decrypted data into a nested dictionary with all the password entries


clearConsole()
while True: # starts the login sequence
    newAcc = input('Are you a new user?\n[Y] Yes, I am a new user\n[N] No, I am not a new user\n').lower()
    if newAcc not in {'y', 'n'}:
        print('Invalid Input')
        time.sleep(1)
        clearConsole()
        continue
    if newAcc == 'y':
        createAccount()
        continue
    if newAcc == 'n':
        break
clearConsole()
while True:
  passInput = pwinput.pwinput('Please input the Master Password:\n')
  if passInput == decrypt(open('MasterPass.txt', 'r').read()): # if the input matches up with the decrypted data from the MasterPass.txt file, the user is granted access
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
  menuSelect = mainMenu() # the selection for the main menu is defined by the mainMenu function
  clearConsole()
  if menuSelect == 'new': # if the user selects the 'Create New Entry' option, this segment under the if statement is ran
    passDict = openPassData() # grabs the data from the UserPassData.txt file, decrypts it, and formats it into a nested dictionary
    while True:
      websiteInput = input('What Website is the password for?\n').lower() # queries for the website of the password, makes the input all lowercase for no case-sensitivity
      if websiteInput in passDict: # if the inputted password already has an entry, it tells the user that an existing entry with that same name already exists
          print(f'The website {websiteInput} already has an input. If you would like to edit it, delete it and create a new one')
          time.sleep(3)
          break
      websiteUsername = input(f'What is the Username for {websiteInput}?\n') # grabs the username for the entry
      websitePassword = pwinput.pwinput(f'What is the Password for {websiteInput}?\n') # grabs the password in a protected manner ('password' would show up in console as '********')
      newPassDict = {'website' : websiteInput,
                    'username' : websiteUsername,
                    'password' : websitePassword} # a new nested dictionary is made with the data inputted by the user
      passDict[websiteInput] = newPassDict # the new dict is inserted into the existing dict
      passDataWrite = open('UserPassData.txt', 'w')
      passDataWrite.write(encrypt(str(passDict))) # the new dict is written in the 'UserPassData.txt' file
      print('Password data saved!')
      time.sleep(2)
      passDataWrite.close()
      break
  if menuSelect == 'view': # if the user selects the 'View an entry' option, this segment under the if statement is ran
    passDict = openPassData() # grabs the data from the UserPassData.txt file, decrypts it, and formats it into a nested dictionary
    websiteList = [] # defines the website List for use later
    for i in passDict:
       websiteList.append(i) # grabs all the entry websites from the passwords
    while True:
      clearConsole()    
      print('Select one:') # selection menu for viewing a password
      for num, website in enumerate(websiteList): # prints the website and a number assigned with it to make a convenient selection system
        print(f'[{num+1}] {website}')
      print('[B] Go back')
      menuSelect = input().lower()
      if menuSelect == 'b': # the user can exit by typing 'b'
        break
      try: # if the input isn't a number, it returns 'Invalid Input'
         menuSelect = int(menuSelect)
      except ValueError:
         print('Invalid input')
         continue
      if menuSelect > len(websiteList) or menuSelect < 1: # if the input is a number not listed on the menu, it returns 'Invalid Input'
        print('Invalid Input')
        continue
      else:
        clearConsole()
        websitePassReq = websiteList[menuSelect-1]
        username = passDict[websitePassReq]['username'] # defines the username for the selected entry
        password = passDict[websitePassReq]['password'] # defines the password for the selected entry
        pc.copy(password) # copies the password to the clipboard instead of showing it to the user
        print(f'Website: {websitePassReq}\nUsername: {username}\nPassword: Copied to clipboard') # displays the requested information
        print('Click enter when you are finished')
        getpass.getpass('') # this is just to detect when a user presses enter without showing what the user typed into the console
        break
  if menuSelect == 'del': # if the user selects the 'Delete an entry' option, this segment under the if statement is ran
    passDict = openPassData() # grabs the data from the UserPassData.txt file, decrypts it, and formats it into a nested dictionary
    websiteList = [] # defines the website list for use later
    for i in passDict:
       websiteList.append(i) # adds all the websites from the password entries to the list
    while True:
      print('Select one to delete:') # selection menu for viewing a password
      for num, website in enumerate(websiteList):  # prints the website and a number assigned with it to make a convenient selection system
        print(f'[{num+1}] {website}')
      print('[B] Go back')
      menuSelect = input().lower()
      if menuSelect == 'b': # the user can exit by typing 'b'
        goBack = True # if the user needs to go back
        break
      goBack = False
      try:  # if the input isn't a number, it returns 'Invalid Input'
         menuSelect = int(menuSelect)
      except ValueError:
        print('Invalid input')
        time.sleep(1)
        continue
      if menuSelect > len(websiteList) or menuSelect < 1: # if the input is a number not listed on the menu, it returns 'Invalid Input'
        print('Invalid Input')
        time.sleep(1)
        continue
      else:
        break
    if goBack == False:
      confirm = input('Are you sure you want to delete this? This action can not be undone.\n(Type "Yes" to confirm)\n') # confirms with the user that they want to delete the entry
      if confirm != 'Yes': # if the user doesn't say yes, the entry isn't deleted
        print('Aborting...')
        time.sleep(2)
      else:
        websitePassDel = websiteList[menuSelect-1] # grabs the name of the website being deleted
        del passDict[websitePassDel] # deletes the entry from the dictionary
        passDataWrite = open('UserPassData.txt', 'w') # opens the 'UserPassData.txt' file
        passDataWrite.write(encrypt(str(passDict))) # encrypts the new dictionary and stores it in the 'UserPassData.txt' file
        passDataWrite.close() # closes the file
        print('Entry Deleted!')
        time.sleep(2)