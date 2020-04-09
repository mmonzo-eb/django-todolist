from django.db import models
from django.conf import settings


# Create your models here.
class Priority(models.Model):

    name = models.CharField(max_length=20)
    order = models.IntegerField()

    def __str__(self):
        return '{}: {} (order {})'.format(
            self.id,
            self.name,
            self.order,
        )

    class Meta:
        verbose_name_plural = "Priorities"


class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_user'
    )
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_by'

    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='updated_by'

    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
    )
