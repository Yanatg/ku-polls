from django.db import models
from django.contrib.auth.models import User
from .choice import Choice


class Vote(models.Model):
    """ Record a Vote for a Poll Choice by User """

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "polls_vote"
        app_label = "polls"
