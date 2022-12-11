import os

import re
import sys
from os import getenv
from resources.data import DEV
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()




API_ID = int(getenv("API_ID", "26318388"))
API_HASH = getenv("API_HASH", "a5c549d2420fa6a7d7edbf08736f5a78")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/8a35c510bf511986cb563.jpg")

#CLIENT SESSION

STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "AQB1OwsBSItHHOG0G94zdT2_smfIcTkekJcQTcsIzgkU_Xhh9eXNZfac9f6vebkH0Aq7EH4tQ0GJ-4Fvn2mECm7c6M86UUx5wPqhqYwBmj9rQiDreNRKX8ADdOin-vk5-tr-_mkvmpKjusk_8MHFp5odVk8UpW7hBJDKcvrG08ILDiQO782EKks0uzKYIrp04TsagWd52V39WRyM2Oq9Q_c7t3ex0Jtq9nxBG80jPI2ezctEHakzGmFYZiCEZII2-1UdkE1jrean2eD-qe36K5VUnteFX_lB490ADW1jssrN7pUh7JcOLqlqG5sX-IcM_E2tehS-qPEeSwJaoVHE0Y-9fENxtAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
STRING8 = getenv("STRING_SESSION8", None)
STRING9 = getenv("STRING_SESSION9", None)
STRING10 = getenv("STRING_SESSION10", None)
OWNER_ID = int(getenv("OWNER_ID", "5656382791")) 
SUDO_USERS = getenv("SUDO_USER", "5656382791") 


"""
------------------------------DON'T EDIT AFTER THIS LINE---------------------------------------
"""

# CONVERTING STR TO INT

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list




# SUDO SETUP

SUDOERS = []

if SUDO_USERS:
    SUDOERS = make_int(SUDO_USERS)

DEVS = DEV
for i in DEVS:
    SUDOERS.append(i)
    SUDOERS.append(OWNER_ID)
