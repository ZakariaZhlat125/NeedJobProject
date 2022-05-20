
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField




GENDER_CHOICES = (
    ('M', "Male"),
    ('F', "Female"),
    ('O', "Other"),
)
class User(AbstractUser):
    username=None
    email=models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    date_of_birth = models.DateField(default='1990-01-01')
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
    picture=models.ImageField(
        upload_to='img/users',null=True,verbose_name=""
    )
    phone = PhoneNumberField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
        return self.email