from celery import shared_task
from time import sleep
from random import randint


@shared_task
def add(x, y):
    """
    Bardzo prosty task, który sumuje 2 liczby. Dodane sztucznie sleep, które
    powoduje udawanie, że task wykonuje się długo.
    :param x: pierwsza liczba
    :param y: druga liczba
    :return: suma liczb
    """
    sleep(randint(1,5))
    return x + y
