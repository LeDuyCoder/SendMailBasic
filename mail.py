import smtplib, ssl

class Email():
    def __init__(self):
        self.sender = ""
        self.password = ""
        self.rect = ""
    
    def setMailSend(self, mail):
        self.rect = mail

    def loginMail(self, sender, password):
        self.sender = sender
        self.password = password
        
        context = ssl.create_default_context()
        self.email = smtplib.SMTP("smtp.gmail.com", 587)
        self.email.ehlo()  
        self.email.starttls(context=context)
        self.email.ehlo()
        login = self.email.login(self.sender, self.password)
        return login[0]
    
    def sendMail(self, title, content):
        if title[0:8] == "Subject: ":
            title = title[8:]
        message = f"""\
Subject: {title}

{content}
        """

        context = ssl.create_default_context()
        self.email = smtplib.SMTP("smtp.gmail.com", 587)
        self.email.ehlo()
        self.email.starttls(context=context)
        self.email.ehlo()
        login = self.email.login(self.sender, self.password)
        self.email.sendmail(self.sender, self.rect, message.encode("UTF-8"))