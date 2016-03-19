from django.db import models

# Create your models here.

class Answers(models.Model):
    answers_text = models.CharField(max_length=200)
    def __str__(self):
        return answers_text

class Questions(models.Model):
    answers = models.ForeignKey(Answers, on_delete=models.CASCADE)
    question_text  = models.CharField(max_length=200)


class Contents(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

