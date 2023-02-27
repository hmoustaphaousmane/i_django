from django.db import models

class Question (models.Model) :
    """
    Question model with a question and and a publication date
    """
    question_text = models.CharField (max_length = 200)
    pub_date = models.DateTimeField ('date published')

class Choice (models.Model) :
    """
    Choice model that has two fields : text of the choice and votes
    """
    question = models.ForeignKey (Question, on_delete = models.CASCADE)
    choice_text = models.CharField (max_length = 200)
    votes = models.IntegerField (default = 0)