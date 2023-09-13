from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=100)
    event_location = models.CharField(max_length=70)
    event_date = models.CharField(max_length=50)
    event_desc = models.TextField()

    def __str__(self):
        return self.event_title
    
class Applicant(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name