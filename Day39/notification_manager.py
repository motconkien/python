import smtplib

class NotificationManager:
    def __init__(self,toemail):
        self.email = "hoanghuyen.hh20897@gmail.com"
        self.password = "vxcmrxhyoavmhsap"
        self.toemail = toemail
    
    def sendemai(self,mess):
        with smtplib.SMTP("smtp.gmail.com", port = 587) as con:
            con.starttls()
            con.login(self.email,self.password)
            con.sendmail(from_addr=self.email,to_addrs=self.toemail,msg=mess)
            print("Send successfully")