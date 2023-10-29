from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from polls.models import Choice, Question, Vote


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
        user_last_vote = get_user_last_vote(request.user, self.object)
        context = self.get_context_data(object=self.object,
                                        user_last_vote=user_last_vote)
        return self.render_to_response(context)

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        questions = get_available_questions()
        return Question.objects.filter(pk__in=questions)


@login_required
def vote(request, question_id):
    """ View for voting on a question. """
    question = get_object_or_404(Question, pk=question_id)

    if not question.can_vote():
        messages.error(request,
                       'This question is not available for voting.')
        return redirect('polls:index')

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        messages.error(request, "You didn't select a choice.")
        return redirect('polls:detail', pk=question.id)

    try:
        # get the vote for this user and this question
        vote = Vote.objects.get(user=request.user, choice__question=question)
        # update the vote
        vote.choice = selected_choice
        vote.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=request.user, choice=selected_choice)
    # vote.save()
    messages.success(request, 'You have successfully voted.')

    return HttpResponseRedirect(
        reverse('polls:results', args=(question.id,)))


def get_available_questions():
    """ Returns a list of questions that are available to view. """
    questions = Question.objects.all()
    return [q.id for q in questions if q.is_published()]


def get_user_last_vote(user, question):
    """ Returns the last vote of a user for a question. """
    if user.is_authenticated:
        try:
            return Vote.objects.filter(
                user=user, choice__question=question).last()
        except Vote.DoesNotExist:
            return None
    return None
