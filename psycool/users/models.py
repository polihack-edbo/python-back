"""User app models"""

from django.db import models

from django.contrib.auth import get_user_model


class Profile(models.Model):
    """Profile used as abstract class to other models"""
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    birthday = models.DateField()
    region = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{ self.user.first_name } { self.user.last_name }'

    class Meta:
        abstract = True


class Patient(Profile):
    """Patient model that extends from Profile abstract class"""
    contact = models.CharField(max_length=30, null=True)
    relative_contact = models.CharField(max_length=30, null=True)
    occupation = models.CharField(max_length=30)
    educational_level = models.CharField(max_length=50)


class Psychologist(Profile):
    """Psychologist model that extends from Profile abstract class"""
    professional_license = models.ImageField(upload_to='licenses')
    school = models.CharField(max_length=50)
    verified = models.BooleanField(blank=True, default=False)

