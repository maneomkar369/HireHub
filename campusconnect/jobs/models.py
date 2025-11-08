from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.JSONField(default=list)
    about = models.TextField(blank=True)
    course = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=10, choices=[('student', 'Student'), ('admin', 'Admin'), ('recruiter', 'Recruiter')], default='student')
    company_name = models.CharField(max_length=200, blank=True)
    projects = models.JSONField(default=list, blank=True)
    # Portfolio fields
    github_url = models.URLField(blank=True, verbose_name='GitHub Profile')
    linkedin_url = models.URLField(blank=True, verbose_name='LinkedIn Profile')
    portfolio_url = models.URLField(blank=True, verbose_name='Portfolio Website')
    certifications = models.JSONField(default=list, blank=True, help_text='List of certifications')

    def __str__(self):
        return self.user.username
    
    def skill_match_percentage(self, job):
        """Calculate skill match percentage for a given job"""
        if not self.skills or not job.skills_required:
            return 0
        user_skills = set(skill.lower() for skill in self.skills)
        job_skills = set(skill.lower() for skill in job.skills_required)
        if not job_skills:
            return 0
        matching = user_skills.intersection(job_skills)
        return round((len(matching) / len(job_skills)) * 100, 1)

class Job(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('filled', 'Filled'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    skills_required = models.JSONField(default=list)
    apply_link = models.URLField(blank=True)
    last_date = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def is_expired(self):
        """Check if job has passed the last application date"""
        from django.utils import timezone
        return timezone.now().date() > self.last_date
    
    def application_count(self):
        """Get number of applications for this job"""
        return self.application_set.count()

class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('interviewed', 'Interviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    status_updated_at = models.DateTimeField(auto_now=True)
    recruiter_notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'job')
        ordering = ['-applied_at']
    
    def skill_match_percentage(self):
        """Get skill match percentage for this application"""
        try:
            return self.user.profile.skill_match_percentage(self.job)
        except:
            return 0
