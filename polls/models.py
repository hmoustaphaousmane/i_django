import datetime

from django.db import models
from django.utils import timezone

class Question (models.Model) :
    """
    Question model with a question and and a publication date
    """
    question_text = models.CharField (max_length = 200)
    pub_date = models.DateTimeField ('date published')

    def __str__ (self) :
        return self.question_text

    def recently_published (self) :
        return self.pub_date >= timezone.now () - datetime.timedelta (days = 1)

class Choice (models.Model) :
    """
    Choice model that has two fields : text of the choice and votes
    """
    question = models.ForeignKey (Question, on_delete = models.CASCADE)
    choice_text = models.CharField (max_length = 200)
    votes = models.IntegerField (default = 0)

    def __str__ (self) :
        return self.choice_text