from django.db import models

# Create your models here.

class UserModel(models.Model):
    firstName=models.CharField(max_length=500)
    lastName=models.CharField(max_length=500)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=15)


class SessionToken(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    session_token=models.CharField(max_length=500,default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)


class HouseModel(models.Model):
    city_name=models.CharField(max_length=500)
    area_name=models.CharField(max_length=500,null=True)
    area_name=models.CharField(max_length=500,null=True)
    address=models.CharField(max_length=500,null=True)
    amenities=models.CharField(max_length=700,null=True)
    furnishing=models.CharField(max_length=500,null=True)
    available_for=models.CharField(max_length=500,null=True)
    image_url=models.CharField(max_length=500,null=True)
    price=models.IntegerField(null=True)
    bedroom_no=models.IntegerField(null=True)
    house_type=models.CharField(max_length=500,null=True)
    posted_by=models.EmailField(null=True)
  

class AddBookmark(models.Model):
    user_email=models.EmailField(null=True)
    house_id=models.CharField(max_length=100,default=0)
    add_to_bookmark=models.BooleanField(default=False)