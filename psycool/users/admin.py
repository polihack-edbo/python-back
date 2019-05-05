"""User app admin config"""

from django.contrib import admin

from .models import Patient, Psychologist

admin.site.register(Patient)
admin.site.register(Psychologist)