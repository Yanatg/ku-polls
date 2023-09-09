import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question


def create_question(question_text, pub_date, end_date=None):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Question.objects.create(question_text=question_text, pub_date=pub_date,
                                   end_date=end_date)


class QuestionIndexViewTests(TestCase):
    """ Tests for the index view."""

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.",
                                   pub_date=timezone.now() - datetime.timedelta(days=30))
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.",
                        pub_date=timezone.now() + datetime.timedelta(days=30))
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_now_pub_date(self):
        """
        Questions with a pub_date of now are displayed on the index page.
        """
        question = create_question(question_text="Now pub date.", pub_date=timezone.now())
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )


class QuestionDetailViewTests(TestCase):
    """ Tests for the detail view."""

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.',
                                        pub_date=timezone.now() - datetime.timedelta(days=5))
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionResultsViewTests(TestCase):
    """ Tests for the results view. """

    def test_vote_count_display(self):
        """ Tests that the vote count is displayed. """
        question = create_question(question_text='Vote count display.', pub_date=timezone.now())
        choice = question.choice_set.create(choice_text='Choice 1')
        choice.votes = 5
        choice.save()
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertContains(response, '5')


class QuestionCanVoteTests(TestCase):
    """ Tests for the can_vote method of the Question model. """

    def test_can_vote_on_start_date(self):
        """ Tests that can_vote returns True when the start date is today. """
        question = create_question(question_text='Can vote on start date.', pub_date=timezone.now())
        self.assertTrue(question.can_vote())

    def test_can_vote_future_start_date(self):
        """ Tests that can_vote returns False when the start date is in the future. """
        question = create_question(question_text='Can vote on start date.',
                                   pub_date=timezone.now() + datetime.timedelta(days=5))
        self.assertFalse(question.can_vote())

    def test_can_vote_past_end_date(self):
        """ Tests that can_vote returns False when the end date is in the past. """
        question = create_question(question_text='Can vote on start date.',
                                   pub_date=timezone.now() - datetime.timedelta(days=5),
                                   end_date=timezone.now() - datetime.timedelta(days=1))
        self.assertFalse(question.can_vote())

    def test_can_vote_on_publishe_date(self):
        """ Tests that can_vote returns True when the start date is today. """
        question = create_question(question_text='Can vote on start date.', pub_date=timezone.now())
        self.assertTrue(question.can_vote())
