import time
from threading import Thread

from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models


@receiver(post_save, sender=models.TodoList)
def on_post_save_sender(sender, **kwargs):
    print(f"{sender} post_save")
    t = Thread(target=long_task)
    t.start()
    print(f"{sender} post_save_end")


def long_task():
    print(f"start long task")
    time.sleep(10)
    print(f"end long task")
