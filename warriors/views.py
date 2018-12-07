from django.shortcuts import render

from warriors.models import MEMBERSHIP_TYPE_CHOICES, SITUATION_CHOICES, Report, Soldier


def index(request):
    return render(request, 'home/index.html')


def warriors(request):
    context = dict(
        memberships=MEMBERSHIP_TYPE_CHOICES,
        situations=SITUATION_CHOICES
    )
    return render(request, 'home/warriors.html', context)
