from django.db import models
from django.contrib.auth.models import User


MEMBERSHIP_TYPE_CHOICES = [
    (1, 'mobilize'),
    (2, 'guard'),
    (3, 'army'),
    (4, 'gendarmerie'),
    (5, 'student'),
    (6, 'honorable'),
    (7, 'committee'),
    (8, 'jihadist'),
    (9, 'market'),
    (10, 'Taleb'),
    (11, 'farmer'),
    (12, 'employee'),
    (13, 'cultural'),
    (14, 'un student'),
    (15, 'artist'),
    (16, 'doctor'),
    (17, 'nomads'),
    (18, 'urban'),
    (19, 'rural'),
    (20, 'soldier'),
    (21, 'other'),
]

SITUATION_CHOICES = [
    (1, 'martyr'),
    (2, 'veteran'),
    (3, 'free'),
    (4, 'warrior'),
    (5, "martyrs' father"),
    (6, "martyrs' brother"),
    (7, 'deceased'),
]


class Report(models.Model):
    STATUS_CHOICES = [(0, 'inactive'), (1, 'active')]

    membership_type = models.SmallIntegerField(choices=MEMBERSHIP_TYPE_CHOICES)
    situation = models.SmallIntegerField(choices=SITUATION_CHOICES)
    owner_phone = models.CharField(max_length=18)
    photographer_name = models.CharField(max_length=255)
    shooting_date = models.DateField()
    camp_name = models.CharField(max_length=255)
    operational_area = models.CharField(max_length=255)
    division_commander = models.CharField(max_length=255)
    battalion_commander = models.CharField(max_length=255)
    company_commander = models.CharField(max_length=255)
    batch_commander = models.CharField(max_length=255)
    description = models.TextField()
    surname = models.CharField(max_length=255)
    supervisor = models.CharField(max_length=255)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'reports'


class Soldier(models.Model):
    TYPE_CHOICES = [(0, 'standing'), (1, 'sitting')]

    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    surname = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    responsibility = models.CharField(max_length=255)
    membership_type = models.SmallIntegerField(choices=MEMBERSHIP_TYPE_CHOICES)
    situation = models.SmallIntegerField(choices=SITUATION_CHOICES)
    workplace = models.CharField(max_length=255)
    phone = models.CharField(max_length=18)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'soldiers'
