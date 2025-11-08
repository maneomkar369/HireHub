#!/usr/bin/env python
"""Setup script to create admin user and sample jobs"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campusconnect.settings')
django.setup()

from django.contrib.auth.models import User
from jobs.models import Job, Profile
from datetime import datetime, timedelta

print("=" * 50)
print("HireHub - Admin Setup")
print("=" * 50)

# Create or get admin user
admin_username = input("Enter admin username (default: admin): ").strip() or "admin"
admin_email = input("Enter admin email (default: admin@hirehub.com): ").strip() or "admin@hirehub.com"
admin_password = input("Enter admin password (default: admin123): ").strip() or "admin123"

admin_user, created = User.objects.get_or_create(
    username=admin_username,
    defaults={
        'email': admin_email,
        'is_staff': True,
        'is_superuser': True
    }
)

if created:
    admin_user.set_password(admin_password)
    admin_user.save()
    print(f"✓ Created admin user: {admin_username}")
else:
    if not admin_user.is_staff:
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        print(f"✓ Updated {admin_username} to admin")
    else:
        print(f"✓ Admin user already exists: {admin_username}")

print(f"\nAdmin Login Credentials:")
print(f"  Username: {admin_username}")
print(f"  Password: {admin_password}")

# Sample jobs data
jobs_data = [
    {
        'title': 'Software Development Intern',
        'company': 'Google',
        'location': 'Bangalore, India',
        'job_type': 'Internship',
        'skills_required': ['Python', 'JavaScript', 'React'],
        'apply_link': 'https://careers.google.com/apply',
        'last_date': datetime.now().date() + timedelta(days=30)
    },
    {
        'title': 'Full Stack Developer',
        'company': 'Amazon',
        'location': 'Hyderabad, India',
        'job_type': 'Full-time',
        'skills_required': ['Java', 'AWS', 'Node.js', 'MongoDB'],
        'apply_link': 'https://amazon.jobs/apply',
        'last_date': datetime.now().date() + timedelta(days=25)
    },
    {
        'title': 'Data Science Intern',
        'company': 'Microsoft',
        'location': 'Pune, India',
        'job_type': 'Internship',
        'skills_required': ['Python', 'Machine Learning', 'SQL', 'Data Analysis'],
        'apply_link': 'https://careers.microsoft.com/apply',
        'last_date': datetime.now().date() + timedelta(days=20)
    },
    {
        'title': 'Frontend Developer',
        'company': 'Flipkart',
        'location': 'Bangalore, India',
        'job_type': 'Full-time',
        'skills_required': ['React', 'TypeScript', 'CSS', 'HTML'],
        'apply_link': 'https://flipkart.com/careers',
        'last_date': datetime.now().date() + timedelta(days=15)
    },
    {
        'title': 'UI/UX Design Intern',
        'company': 'Swiggy',
        'location': 'Mumbai, India',
        'job_type': 'Internship',
        'skills_required': ['Figma', 'Adobe XD', 'UI Design', 'User Research'],
        'apply_link': 'https://swiggy.com/careers',
        'last_date': datetime.now().date() + timedelta(days=18)
    },
]

print("\n" + "=" * 50)
add_jobs = input("Add sample jobs? (y/n, default: y): ").strip().lower() or "y"

if add_jobs == 'y':
    created_count = 0
    for job_data in jobs_data:
        job, created = Job.objects.get_or_create(
            title=job_data['title'],
            company=job_data['company'],
            defaults={
                'location': job_data['location'],
                'job_type': job_data['job_type'],
                'skills_required': job_data['skills_required'],
                'apply_link': job_data['apply_link'],
                'last_date': job_data['last_date'],
                'posted_by': admin_user
            }
        )
        if created:
            created_count += 1
            print(f"✓ Created: {job.title} at {job.company}")
        else:
            print(f"- Already exists: {job.title} at {job.company}")

    print(f"\n✓ Added {created_count} new jobs")
    print(f"✓ Total jobs in database: {Job.objects.count()}")

print("\n" + "=" * 50)
print("Setup Complete!")
print("=" * 50)
print(f"\nYou can now login at: http://localhost:8000/login/")
print(f"Username: {admin_username}")
print(f"Password: {admin_password}")
print("\n")
