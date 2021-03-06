from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name

class Choice(models.Model):
    choice_text = models.CharField(
        max_length=200
    )
    is_right_choice = models.BooleanField(
        default=False
    )
    def __str__(self):
        return self.choice_text

class SelectedChoices(models.Model):
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        related_name='selected_choice'
    )
    is_selected = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    exam = models.ForeignKey(
        'exam.Exam',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    question = models.ForeignKey(
        'exam.Question',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="selected_choice"
    )


class Question(models.Model):
    title = models.CharField(
        max_length=100
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="questions_by_topic"
    )
    total_duration = models.DurationField(
        default=30
    )
    choices = models.ManyToManyField(
        Choice,
        through='QuestionChoice'
    )

    def __str__(self):
        return self.title

class QuestionChoice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE
    )
    def __str__ (self):
        return self.choice.choice_text

class Exam(models.Model):
    name = models.CharField(
        max_length=100
    )
    total_duration = models.DurationField(
        null=True,
        blank=True
    )
    question = models.ManyToManyField(
        Question,
        through='QuestionGroup'
    )
    is_published = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

class QuestionGroup(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )


