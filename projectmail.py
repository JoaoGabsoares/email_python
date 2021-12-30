import os
import smtplib
from email.message import EmailMessage
import time
import getpass

# configurar email, senha
email_adress = input('Digite seu email: ')
email_password = getpass.getpass('Digite sua senha: ')
time.sleep(3)

# criar email
msg = EmailMessage()
msg['From'] = email_adress
msg['to'] = input('Digite o Destinátario: ')
msg['Subject'] = input('Digite o assunto: ')
msg.set_content(input('Digite sua Mensagem: '))

time.sleep(5)

# enviar email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_adress, email_password)
    smtp.send_message(msg)
