from django.db import models

class crime(models.Model):
  crime_type = models.CharField(max_length=100, blank=True, null=True, default="")
  year = models.IntegerField(blank=True, null=True, default=None)
  month = models.IntegerField(blank=True, null=True, default=None)  
  day = models.IntegerField(blank=True, null=True, default=None)  
  hour = models.IntegerField(blank=True, null=True, default=None)
  minute = models.IntegerField(blank=True, null=True, default=None)
  block = models.CharField(max_length=100, blank=True, null=True, default=None)
  neighbor = models.CharField(max_length=100,blank=True, null=True, default=None)
  x = models.CharField(max_length=20, blank=True, null=True, default=None)
  y = models.CharField(max_length=20, blank=True, null=True, default=None)

  def __str__(self):
    return self.crime_type