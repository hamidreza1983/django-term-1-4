from celery import shared_task
import time
from django.core.mail import send_mail


@shared_task
def send_email(
    title: str,
    caption: str,
    sender: str,
    receiver: list,
    fail_silently=True,
):
    time.sleep(10)
    send_mail(title, caption, sender, receiver, fail_silently)