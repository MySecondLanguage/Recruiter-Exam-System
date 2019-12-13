from django.db import models
from django.contrib.auth.models import User

from exam.models import Question


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
