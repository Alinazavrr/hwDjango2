from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import Signal
from django.dispatch import receiver
from django.core.signing import Signer

@receiver(post_save, sender=User)
def check_user_email(sender, **kwargs):
    user = kwargs['instance']
    username = user.username
    niga = Signer.sign(username)
    email = EmailMessage(subject='Check email', body=f'127.0.0.1:8000/accept/{niga}', to=[user.email])
    email.send()
