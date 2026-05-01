from django.contrib import admin
from .models import Partner_Category, Activity, Partner, Team_Member, Media, Member_Position, Statistic, Participant, Project
#register your models here

admin.site.register(Partner_Category)
admin.site.register(Activity)
admin.site.register(Partner)
admin.site.register(Team_Member)
admin.site.register(Media)
admin.site.register(Member_Position)
admin.site.register(Participant)
admin.site.register(Project)

class StatisticAdmin(admin.ModelAdmin):
    list_display = ('value', 'description', 'order')
    list_editable = ('order',)
    ordering = ('order',)

admin.site.register(Statistic, StatisticAdmin)