#!/usr/bin/env python3
import string
import secrets
import time
import os

#Color codes 
os.system("color")
COLOR = {
     "BLUE": "\033[94m",
     "GREEN": "\033[92m",
     "RED": "\033[91m",
     "ENDC": "\033[0m",
     "BOLD": "\033[1m",
     "YELLOW": "\033[93m",
     "CYAN": "\033[96m",
     "GREY": "\033[1;30m",
     "LIGHT_WHITE": "\033[1;37m",
     "BROWN": "\033[0;33m",
     "PURPLE": "\033[0;35m"
}

#Banner
print(COLOR["CYAN"], """
████████╗██╗░░██╗███████╗██████╗░░█████╗░███╗░░██╗██╗░░░██╗████████╗░█████╗░███████╗
╚══██╔══╝██║░░██║██╔════╝██╔══██╗██╔══██╗████╗░██║██║░░░██║╚══██╔══╝██╔══██╗╚════██║
░░░██║░░░███████║█████╗░░██║░░██║██║░░██║██╔██╗██║██║░░░██║░░░██║░░░██║░░██║░░░░██╔╝
░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░██║██║╚████║██║░░░██║░░░██║░░░██║░░██║░░░██╔╝░
░░░██║░░░██║░░██║███████╗██████╔╝╚█████╔╝██║░╚███║╚██████╔╝░░░██║░░░╚█████╔╝░░██╔╝░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░░░░╚═╝░░░░╚════╝░░░╚═╝░░░
     █▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
     █▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄""" + COLOR["YELLOW"] + " v2.0", COLOR["ENDC"])
print(COLOR["GREY"], """
==============================================[""" + COLOR["LIGHT_WHITE"] + "AUTHOR - " +  COLOR["BROWN"] + "Selroy.S" + COLOR["GREY"] +"]===================", COLOR["ENDC"])

time.sleep(1)
print(" ")

#First question until the user co-operates by providing a Int :)      .....(Colored Question)
print(COLOR["PURPLE"], "How many Characters Password you want?", COLOR["ENDC"])
while True:
     try:
          print(COLOR["LIGHT_WHITE"],"Type:",COLOR["ENDC"], end="")
          passwd_len = int(input())
          break
     except:
          print("", end="")
          print(COLOR["RED"], "Only Numbers are Valid!!\n", COLOR["ENDC"])
print(" ")

#Second question   ......(Colored Question)
print(COLOR["PURPLE"], "Choose how many passwords you want to generate with the length that was specified above?", COLOR["ENDC"])
print(COLOR["BLUE"] + "1. " + COLOR["LIGHT_WHITE"] + "One Password\n" + COLOR["BLUE"] + "2. " + COLOR["LIGHT_WHITE"] + "Five Passwords\n" + COLOR["BLUE"] + "3. " + COLOR["LIGHT_WHITE"] + "Ten Passwords\n" + COLOR["BLUE"] + "4. " + COLOR["LIGHT_WHITE"] + "Fifteen Passwords", COLOR["ENDC"])

#Option Number from User    .......(Colored)
print(COLOR["BLUE"], "Type Option Number:",COLOR["ENDC"], end="")
passwd_choice = input()
print("\n")

#Option 1
if passwd_choice == str(1):
     characters = string.ascii_letters + string.digits + string.punctuation
     passwd = ''.join((secrets.choice(characters) for i in range(passwd_len)))
     passwords = ("Password: " + passwd)
     print("Password: " + COLOR["GREEN"] + passwd, COLOR["ENDC"])
     print("\n")
     print(COLOR["YELLOW"], "Above is your " + str(passwd_len) + " characters Password :)\n", COLOR["ENDC"])

#Option 2
elif passwd_choice == str(2):
     passwords = ""
     for i in range(5):
          characters = string.ascii_letters + string.digits + string.punctuation
          passwd = ''.join((secrets.choice(characters) for i in range(passwd_len)))
          passwords += (str(i+1) +") " + "Password: " + passwd + "\n")
          print(str(i+1) +") " + "Password: " + COLOR["GREEN"] + passwd, COLOR["ENDC"])
     print("\n")
     print(COLOR["YELLOW"], "Above is your " + str(passwd_len) + " characters Passwords :)\n", COLOR["ENDC"])
    
#Option 3
elif passwd_choice == str(3):
     passwords = ""
     for i in range(10):
          characters = string.ascii_letters + string.digits + string.punctuation
          passwd = ''.join((secrets.choice(characters) for i in range(passwd_len)))
          passwords += (str(i+1) +") " + "Password: " + passwd + "\n")
          print(str(i+1) +") " + "Password: " + COLOR["GREEN"] + passwd, COLOR["ENDC"])
     print("\n")
     print(COLOR["YELLOW"], "Above is your " + str(passwd_len) + " characters Passwords :)\n", COLOR["ENDC"])

#Option 4
elif passwd_choice == str(4):
     passwords = ""
     for i in range(15):
          characters = string.ascii_letters + string.digits + string.punctuation
          passwd = ''.join((secrets.choice(characters) for i in range(passwd_len)))
          passwords += (str(i+1) +") " + "Password: " + passwd + "\n")
          print(str(i+1) +") " + "Password: " + COLOR["GREEN"] + passwd, COLOR["ENDC"])
     print("\n") 
     print(COLOR["YELLOW"], "Above is your " + str(passwd_len) + " characters Passwords :)\n", COLOR["ENDC"])

#For Invalid Option
else:
     print(COLOR["RED"], "INVALID OPTION!!!", COLOR["ENDC"])
     print("\n")
     print(COLOR["YELLOW"], """IMP: Use the options which have showed above,
     for e.g = type ' 1 ' (To choose the first option) or 
               type ' 2 ' (To choose the second option)""", COLOR["ENDC"])
     time.sleep(5)
     exit()

#Boolean Option for Saving File   .........(Colored)
print(COLOR["LIGHT_WHITE"], "Do you want to Save the File?" + " (" + COLOR["GREEN"] + "Y" + COLOR["LIGHT_WHITE"] + "/" + COLOR["RED"] + "n" + COLOR["LIGHT_WHITE"] + "): ",COLOR["ENDC"] , end="")
answer = input()

#If User wants to save the file
if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes":
     directory_path = os.getcwd()
     file_name = input("Name the Password file: ")
     saving_file = os.path.join(directory_path, file_name+".txt")
     file = open(saving_file, "w")
     file.write(passwords)
     file.close()
     print("\n")
     print("Your File saved at this Directory: " + COLOR["GREEN"] + directory_path + COLOR["ENDC"] + "\n" + "Saved File Name: " + COLOR["GREEN"] + file_name + ".txt", COLOR["ENDC"])

#Else the Answer is No or invalid input
else:
     print(COLOR["BOLD"], COLOR["RED"], "      File Saving Declined!!\n", COLOR["ENDC"])
     print(COLOR["CYAN"], "------------ Thankyou!! Byee ^_^ -------------", COLOR["ENDC"])

time.sleep(5)
exit()