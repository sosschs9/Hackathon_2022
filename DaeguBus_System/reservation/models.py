from csv import unregister_dialect
# from django.db import models
from djongo import models
import pymongo

client = pymongo.MongoClient("mongodb+srv://dbUser:1234@cluster0.3fk5bkx.mongodb.net/?retryWrites=true&w=majority")
db = client.deagu_bus
col_user = db.user_info

# Create your models here.
class User(models.Model):
    NATIONAL_CHOICES = (
        ('NP', 'Nomal person'),
        ('WP','Weak person'),
    )
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=2, choices=NATIONAL_CHOICES)

    def __str__(self):
        return self.user_id