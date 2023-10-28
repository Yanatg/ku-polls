from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Choice, Question, Vote
from .details import get_available_questions


class IndexView(generic.ListView):
    """ Generic view for displaying a list of objects. """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions
        (not including those set to be published in the future).
        """
        questions = get_available_questions()
        return Question.objects.filter(
            pk__in=questions
        ).order_by('-pub_date')
