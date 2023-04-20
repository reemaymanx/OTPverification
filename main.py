import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# create color
background_colour = '#000000'
f1 = '#FFEBCD'
f2 = '#ffffff'

# window
window = tk.Tk()
window.title("")
window.geometry('500x450')
window.configure(bg=background_colour)


# frames
frame_line = tk.Frame(window, width=700, height=20, bg="maroon")
frame_line.grid(row=0, column=0)
frame_body = tk.Frame(window, width=700, height=590, bg=f2)
frame_body.grid(row=1, column=0)

# frame body
otp_region = tk.Label(frame_body, text="OTP Verification", height=1, font=('Ivy 18 bold'), bg=f2)
otp_region.place(x=145, y=10)

##email region
input_email_name = tk.Label(frame_body, text="Enter Email", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
input_email_name.place(x=185, y=55)
input_email = tk.Entry(frame_body,width=30)
input_email.pack()
input_email.place(x=155, y=85)


## sent otp
enter_otp = tk.Label(frame_body, text="Enter sent OTP", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
enter_otp.place(x=170, y=160)
input_otp = tk.Entry(frame_body, width=30)
input_otp.pack()
input_otp.place(x=155, y=190)


mails= ['reayza15@example.com','sync@example.com','hudson@example.com']
def check_email(username):
    validuser= False
    for mail in mails:
        if mail == username:
            validuser =True
            break
    return validuser


otp = random.SystemRandom().randint(100000, 999999)
key = otp
def sms():
    check = check_email(input_email.get())
    if (check == True):
     screen =Toplevel(window)
     screen.title("sms message")
     screen.geometry('300x300')
     screen.configure(bg="white")
     key1= str(key)
     statement = 'Your OTP Verification is '+ key1
     tk.Label(screen, text= statement, bg="white", font=('arial 15') ).pack(expand=True)
     screen.mainloop()
    else:
        messagebox.showinfo("showinfo","Invalid Email")



def check_otp():

    if key == int(input_otp.get()):
        messagebox.showinfo("showinfo","Successful Login")
    else:
        messagebox.showinfo("showinfo","Invalid Login, Wrong OTP")



##subit button
submit_button = tk.Button(frame_body, text="submit", bd=2, font="arial 10", fg="black", bg="silver", height=1,
                          command=sms)
submit_button.place(x=210, y=130)

# check button
check_button = tk.Button(frame_body, text="Check OTP", bd=1, font="arial 10", fg="black", bg="silver", height=1,command=check_otp)
check_button.place(x=195, y=240)


# resend button
check_button = tk.Button(frame_body, text="Resend OTP", bd=1, font="arial 10", fg="grey", bg="silver", height=1,command=sms)
check_button.place(x=192, y=280)
window.mainloop()
