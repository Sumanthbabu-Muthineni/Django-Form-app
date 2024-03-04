from django.db import models

class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    event_sessions = models.TextField()
