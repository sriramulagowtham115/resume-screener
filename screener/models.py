from django.db import models
from django.utils import timezone

class ParsedResume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.TextField()
    education = models.TextField()
    experience = models.TextField(default="Not Available")
    score = models.FloatField()
    matched_skills = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)  # NEW LINE

    def __str__(self):
        return self.email or f"Resume {self.id}"
