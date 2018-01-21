from flask import Flask
from flask_mail import Mail
from flask_script import Shell,Manager
import os


app = Flask(__name__)
manager = Manager(app)
app.config['MAIL_SERVER']='smtp.sina.com'
app.config['MAIL_PORT']='25'
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')

mail=Mail(app)


def make_shell_context():
    return dict(app=app)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__=='__main__':
     manager.run()


