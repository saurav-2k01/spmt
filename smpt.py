#SPMT
#importing all necessary modules.
import pandas as pd
import numpy as np
import random
from pyfiglet import Figlet

#defineing variables for later uses.
name = []
username = []
account = []
password = []
passwordlen = []
raw = {}

# figlet lets you style the font
f = Figlet(font="slant")
def get_info():
    _name = input("Name =>> ")
    name.append(_name)
    _username = input("UserName =>> ")
    username.append(_username)
    _account = input("Account =>> ")
    account.append(_account)
""""defining paswd_gen function to generate random password from all possible string to make it strong."""
def paswd_gen():
    plength = int(input("enter the password length =>> "))
    paswd = ''
    for i in range(plength):
        paswd += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_-")
    password.append(paswd)
    passwordlen.append(len(paswd))
# function deco is defined to decorate the console
def deco():
    print("============================================================================================================================"
          "============================================================================================================================")
"""" The main SPMT function is defined to call all defined function and run the program """
def SPMT():
    deco()
    get_info()
    paswd_gen()
    deco()
    raw["Name"] = name
    raw["UserName"] = username
    raw["account"] = account
    raw["Password"] = password
    raw["Passwordlen"] = passwordlen
"""" data_ function is defined to conver all data to data frame to tore it in a managed way in file"""
def data_():
    df = pd.DataFrame(raw)
    return df
""""df_to_dl is defined to save all data list in a file"""
def df_to_dl():
    file = input("enter file name to save data =>> ".title())
    datalist = data_().to_numpy()
    np.savetxt(file, datalist,fmt="%s")
    print("data saved succesfully in", file,"!")
deco()
print(f.renderText("Welcome To SPMT !!!"))
deco()

"""" all together all the functions run here """
while True:
    SPMT()
    exit = input("enter \"n\" to exit and \"y\" to continue =>> ".title())
    if exit == "n":
        print(data_())
        deco()
        print("Thanks for using SPMT !")
        df_to_dl()
        deco()
        break
    elif exit == "y":
        continue
    else:
        print("Invalid Input \n\n")
        deco()
        print("Thanks for using SPMT !")
        df_to_dl()
        print(data_())
        break

