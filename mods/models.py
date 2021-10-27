from django.db import models

# Create your models here.

class Alert(models.Model):
    alert_department = models.CharField(max_length=30)
    alert_date = models.DateField()
    alert_subject = models.CharField(max_length=100)
    alert_body = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.id}-{self.alert_department}"

