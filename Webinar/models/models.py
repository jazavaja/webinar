from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    db_table = 'Users'
    # this comes and wel

    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    class Meta:
        db_table = 'Users'
        ordering = ['created_at']# this creates
        verbose_name = 'users'
        verbose_name_plural = 'users'
        # unique_together = ('firstname', 'lastname'♦
class Webinar(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    title_image = models.ImageField(upload_to='webinar_images/')
    hosted_at = models.DateTimeField()
    ticket_expiration = models.DateTimeField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'webinar'
        ordering = ['created_at']  # this creates
        verbose_name = 'webinar'
        verbose_name_plural = 'webinars'
class Site_settings(models.Model):
    key = models.CharField(max_length=100,unique=True)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'site_settings'
        ordering = ['created_at']# this creates
        verbose_name = 'site_settings'
        verbose_name_plural = 'site_settings'

# Create your models here.
class ticket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    webinar_id = models.ForeignKey(Webinar, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'ticket'
        ordering = ['created_at']# this creates
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'


from enum import Enum


class Role_webinar(Enum):
    PARTICIPANT = 'participant'
    HOST = 'host'
    SPEAKER = 'speaker'

    @classmethod
    def choices(cls):
        return [(key.value, key.name.capitalize()) for key in cls]
class webinar_user(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    webinar_id = models.ForeignKey(Webinar, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=Role_webinar.choices(),
        default=Role_webinar.PARTICIPANT.value,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'webinar_user'
        ordering = ['created_at']# this creates
        verbose_name = 'webinar_user'
        verbose_name_plural = 'webinar_users'