from celery import shared_task
import time 


@shared_task
def send_email():
    time.sleep(5)
    print ("email send")

def send_adv():
    print ("adv send")