# Código Original -> Curso
# # email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv
load_dotenv()

def sendMail(html, asunto, para):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = asunto
    msg['From'] = os.getenv("SMTP_USER")
    msg['To'] = para
    
    msg.attach(MIMEText(html, 'html'))
    
    try:
        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
        server.sendmail(os.getenv("SMTP_USER"), para, msg.as_string())
        server.quit()
    except smtplib.SMTPResponseException as e:
        print("error envió mail")





# # Código mejorado
# # email
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import os
# from dotenv import load_dotenv

# # Cargar variables de entorno
# load_dotenv()

# def sendMail(html, asunto, para):
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = asunto
#     msg['From'] = os.getenv("SMTP_USER")
#     msg['To'] = para
    
#     msg.attach(MIMEText(html, 'html'))
    
#     try:
#         server = smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT")))
#         server.starttls()  # Asegura la conexión si el servidor lo requiere
#         server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
#         server.sendmail(os.getenv("SMTP_USER"), para, msg.as_string())  # Corrección aquí
#         server.quit()
#         print("Correo enviado correctamente")
#     except smtplib.SMTPException as e:
#         print(f"Error al enviar el correo: {e}")