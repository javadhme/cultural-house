from django.contrib import admin
from warriors.models import Report, Soldier


class ReportAdmin(admin.ModelAdmin):
    list_display = ['surname', 'membership_type', 'situation', 'owner_phone', 'photographer_name', 'status']
    search_fields = ['surname', 'membership_type', 'situation', 'owner_phone', 'photographer_name', 'status']
    list_filter = ['surname', 'membership_type', 'situation', 'owner_phone', 'photographer_name', 'status']


class SoldierAdmin(admin.ModelAdmin):
    list_display = ['surname', 'father_name', 'responsibility', 'membership_type']
    search_fields = ['surname', 'father_name', 'responsibility', 'membership_type']
    list_filter = ['surname', 'father_name', 'responsibility', 'membership_type']


admin.site.register(Report, ReportAdmin)
admin.site.register(Soldier, SoldierAdmin)
