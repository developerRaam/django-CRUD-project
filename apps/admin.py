from django.contrib import admin
from .models import *

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("name","mobile","email","on_date")
admin.site.register(UserAccount,UserAccountAdmin)

class IncidentMasterAdmin(admin.ModelAdmin):
    list_display = ("location","incident_department","date_time","incidnt_location","incident_severity","suspected_cause","immediate_action")
admin.site.register(IncidentMaster,IncidentMasterAdmin)

class SubIncidentTypeAdmin(admin.ModelAdmin):
    list_display = ("user_id","indcident_id","incident_type","on_date")
admin.site.register(SubIncidentType,SubIncidentTypeAdmin)