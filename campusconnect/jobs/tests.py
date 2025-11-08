from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Job, SavedJob, Application

class CampusConnectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(user=self.user, skills=['Python', 'Django'])
        self.job = Job.objects.create(
            title='Test Job',
            company='Test Company',
            location='Remote',
            job_type='Full-time',
            skills_required=['Python'],
            apply_link='https://example.com',
            last_date='2025-12-31',
            posted_by=self.user
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertIn('Python', self.profile.skills)

    def test_job_creation(self):
        self.assertEqual(self.job.title, 'Test Job')
        self.assertEqual(self.job.company, 'Test Company')

    def test_save_job(self):
        saved = SavedJob.objects.create(user=self.user, job=self.job)
        self.assertEqual(saved.user, self.user)
        self.assertEqual(saved.job, self.job)

    def test_apply_job(self):
        application = Application.objects.create(user=self.user, job=self.job)
        self.assertEqual(application.user, self.user)
        self.assertEqual(application.job, self.job)

    def test_eligibility_check(self):
        # Test match
        user_skills = set(self.profile.skills)
        job_skills = set(self.job.skills_required)
        self.assertTrue(user_skills.issuperset(job_skills))

        # Test partial
        self.job.skills_required = ['Python', 'Java']
        self.job.save()
        job_skills = set(self.job.skills_required)
        self.assertTrue(user_skills & job_skills)
        self.assertFalse(user_skills.issuperset(job_skills))

        # Test none
        self.job.skills_required = ['Java', 'C++']
        self.job.save()
        job_skills = set(self.job.skills_required)
        self.assertFalse(user_skills & job_skills)
