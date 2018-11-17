from django.db import models

class Local(models.Model):
    name = models.CharField(max_length=100)
    area_total = models.IntegerField()
    aliquot = models.IntegerField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    pincode = models.IntegerField()

    def __str__(self):
        return self.name