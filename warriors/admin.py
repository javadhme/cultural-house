from django.contrib import admin
from warriors.models import Report, Soldier
from django.utils.translation import gettext as _
from django.template.loader import render_to_string


class SoldierInline(admin.TabularInline):
    model = Soldier


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['thumb', 'surname', 'owner_phone', 'photographer_name', 'status']
    ordering = ['-created_time']
    search_fields = ['surname', 'owner_phone', 'photographer_name', 'status']
    list_filter = ['surname', 'owner_phone', 'photographer_name', 'status']

    fieldsets = (
        ("Report", {
            'fields': ('picture', 'image', 'owner_phone', 'photographer_name',
                       'shooting_date', 'camp_name', 'operational_area', 'division_commander', 'battalion_commander',
                       'company_commander', 'batch_commander', 'description', 'surname', 'supervisor', 'status'),
        }),
    )
    readonly_fields = ['picture', ]

    inlines = [SoldierInline]

    def picture(self, obj):
        if obj.image:
            return render_to_string('form_img.html', {'image': obj.image})

    def thumb(self, obj):
        if obj.image:
            return render_to_string('thumb.html', {'image': obj.image})
        else:
            return ''

    picture.short_description = _('Preview')
    thumb.short_description = _('Thumb')
