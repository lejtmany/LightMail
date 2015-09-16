from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    dob = models.DateField()

class Email(models.Model):
    date = models.DateTimeField()
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    is_deleted = models.BooleanField()



