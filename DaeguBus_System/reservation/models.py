from csv import unregister_dialect
from secrets import choice
# from django.db import models
from djongo import models
import pymongo

client = pymongo.MongoClient("mongodb+srv://dbUser:1234@cluster0.3fk5bkx.mongodb.net/?retryWrites=true&w=majority")
db = client.deagu_bus
col_user = db.user_info

# Create your models here.
class User_db(models.Model):
    NATIONAL_CHOICES = (
        ('NP', 'Nomal person'),
        ('WP','Weak person'),
    )
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=2, choices=NATIONAL_CHOICES)

    def __str__(self):
        return self.user_id

class ReserveBus(models.Model):
    BUS_CHOICES = (
        ('N1', '예약버스 1번'),
        ('N2', '예약버스 2번'),
        ('N3', '예약버스 3번'),
    )

    busname = models.CharField(max_length=2, choices=BUS_CHOICES)
    startStation = models.CharField(max_length=200)
    endStation = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id
