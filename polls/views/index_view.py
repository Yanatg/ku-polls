from django.views import generic
from polls.models import Question
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
