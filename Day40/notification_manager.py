import smtplib
import os

class NotificationManager:
    def __init__(self,toemail):
        self.email = os.environ.get("EMAIL")
        self.password = os.environ.get("PASS")
        self.toemail = toemail
    
    def sendemail(self,mess):
        with smtplib.SMTP("smtp.gmail.com", port = 587) as con:
            con.starttls()
            con.login(self.email,self.password)
            con.sendmail(from_addr=self.email,to_addrs=self.toemail,msg=mess)
            print("Send successfully")

if __name__ == "__main__":
    noti = NotificationManager("hynuiux@gmail.com")
    noti.sendemail("Hello, this is test")