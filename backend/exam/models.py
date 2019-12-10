from django.db import models


class Topic(models.Model):
    name = models.CharField(
        max_length=50
    )

class Choice(models.Model):
    choice_text = models.CharField(
        max_length=200
    )
    is_right_choice = models.BooleanField(
        default=False
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
    choices = models.ManyToManyField(
        Choice,
        through='QuestionChoice'
    )

class QuestionChoice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE
    )

class Exam(models.Model):
    name = models.CharField(
        max_length=100
    )
    total_duration = models.DurationField(
        default=30
    )
    queston = models.ManyToManyField(
        Question,
        through='QuestionGroup'
    )
    is_published = models.BooleanField(
        default=True
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


