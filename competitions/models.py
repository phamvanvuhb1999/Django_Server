from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

def validate_count_time(value):
    import os
    from django.core.exceptions import ValidationError
    if value <= 0:
        raise ValidationError('Input value invalid.')


class Competition(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    exam_lo = models.FileField(upload_to='exam_los')
    time_limit = models.IntegerField(validators=[validate_count_time])
    start_time = models.DateTimeField(default=timezone.now)
    time_for_testing = models.IntegerField(validators=[validate_count_time]);
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

    #frint help
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("competition-detail", kwargs={"pk": self.pk})
