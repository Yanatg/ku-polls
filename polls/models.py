import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """ Model for polls questions """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    end_date = models.DateTimeField('date ended', default=None, null=True, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        return self.pub_date <= timezone.now()

    def can_vote(self):
        return self.is_published() and (self.end_date is None or self.end_date >= timezone.now())


class Choice(models.Model):
    """ Model for polls choices """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
