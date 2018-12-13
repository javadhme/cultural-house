from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


MEMBERSHIP_TYPE_CHOICES = [
    (1, _('mobilize')),
    (2, _('guard')),
    (3, _('army')),
    (4, _('gendarmerie')),
    (5, _('student')),
    (6, _('honorable')),
    (7, _('committee')),
    (8, _('jihadist')),
    (9, _('market')),
    (10, _('Taleb')),
    (11, _('farmer')),
    (12, _('employee')),
    (13, _('cultural')),
    (14, _('un student')),
    (15, _('artist')),
    (16, _('doctor')),
    (17, _('nomads')),
    (18, _('urban')),
    (19, _('rural')),
    (20, _('soldier')),
    (21, _('other')),
]

SITUATION_CHOICES = [
    (1, _('martyr')),
    (2, _('veteran')),
    (3, _('free')),
    (4, _('warrior')),
    (5, _("martyrs' father")),
    (6, _("martyrs' brother")),
    (7, _('deceased')),
]


class Report(models.Model):
    STATUS_CHOICES = [(0, _('inactive')), (1, _('active'))]

    image = models.ImageField(_('Image'), upload_to="images/soldiers")
    owner_phone = models.CharField(_('Own phone'), max_length=18)
    photographer_name = models.CharField(_('Photographer name'), max_length=255)
    photographer_address = models.CharField(_('Photographer address'), max_length=255)
    shooting_date = models.DateField(_('Shooting date'))
    camp_name = models.CharField(_('Camp name'), max_length=255)
    operational_area = models.CharField(_('Operational area'), max_length=255)
    division_commander = models.CharField(_('Division commander'), max_length=255)
    battalion_commander = models.CharField(_('Battalion commander'), max_length=255)
    company_commander = models.CharField(_('Company commander'), max_length=255)
    batch_commander = models.CharField(_('Batch commander'), max_length=255)
    description = models.TextField(_('Description'))
    surname = models.CharField(_('Surname'), max_length=255)
    supervisor = models.CharField(_('Supervisor'), max_length=255)
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICES, default=0)
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True, null=True)
    updated_time = models.DateTimeField(_('Updated time'), auto_now=True, null=True)

    class Meta:
        db_table = 'reports'
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')


class Soldier(models.Model):
    TYPE_CHOICES = [(0, _('standing')), (1, _('sitting'))]

    report = models.ForeignKey(Report, on_delete=models.CASCADE, verbose_name=_('Report'))
    surname = models.CharField(_('Surname'), max_length=255)
    father_name = models.CharField(_('Father name'), max_length=255)
    responsibility = models.CharField(_('Responsibility'), max_length=255)
    membership_type = models.SmallIntegerField(_('Membership type'), choices=MEMBERSHIP_TYPE_CHOICES)
    situation = models.SmallIntegerField(_('Situation'), choices=SITUATION_CHOICES)
    workplace = models.CharField(_('Workplace'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=18)
    type = models.SmallIntegerField(_('Type'), choices=TYPE_CHOICES)
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True, null=True)
    updated_time = models.DateTimeField(_('Updated time'), auto_now=True, null=True)

    class Meta:
        db_table = 'soldiers'
        verbose_name = _('Soldier')
        verbose_name_plural = _('Soldiers')
