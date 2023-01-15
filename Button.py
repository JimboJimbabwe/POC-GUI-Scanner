import os

import tkinter



from tkinter import *
from tkinter.ttk import *


os.system("./writescript.sh")



# Creating a tkinter window

root = Tk()

root.title("HTTP Scanner")


# Initialize tkinter window with dimensions 300 x 250

root.geometry('800x800')

# Define a command for button

NTLM1 = PhotoImage(file = "/home/kali/Desktop/Icons/house.png")
SMB1 = PhotoImage(file = "/home/kali/Desktop/Icons/smb.png")
Sec1 = PhotoImage(file = "/home/kali/Desktop/Icons/sechead.png")
SQL1 = PhotoImage(file = "/home/kali/Desktop/Icons/syringe.png")
WAF1 = PhotoImage(file = "/home/kali/Desktop/Icons/waf.png")
CSRF1 = PhotoImage(file = "/home/kali/Desktop/Icons/pen.png")

NTLM2 = NTLM1.subsample(6, 6)
SMB2 = SMB1.subsample(9, 9)
Sec2 = Sec1.subsample(9, 9)
SQL2 = SQL1.subsample(9, 9)
WAF2 = WAF1.subsample(24, 24)
CSRF2 = CSRF1.subsample(4, 4)


def run_smb():

    os.system("cd ScriptRepo && ./smb1.sh")



def run_csrf():

	os.system("cd ScriptRepo && ./csrf.sh")



def run_ntlm():

	os.system("cd ScriptRepo && ./NTLM.sh")



def run_sql():

	os.system("cd ScriptRepo && ./SQL.sh")



def run_sec():

	os.system("cd ScriptRepo && ./Secheaders.sh")


def run_waf1():

	os.system("cd ScriptRepo && ./WAFFINGER.sh")



# Creating a Button

btn = tkinter.Button(root, text='smb scan', image = SMB2, compound = LEFT, height= 75, width=240, command=run_smb)

btn2 = tkinter.Button(root, text='CSRF Scan', image = CSRF2, compound = LEFT, height= 75, width=240, command=run_csrf)

btn3 = tkinter.Button(root, text='Enum NTLM', image = NTLM2, compound = LEFT, height= 75, width=240, command=run_ntlm)

btn4 = tkinter.Button(root, text='SQL scan', image = SQL2, compound = LEFT, height= 75, width=240, command=run_sql)

btn5 = tkinter.Button(root, text='Scan Security Headers', image = Sec2, compound = LEFT, height= 75, width=240, command=run_sec)

btn6 = tkinter.Button(root, text='WAF Fingerprint scan',  image = WAF2, compound = LEFT, height= 75, width=240, command=run_waf1)



# Set the position of button to coordinate (100, 20)

btn.grid(row=1,column=0)

btn2.grid(row=2,column=0)

btn3.grid(row=3,column=0)

btn4.grid(row=4, column=0)

btn5.grid(row=5, column=0)

btn6.grid(row=6, column=0)

root.mainloop()

