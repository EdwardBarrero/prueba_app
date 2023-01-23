import datetime

from django.urls.base import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Question
# Create your tests here.
class QuestionModelTest(TestCase):

  def test_was_published_recently_with_future_questions(self):
    time = timezone.now() + datetime.timedelta(days=2)
    future_question = Question(question_text = "¿Cual es tu zona del mundo favorita?", pub_date=time)
    self.assertIs(future_question.was_published_recently(), False)

  def test_was_published_recently_with_past_questions(self):
    time = timezone.now() - datetime.timedelta(days=2)
    past_question = Question(question_text="¿Qué día es?", pub_date=time)
    self.assertIs(past_question.was_published_recently(), False)

  def test_was_publised_recently_with_present_time(self):
    time = timezone.now()
    today_question = Question(question_text="test today", pub_date=time)
    self.assertIs(today_question.was_published_recently(), True)

class QuestionIndexViewTest(TestCase):
  
  def test_no_question(self):
    response = self.client.get(reverse("polls:index"))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available")
    self.assertQuerysetEqual(response.context["lastest_questions_list"], [])

  def test_no_future_question(self):
    response = self.client.get(reverse("polls:index"))
    time = timezone.now() + datetime.timedelta(days=2)
    future_question = Question(question_text='Pregunta del futuro', pub_date=time)
    self.assertEqual(response.status_code, 200)
    self.assertNotIn(future_question, response.context['lastest_questions_list'])
    