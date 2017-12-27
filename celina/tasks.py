"""Task Module"""
from celery import shared_task
from time import sleep
from random import randint
from .models import History


@shared_task(rate_limit="5/m")
def add_history(number_of_values=100, minimum=0, maximum=100):
    """
    Add to history table random values
    :param number_of_values: number of values/rows in db
    :param minimum: minimal value
    :param maximum: maximum value
    :return:
    """
    for counter in range(number_of_values):
        History.objects.create(value=randint(minimum, maximum))
    return True


@shared_task(rate_limit="5/m")
def add_history_bulk(number_of_values=100, minimum=0, maximum=100):
    """
    Add to history table random values in bulk
    :param number_of_values: number of values/rows in db
    :param minimum: minimal value
    :param maximum: maximum value
    :return:
    """
    history_list = []
    for counter in range(number_of_values):
        new_history = History(value = randint(minimum, maximum))
        history_list.append(new_history)
    History.objects.bulk_create(history_list)
    return True


@shared_task
def add(first_number, second_number):
    """
    Bardzo prosty task, który sumuje 2 liczby. Dodane sztucznie sleep, które
    powoduje udawanie, że task wykonuje się długo.
    :param first_number: pierwsza liczba
    :param second_number: druga liczba
    :return: suma liczb
    """
    sleep(randint(1, 5))
    return first_number + second_number
