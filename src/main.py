
# import necessary libraries
from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

# define essential variables
## insert Twilio SID 
TWILIO_SID = ''   # DELETE BEFORE PULL REQUEST!!!!!
## insert Twilio Auth Token
TWILIO_AUTH_TOKEN = ''   #DELETE BEFORE PULL REQUEST!!!!!
## insert sender number aka twilio number
SENDER_NUMBER = '+123456789'   #DELETE BEFORE PULL REQUEST!!!!!
## insert recipient number aka verified recipient number in twilio
RECIPIENT_NUMBER = '+88888888'   #DELETE BEFORE PULL REQUEST!!!!!

# define otp_verifier frontend & simple backend class
class otp_verifier(Tk):
    def __init__(self):
        """frontend GUI"""
        super().__init__()
        self.geometry('600x550')
        self.resizable(False, False)
        self.iconbitmap('./images/otp_icon_213651.ico')
        self.title('OTP Verification System')
        # simple backend via Twilio
        self.n = random.randint(10000, 99999)
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.client.messages.create(to=[RECIPIENT_NUMBER],
                                    from_= SENDER_NUMBER,
                                    body=self.n)

    def Labels(self):
        self.c = Canvas(self, bg='grey', width=400, height=280)
        self.c.place(x=100, y=60)

        self.Login_Title = Label(self, text='OTP Verification', font='arial 20 bold', bg='lightgrey')
        self.Login_Title.place(x=210, y=90)

    def Entry(self):
        self.User_Name = Text(self, borderwidth=2, highlightthickness=0, wrap='word', width=29, height=2)
        self.User_Name.place(x=190, y=160)

    def Buttons(self):
        self.submitButtonImage = PhotoImage(file='./images/SUBMIT-BUTTON.png')
        self.submitButton = Button(self, image=self.submitButtonImage, command=self.checkOTP, border=0)
        self.submitButton.place(x=208, y=240)

        self.resendOTPImage = PhotoImage(file='./images/RESEND_OTP.png')
        self.resendOTP = Button(self, image=self.resendOTPImage, command=self.resendOTP, border=0)
        self.resendOTP.place(x=208, y=400)

    def checkOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, 'end-1c'))
            if self.userInput == self.n:
                messagebox.showinfo('showinfo', 'Login Success!')
                self.n = 'done'
            elif self.n == 'done':
                messagebox.showinfo('showinfo', 'Already used OTP!')
            else:
                messagebox.showinfo('showinfo', 'Wrong OTP!')
        except:
            messagebox.showinfo('showinfo', 'Invalid OTP!')

    def resendOTP(self):
        self.n = random.randint(10000, 99999)
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.client.messages.create(to=[RECIPIENT_NUMBER],
                                    from_= SENDER_NUMBER,
                                    body=self.n)


# Tkinter mainloop
if __name__ == '__main__':
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()