#Write many messages when we click enter
import os
os.environ['DISPLAY'] = ':0'

import pyautogui as spam
import time

limit=input("Enter no. of messages: ")
msg=input("Enter the message you want to send: ")

i=0
time.sleep(5)

while i<int(limit):
    spam.typewrite(msg)
    spam.press('Enter')
    i+=1