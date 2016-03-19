from django.db import models

# Create your models here.
class Answers(models.Model):
    answers_text = models.CharField(max_length=200)

class Questions(models.Model):
    answers = models.ForeignKey(Answers, on_delete=models.CASCADE)
    question_text  = models.CharField(max_length=200)

class Contents():
    def __init__(self,name,text):
        self.name = name
        self.text = text

