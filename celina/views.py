from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django_celery_results.models import TaskResult
from random import randint
from .tasks import add


class ListView(View):
    """Widok listy wszystkich puszczonych zadań"""
    def get(self, request):
        """Zwraca listę zadań ułożoną względem czasu ukończenia"""
        list_of_result = TaskResult.objects.all().order_by('-date_done')
        return render(request, 'index.html', {'l':list_of_result})


class AddView(View):
    def get(self, request):
        number_one = randint(0, 100)
        number_two = randint(0, 100)
        add.delay(number_one, number_two)
        return redirect(reverse(viewname='list'))
