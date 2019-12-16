from django.db import models
from django.contrib.auth.models import User

from exam.models import (
    Question,
    Exam,
)


class Result(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    marks = models.IntegerField(
        default=0
    )

    elapsed = models.DurationField(
        null=True,
        blank=True
    )

    def __str__ (self):
        return self.user.question.title

class ResultSummery(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    is_exam_completed = models.BooleanField(default=False)
    exam = models.OneToOneField(
        Exam,
        on_delete=models.CASCADE
    )
    total_marks = models.IntegerField()

    def __str__ (self):
        return self.exam.name
