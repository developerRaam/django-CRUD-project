from django.db import models

# Create your models here.
class UserAccount(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=250, editable=False)
    on_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class IncidentMaster(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=255)
    incident_department = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    incidnt_location = models.CharField(max_length=255)
    incident_severity = models.CharField(max_length=255)
    suspected_cause = models.CharField(max_length=255)
    immediate_action = models.CharField(max_length=255)
    
    
class SubIncidentType(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE,blank=True, null=True)
    indcident_id = models.ForeignKey(IncidentMaster, on_delete=models.CASCADE,blank=True, null=True)
    incident_type = models.CharField(max_length=50)
    on_date = models.DateField(auto_now=True)