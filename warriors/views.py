from django.shortcuts import render
from django.views.generic import TemplateView
from warriors.models import MEMBERSHIP_TYPE_CHOICES, SITUATION_CHOICES, Report, Soldier


def index(request):
    return render(request, 'home/index.html')


def warriors(request):
    context = dict(
        memberships=MEMBERSHIP_TYPE_CHOICES,
        situations=SITUATION_CHOICES,
        soldiers_type=Soldier.TYPE_CHOICES,
        soldiers_count=range(1, 6),
    )
    return render(request, 'home/warriors.html', context)


class Warriors(TemplateView):
    template_name = 'home/warriors.html'

    def get(self, request, **kwargs):
        context = dict(
            memberships=MEMBERSHIP_TYPE_CHOICES,
            situations=SITUATION_CHOICES,
            soldiers_type=Soldier.TYPE_CHOICES,
            soldiers_count=range(1, 6),
        )
        return render(request, self.template_name, context)

    def post(self, request):
        data = request.POST
        # TODO: save data to models

        context = dict(
            memberships=MEMBERSHIP_TYPE_CHOICES,
            situations=SITUATION_CHOICES,
            soldiers_type=Soldier.TYPE_CHOICES,
            soldiers_count=range(1, 6),
        )
        return render(request, self.template_name, context)
