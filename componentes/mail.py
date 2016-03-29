import sendgrid
import os


class Mail:
    def __init__(self, to, subject, msg):
        self.to = to
        self.subject = subject
        self.msg = msg

    def send(self):
        sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_KEY', ''))
        message = sendgrid.Mail()
        message.add_to(self.to)
        message.set_subject(self.subject)
        message.set_html(self.msg)
        message.set_text(self.msg)
        message.set_from('BuscoAyuda <buscoayuda@buscoayuda.com>')
        print (sg.send(message))
