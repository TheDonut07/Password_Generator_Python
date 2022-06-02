#!/usr/bin/env python3

import string
import secrets
import time
import os

print("""
████████╗██╗░░██╗███████╗██████╗░░█████╗░███╗░░██╗██╗░░░██╗████████╗░█████╗░███████╗
╚══██╔══╝██║░░██║██╔════╝██╔══██╗██╔══██╗████╗░██║██║░░░██║╚══██╔══╝██╔══██╗╚════██║
░░░██║░░░███████║█████╗░░██║░░██║██║░░██║██╔██╗██║██║░░░██║░░░██║░░░██║░░██║░░░░██╔╝
░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░██║██║╚████║██║░░░██║░░░██║░░░██║░░██║░░░██╔╝░
░░░██║░░░██║░░██║███████╗██████╔╝╚█████╔╝██║░╚███║╚██████╔╝░░░██║░░░╚█████╔╝░░██╔╝░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░░░░╚═╝░░░░╚════╝░░░╚═╝░░░
     █▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
     █▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
                                                                 AUTHOR - Selroy.S""")

time.sleep(1)
print(" ")

#First question
passwd_len = int(input("How many charaters Password you want?\n" + "Type: "))

print(" ")

#Second question
print("Choose how many passwords you want to generate with the length that was specified above?")
print("""1. One Password
2. Five Passwords
3. Ten Passwords
4. Fifteen Passwords""")
passwd_choice = (input("Type Option number: "))
print("\n")

#Option 1
if passwd_choice == str(1):
     characters = string.ascii_letters + string.digits + string.punctuation
     passwd = ''.join((secrets.choice(characters) for i in range(passwd_len)))
     passwords = ("Password: " + passwd)
     print(passwords)
     print("\n")
     print("Above is your " + str(passwd_len) + " characters Password :)\n")

#Option 2
elif passwd_choice == str(2):
     passwords = ""
     for i in range(5):
          characters = string.ascii_letters + string.digits + string.punctuation
          passwd = ''.join((secrets.choice(characters) for i in range(passwd_len)))
          passwords += (str(i+1) +") " + "Password: " + passwd + "\n")
          print(str(i+1) +") " + "Password: " + passwd)
     print("\n")
     print("Above is your " + str(passwd_len) + " characters Passwords :)\n")
    
#Option 3
elif passwd_choice == str(3):
     passwords = ""
     for i in range(10):
          characters = string.ascii_letters + string.digits + string.punctuation
          passwd = ''.join((secrets.choice(characters) for i in range(passwd_len)))
          passwords += (str(i+1) +") " + "Password: " + passwd + "\n")
          print(str(i+1) +") " + "Password: " + passwd)
     print("\n")
     print("Above is your " + str(passwd_len) + " characters Passwords :)\n")

#Option 4
elif passwd_choice == str(4):
     passwords = ""
     for i in range(15):
          characters = string.ascii_letters + string.digits + string.punctuation
          passwd = ''.join((secrets.choice(characters) for i in range(passwd_len)))
          passwords += (str(i+1) +") " + "Password: " + passwd + "\n")
          print(str(i+1) +") " + "Password: " + passwd)
     print("\n") 
     print("Above is your " + str(passwd_len) + " characters Passwords :)\n")

else:
     print("INVALID OPTION!!!")
     print("\n")
     print("""IMP: Use the options which have showed above,
     for e.g = type ' 1 ' (To choose the first option) or 
               type ' 2 ' (To choose the second option)""")
     time.sleep(5)
     exit()

answer = input("Do you want to save the file? (Y/n): ")
#If user want to save the file
if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes":
     directory_path = os.getcwd()
     file_name = input("Name the Password file: ")
     saving_file = os.path.join(directory_path, file_name+".txt")
     file = open(saving_file, "w")
     file.write(passwords)
     file.close()
     print("\n")
     print("Your File saved at this Directory: " + directory_path + "\n" + "Saved File Name: " + file_name + ".txt")
else:
     print("\n")
     print("File Saving Declined!!")
     print("Thankyou!! Byee ^_^")

time.sleep(5)
exit()