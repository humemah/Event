from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from django.utils.timezone import timedelta

# Create your models here.
class MyUser(models.Model):
	name = models.CharField(max_length=30)
	phone_number = models.IntegerField()
	email = models.EmailField('User Email')

	def __str__(self):
		return self.name


class Event(models.Model):
	title = models.CharField('title', max_length=120)
	date = models.DateTimeField('Event Date')
	location = models.CharField("location",max_length=120)
	owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(MyUser, blank=True)

def calc_date():
    now = timezone.now()
    return now - timedelta(days=2)

class data(models.Model):
    destination = models.CharField('destination', max_length=30)
    destinationIATA = models.CharField('destinationIATA', max_length=12)
    origin  = models.CharField('origin', max_length=30)
    originIATA = models.CharField('originIATA', max_length=12)
    type = models.CharField('type', max_length=15)
    departure = models.DateTimeField('Departure')
    arrival = models.DateTimeField('arrival')
    created_at = models.DateField(default=calc_date)


