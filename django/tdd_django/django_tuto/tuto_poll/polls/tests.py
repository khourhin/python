from django.core.urlresolvers import resolve
from django.test import TestCase
from django.utils import timezone
from django.http import HttpRequest
from polls import models, views

class PollsUpdateTest(TestCase):

    def test_adding_a_new_question(self):
        q = models.Question(question_text = "New poll coming ?", pub_date=timezone.now())
        q.save()
        print(q)
        self.assertEqual(len(models.Question.objects.all()), 1)

class ViewTest(TestCase):

    def test_polls_return_correct_html(self):
        found = resolve('/polls/')
        self.assertEqual(found.func, views.index)
