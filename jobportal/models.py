from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile

class Jobs(models.Model):
    job_title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    job_description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk':self.pk})
    

class JobApplication(models.Model):
    applicant = models.ManyToManyField(User)
    cover_letter = models.TextField()
    cv = models.FileField()
    date_applied = models.DateTimeField(default=timezone.now)