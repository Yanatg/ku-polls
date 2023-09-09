from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .models import Choice, Question


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
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """
    Generic view for displaying a detail page for a particular type of object.
    """
    model = Question
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except:
            return redirect('polls:index')
        if not self.object.can_vote():
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


def vote(request, question_id):
    """ View for voting on a question. """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,)))


def get_available_questions():
    """ Returns a list of questions that are available to view. """
    questions = Question.objects.all()
    return [q.id for q in questions if q.is_published()]
