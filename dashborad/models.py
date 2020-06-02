from django.db import models
from django.utils import timezone

# Create your models here.
class Health(models.Model):
    time = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    intensitytime = models.TextField(blank=True, null=True)
    intensity = models.TextField(blank=True, null=True)
    stepsminute = models.TextField(blank=True, null=True)
    steps = models.TextField(blank=True, null=True)
    sleepminute = models.TextField(blank=True, null=True)
    sleepvalue = models.TextField(blank=True, null=True)
    sleeplogid = models.TextField(blank=True, null=True)
    metminute = models.TextField(blank=True, null=True)
    mets = models.TextField(blank=True, null=True)
    calminute = models.TextField(blank=True, null=True)
    calories = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health'


