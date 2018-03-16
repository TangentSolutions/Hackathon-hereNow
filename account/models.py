from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User


class UserRole(models.Model):
    ROLE_CHOICES = (
        ('P', 'Primary User'),
        ('C', 'Connected User')
    )

    name = models.CharField(max_length=50, choices=ROLE_CHOICES)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return '{} - {}'.format(self.name, self.description)

class UserDetail(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unspecified')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='U')
    address = models.TextField(null=True, blank=True, default=None)
    phone = models.CharField('Contact Number', max_length=50, blank=True, null=True)

    role = models.ForeignKey(UserRole, related_name='users', blank=True, null=True, on_delete=models.DO_NOTHING)

    related_users = models.ForeignKey('UserDetail', on_delete=models.CASCADE, related_name="user_related_users", null=True,
                                      blank=True)
    token = models.CharField(max_length=255, null=True, blank=True, default=None)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.user.first_name)


@receiver(post_save, sender=User)
def create_user_user_detail(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_user_detail(sender, instance, **kwargs):
    instance.user.save()