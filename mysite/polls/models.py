from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

#this will make a table called question in the db
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #could be used for example to sort questions by date
    pub_date = models.DateTimeField()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

#corresponds to a question, will be a table in the db
class Choice(models.Model):
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


