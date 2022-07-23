from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100, verbose_name='package name')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='package price')
    detail = models.TextField(verbose_name='package details')
    items = models.IntegerField()
    type_of_camera = models.CharField(max_length=100, verbose_name='Type of camera',null=True)
    process = models.CharField(max_length=100, verbose_name='Process',null=True)
    term = models.CharField(max_length=100, verbose_name='term', null=True)
    image = models.ImageField(upload_to='images/Package__images/', verbose_name="Package image", blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name='package category', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='category name')
    image = models.ImageField(upload_to='images/Category__images/', verbose_name="Category image", blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', verbose_name="Appointment category",null=True, on_delete=models.DO_NOTHING)
    package = models.ForeignKey('Package', verbose_name="Appointment package", on_delete=models.DO_NOTHING)
    date = models.DateTimeField('%Y-%m-%d %H:%M:%S',null=True,blank=True)
    time = models.TimeField(verbose_name="Appointment time",null=True,blank=True)
    first_name = models.CharField(max_length=100,verbose_name='Your first name', blank=True)
    last_name = models.CharField(max_length=100,verbose_name='Your last name', blank=True)
    email = models.CharField(max_length=100,verbose_name='Your email address')
    phone = models.CharField(max_length=13,verbose_name='Your phone number')
    # massage = models.TextField(null=True,blank=True,verbose_name="Your massage")
    def __str__(self):
        return self.first_name

class Team(models.Model):
    name = models.CharField(max_length=100,verbose_name='name')
    title = models.CharField(max_length=100,verbose_name='title')
    image = models.ImageField(upload_to='images/team__images/', verbose_name="image")


