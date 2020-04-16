from django.db import models

# Create your models here.
class card_data(models.Model):
    number = models.CharField(max_length=20,null=True)
    month = models.IntegerField()
    year = models.IntegerField()
    cvc = models.IntegerField()
