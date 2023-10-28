from django.db import models
from django.contrib.auth.models import User
from .choice import Choice


class Vote(models.Model):
    """ Record a Vote for a Poll Choice by User """

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
