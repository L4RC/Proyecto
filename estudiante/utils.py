# En un archivo como 'utils.py' en la carpeta de tu aplicación
from django.core.mail import send_mail

def send_registration_email(user_email):
    subject = 'Gracias por registrarte'
    message = '¡Gracias por registrarte en nuestro sitio web!'
    from_email = 'estudianteusac54@gmail.com'
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
