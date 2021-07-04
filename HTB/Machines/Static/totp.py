#TOTP Genrator using pyotp
# Date: 07/28/2021
#Author: Rahul Kalnarayan
#!/usr/bin/env python3
#Required pyotp [pip install pyotp]

import pyotp
from time import sleep

banner = """
████████╗ ██████╗ ████████╗██████╗ 
╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗
   ██║   ██║   ██║   ██║   ██████╔╝
   ██║   ██║   ██║   ██║   ██╔═══╝ 
   ██║   ╚██████╔╝   ██║   ██║     
   ╚═╝    ╚═════╝    ╚═╝   ╚═╝     
"""
#ecret_key = orxxi4c7orxwwzlo
#secret_key = str(raw_input("Enter Your Secret Key Here : "))

totp = pyotp.TOTP('orxxi4c7orxwwzlo')#(Replace your TOTP Private Key)
print (banner)
print("Wait while OTP genrate....")
sleep(5)
print ("Genrated OTP : " + totp.now())
print ("Note : OTP will valid only for 30 sec.")