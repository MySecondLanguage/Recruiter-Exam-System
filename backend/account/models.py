from django.db import models
from django.contrib.auth.models import User

from . enum_helper import UserType

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    user_type = models.CharField(
        choices=UserType.choices(),
        max_length=1,
        default=UserType.EXAMINEE.value
    )