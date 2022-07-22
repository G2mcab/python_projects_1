#generate password
import random

lower_case='abcdefghijklmnopqrstuvwxyz'
upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number='0123456789'
symbols='!@#$%^&*()-<>/\?'

Use_for=lower_case+upper_case+number+symbols

password_length=int(input("Enter the length of password you want to generate:- "))

password="".join(random.sample(Use_for,password_length))

print("The password generated is:- ", password)
