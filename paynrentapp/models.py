from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=150, blank=False, default='')
    icon = models.ImageField(upload_to='static/')

class SubCategory(models.Model):
    category_id = models.CharField(max_length=70, blank=False, default='')
    company_name = models.CharField(max_length=70, blank=False, default='')
    subcategory_name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=150, blank=False, default='')
    icon = models.ImageField(upload_to='static/')

class Vehicle(models.Model):
    agency_id =  models.CharField(max_length=100, blank=False, default='')
    category_id = models.CharField(max_length=100, blank=False, default='')
    subcategory_id = models.CharField(max_length=100, blank=False, default='')
    model_year = models.CharField(max_length=170, blank=False, default='')
    variant = models.CharField(max_length=170, blank=False, default='')
    price = models.CharField(max_length=170, blank=False, default='')
    insured = models.CharField(max_length=70, blank=False, default='')
    registration_no = models.CharField(max_length=170, blank=False, default='')
    owner_name = models.CharField(max_length=170, blank=False, default='')
    mobile_no = models.CharField(max_length=170, blank=False, default='')
    color = models.CharField(max_length=170, blank=False, default='')
    fuel_type = models.CharField(max_length=170, blank=False, default='')
    no_of_seats = models.CharField(max_length=170, blank=False, default='')
    transmission_type = models.CharField(max_length=170, blank=False, default='')
    city =  models.CharField(max_length=100, blank=False, default='')
    icon = models.ImageField(upload_to='static/')

class Administrator(models.Model):
    admin_name = models.CharField(max_length=70, blank=False, default='')
    mobile_no= models.CharField(max_length=150, blank=False, default='')
    email_id= models.CharField(max_length=150, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')

class Customer(models.Model):
    customerf_name = models.CharField(max_length=70, blank=False, default='')
    customerl_name = models.CharField(max_length=70, blank=False, default='')
    mobile_no= models.CharField(max_length=150, blank=False, default='')
    email_id= models.CharField(max_length=150, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')
    address = models.CharField(max_length=200,blank=False,default='')

class Agency(models.Model):
    agency_name = models.CharField(max_length=70, blank=False, default='')
    mobile_no= models.CharField(max_length=150, blank=False, default='')
    email_id= models.CharField(max_length=150, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')
    city = models.CharField(max_length=70, blank=False, default='')

class User(models.Model):
    Username = models.CharField(max_length=70, blank=False, default='')
    UserEmail = models.CharField(max_length=70, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')
    mobileno= models.CharField(max_length=15, blank=False, default='')
    start_date = models.CharField(max_length=170, blank=False, default='')
    end_date = models.CharField(max_length=170, blank=False, default='')
    duration = models.CharField(max_length=70, blank=False, default='')