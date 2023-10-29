import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from polls.models import Question


class QuestionDetailViewTests(TestCase):
    """Tests for the detail view."""

    def setUp(self):
        """Set up a Question."""
        self.question = Question.objects.create(question_text='Past question.',
                                                pub_date=timezone.now() -
                                                datetime.timedelta(days=5))

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        url = reverse('polls:detail', args=(self.question.id,))

        # Create a test user and log them in
        self.client.login(username='testuser', password='12345')

        response = self.client.get(url)
        self.assertContains(response, self.question.question_text)
