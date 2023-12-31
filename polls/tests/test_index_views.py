import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from polls.models import Question


def create_question(question_text, pub_date, end_date=None):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Question.objects.create(question_text=question_text,
                                   pub_date=pub_date,
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
        question = create_question(
            question_text="Past question.",
            pub_date=timezone.now() - datetime.timedelta(days=30)
        )
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
                             pub_date=timezone.now() + datetime.timedelta(
                                 days=30))
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_now_pub_date(self):
        """
        Questions with a pub_date of now are displayed on the index page.
        """
        question = create_question(question_text="Now pub date.",
                                        pub_date=timezone.now())
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_ended_question(self):
        """
        Questions with an end_date in the past are
        still display but cannot vote.
        """
        question = create_question(
            question_text="Ended question.",
            pub_date=timezone.now() - datetime.timedelta(days=10),
            end_date=timezone.now() - datetime.timedelta(days=5)
        )
        response = self.client.get(reverse('polls:index'))
        # Check if the question is in the list
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

        # Verify that the question cannot be voted on
        self.assertFalse(question.can_vote())
