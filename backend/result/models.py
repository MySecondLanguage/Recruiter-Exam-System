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
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )
    total_marks = models.IntegerField()
    total_elapsed_second = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__ (self):
        return self.exam.name


@receiver(post_save, sender=Result)
def update_result_summery(sender, instance, created, **kwargs):
    if created:
        current_exam = Exam.objects.get(is_published=True)

        summery_exists = ResultSummery.objects.filter(
            exam__id=current_exam.id,
            user__id=instance.user.id
        ).exists()


        if summery_exists:
            summery = ResultSummery.objects.get(
                exam__id=current_exam.id,
                user__id=instance.user.id
            )

            prev_elapsed = int(summery.total_elapsed_second)
            h, m, s = str(instance.elapsed).split(':')
            new_elapased = int(h) * 3600 + int(m) * 60 + int(s)

            prev_total = int(summery.total_marks)
            new_total = prev_total + int(instance.marks)
            summery.total_marks = new_total
            summery.total_elapsed_second = prev_elapsed + new_elapased
            summery.save()


        else:
            h, m, s = instance.elapsed.split(':')
            elapsed = int(h) * 3600 + int(m) * 60 + int(s)
            ResultSummery.objects.create(
                user=instance.user,
                exam=current_exam,
                total_marks=instance.marks,
                total_elapsed_second=elapsed,
                is_exam_completed=False
            )


