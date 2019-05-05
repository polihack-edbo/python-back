"""Dashboard app models"""

from django.db import models


class PsychologistDashboard(models.Model):
    """Shows people who are interested in you"""
    patients = models.ManyToManyField()