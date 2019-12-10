from django.db import models


class Topic(models.Model):
    name = models.CharField(
        max_length=50
    )

class Question(models.Model):
    title = models.CharField(
        max_length=100
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )
    total_duration = models.DurationField(
        default=30
    )

class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(
        max_length=200
    )
    is_right_answer = models.BooleanField(
        default=False
    )

class Exam(models.Model):
    name = models.CharField(
        max_length=100
    )
    total_duration = models.DurationField(
        default=30
    )

class QuestionGroup(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )


