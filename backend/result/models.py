from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import (
    post_save,
    post_delete
)
from django.dispatch import receiver

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
        return self.question.title

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


@receiver(post_save, sender=Result)
def update_result_summery(sender, instance, created, **kwargs):
    if created:
        current_exam = Exam.objects.get(is_published=True)

        summery_exists = ResultSummery.objects.filter(exam__id=current_exam.id).exists()


        if summery_exists:
            summery = ResultSummery.objects.get(exam__id=current_exam.id)
            prev_total = int(summery.total_marks)
            new_total = prev_total + int(instance.marks)
            summery.total_marks = new_total
            summery.save()

            
        else:
            ResultSummery.objects.create(
                user=instance.user,
                exam=current_exam,
                total_marks=instance.marks,
                is_exam_completed=False
            )


