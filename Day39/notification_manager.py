import smtplib
import os

class NotificationManager:
    def __init__(self,toemail):
        self.email = os.environ.get("MYEMAI")
        self.password = os.environ.get("MYPASS")
        self.toemail = toemail
    
    def sendemai(self,mess):
        with smtplib.SMTP("smtp.gmail.com", port = 587) as con:
            con.starttls()
            con.login(self.email,self.password)
            con.sendmail(from_addr=self.email,to_addrs=self.toemail,msg=mess)
            print("Send successfully")