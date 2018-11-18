from django.db import models
from django.db.models import Q

# provider xor support for django queries
class QQ:
    def __xor__(self, other):    
        not_self = self.clone()
        not_other = other.clone()
        not_self.negate()
        not_other.negate()

        x = self & not_other
        y = not_self & other

        return x | y

Q.__bases__ += (QQ, )

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