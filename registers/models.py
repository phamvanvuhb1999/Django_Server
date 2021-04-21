from django.db import models
from django.contrib.auth.models import User
from competitions.models import Competition
from django.utils import timezone

# Create your models here.

def validate_model_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.save', '.h5','.pkt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_testfile_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.cpp', '.py', '.java']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')




class Register(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    competition_id = models.ForeignKey(Competition,on_delete=models.PROTECT)
    joined_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.user_id.username


class BaiLam(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    competition_id = models.ForeignKey(Competition, on_delete=models.PROTECT)
    percent = models.FloatField(default=0.0)
    trained_model = models.FileField(upload_to='models', null=False, blank=False, validators=[validate_model_file_extension])
    test_code = models.FileField(upload_to='test_file',blank=False, validators=[validate_testfile_extension])
    posted_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.user_id.username
