from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Competition(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField();
    exam_lo = models.TextField() #fileField after
    time_limit = models.IntegerField()
    start_time = models.DateTimeField(default=timezone.now)
    time_for_testing = models.IntegerField();
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

    #frint help
    def __str__(self):
        return self.name