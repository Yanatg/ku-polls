from django.db import models
from .question import Question


class Choice(models.Model):
    """ Model for polls choices """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    @property
    def votes(self):
        # count the votes for this choice
        return self.vote_set.count()

    def __str__(self):
        return self.choice_text
