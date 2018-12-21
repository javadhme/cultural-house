from datetime import datetime
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

        report = Report(
            image="images/soldiers",
            owner_phone=data.get('owner_phone'),
            photographer_name=data.get('photographer_name'),
            photographer_address=data.get('photographer_position'),
            shooting_date=datetime.now().date(),  # data.get('shooting_date')
            camp_name=data.get('camp_name'),
            operational_area=data.get('operational_area'),
            division_commander=data.get('division_commander'),
            battalion_commander=data.get('battalion_commander'),
            company_commander=data.get('company_commander'),
            batch_commander=data.get('batch_commander'),
            description=data.get('description'),
            surname=data.get('surname'),
            supervisor=data.get('supervisor')
        )
        report.save()

        soldiers = []
        for i in range(1, int(data.get('count'))+1):
            if data['soldier_name_%s' % i]:
                soldiers.append(
                    Soldier(
                        report_id=report.id,
                        surname=data['soldier_name_%s' % i],
                        father_name=data['father_name_%s' % i],
                        responsibility=data['responsibility_%s' % i],
                        membership_type=data['membership_type_%s' % i],
                        situation=data['situation_%s' % i],
                        workplace=data['workplace_%s' % i],
                        phone=data['phone_%s' % i],
                        type=data['type_%s' % i]
                    )
                )

        try:
            Soldier.objects.bulk_create(soldiers)
        except Exception as e:
            print(e)

        context = dict(
            memberships=MEMBERSHIP_TYPE_CHOICES,
            situations=SITUATION_CHOICES,
            soldiers_type=Soldier.TYPE_CHOICES,
            soldiers_count=range(1, 6),
        )
        return render(request, self.template_name, context)
