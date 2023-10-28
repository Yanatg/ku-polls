from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Choice, Question, Vote
from .details import get_available_questions


class ResultsView(generic.DetailView):
    """
    Generic view for displaying a detail page for a particular type of object.
    """
    model = Question
    template_name = 'polls/results.html'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except:
            return redirect('polls:index')
        if not self.object.is_published():
            messages.error(request,
                           'This question is not available for voting.')
            return redirect('polls:index')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        questions = get_available_questions()
        return Question.objects.filter(pk__in=questions)
