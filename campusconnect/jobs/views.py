from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
import csv
from .models import Job, Profile, SavedJob, Application
from .forms import CustomUserCreationForm, JobForm, ProfileForm

def home(request):
    jobs = Job.objects.all().order_by('-created_at')[:6]
    return render(request, 'jobs/home.html', {'jobs': jobs})

def jobs_list(request):
    jobs = Job.objects.all()
    query = request.GET.get('q')
    location = request.GET.get('location')
    job_type = request.GET.get('job_type')
    if query:
        jobs = jobs.filter(Q(title__icontains=query) | Q(company__icontains=query) | Q(skills_required__icontains=query))
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type__icontains=job_type)
    return render(request, 'jobs/jobs_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    # Track job views (increment counter)
    if request.user.is_authenticated and not request.user.is_staff:
        job.views_count += 1
        job.save(update_fields=['views_count'])
    
    is_saved = False
    is_applied = False
    eligibility = None
    skill_match = 0
    
    if request.user.is_authenticated:
        is_saved = SavedJob.objects.filter(user=request.user, job=job).exists()
        is_applied = Application.objects.filter(user=request.user, job=job).exists()
        try:
            profile = Profile.objects.get(user=request.user)
            skill_match = profile.skill_match_percentage(job)
            
            if skill_match >= 80:
                eligibility = 'match'
            elif skill_match >= 40:
                eligibility = 'partial'
            else:
                eligibility = 'none'
        except Profile.DoesNotExist:
            eligibility = 'none'
    
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'is_saved': is_saved,
        'is_applied': is_applied,
        'eligibility': eligibility,
        'skill_match': skill_match
    })

@login_required
def save_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    SavedJob.objects.get_or_create(user=request.user, job=job)
    messages.success(request, 'Job saved!')
    return redirect('job_detail', pk=pk)

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    application, created = Application.objects.get_or_create(user=request.user, job=job)
    
    if created:
        # Send email notification to recruiter
        from .email_notifications import send_application_notification_to_recruiter
        send_application_notification_to_recruiter(application)
        messages.success(request, 'Application submitted successfully! The recruiter has been notified.')
    else:
        messages.info(request, 'You have already applied for this job.')
    
    return redirect('job_detail', pk=pk)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'jobs/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'jobs/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    # Redirect admins to admin dashboard
    if request.user.is_staff:
        return redirect('admin_dashboard')
    
    # Get user profile
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Redirect recruiters to recruiter dashboard
    if profile.role == 'recruiter':
        return redirect('recruiter_dashboard')
    
    # Student dashboard with enhanced features
    saved_jobs = SavedJob.objects.filter(user=request.user).select_related('job')
    applied_jobs = Application.objects.filter(user=request.user).select_related('job').order_by('-applied_at')
    
    # Get job recommendations based on skills
    recommended_jobs = []
    if profile.skills:
        from django.db.models import Q
        from django.utils import timezone
        
        # Find jobs that match user's skills and are still open
        all_jobs = Job.objects.filter(
            status='open',
            last_date__gte=timezone.now().date()
        ).exclude(
            application__user=request.user  # Exclude already applied jobs
        )
        
        # Calculate match percentage and filter
        for job in all_jobs:
            match_percentage = profile.skill_match_percentage(job)
            if match_percentage >= 30:  # At least 30% match
                job.match_percentage = match_percentage
                recommended_jobs.append(job)
        
        # Sort by match percentage
        recommended_jobs.sort(key=lambda x: x.match_percentage, reverse=True)
        recommended_jobs = recommended_jobs[:5]  # Top 5 recommendations
    
    # Application status summary
    status_summary = {
        'pending': applied_jobs.filter(status='pending').count(),
        'shortlisted': applied_jobs.filter(status='shortlisted').count(),
        'interviewed': applied_jobs.filter(status='interviewed').count(),
        'accepted': applied_jobs.filter(status='accepted').count(),
        'rejected': applied_jobs.filter(status='rejected').count(),
    }
    
    return render(request, 'jobs/dashboard.html', {
        'profile': profile,
        'saved_jobs': saved_jobs,
        'applied_jobs': applied_jobs,
        'recommended_jobs': recommended_jobs,
        'status_summary': status_summary,
    })

@login_required
def profile_update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'jobs/profile_update.html', {'form': form})

@login_required
def settings(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'jobs/settings.html', {'form': form})

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    jobs = Job.objects.all().prefetch_related('application_set')
    students = Profile.objects.filter(role='student').select_related('user')
    total_applications = Application.objects.count()
    return render(request, 'jobs/admin_dashboard.html', {
        'jobs': jobs,
        'students': students,
        'total_applications': total_applications
    })

@login_required
def add_job(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Job added!')
            return redirect('admin_dashboard')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})

@login_required
def edit_job(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated!')
            return redirect('admin_dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/edit_job.html', {'form': form})

@login_required
def delete_job(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    job = get_object_or_404(Job, pk=pk)
    job.delete()
    messages.success(request, 'Job deleted!')
    return redirect('admin_dashboard')

@login_required
def view_applicants(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    job = get_object_or_404(Job, pk=pk)
    applications = Application.objects.filter(job=job).select_related('user__profile')
    return render(request, 'jobs/view_applicants.html', {'job': job, 'applications': applications})

@login_required
def export_applications(request):
    if not request.user.is_staff:
        return redirect('home')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="job_applications.csv"'
    writer = csv.writer(response)
    writer.writerow(['Job Title', 'Company', 'Applicant Username', 'Email', 'Applied At'])
    applications = Application.objects.select_related('job', 'user').all()
    for app in applications:
        writer.writerow([app.job.title, app.job.company, app.user.username, app.user.email, app.applied_at])
    return response

@login_required
def export_students(request):
    if not request.user.is_staff:
        return redirect('home')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'Course', 'Skills'])
    students = Profile.objects.filter(role='student').select_related('user')
    for student in students:
        skills = ', '.join(student.skills)
        writer.writerow([student.user.username, student.user.email, student.course, skills])
    return response

# Recruiter Views
@login_required
def recruiter_dashboard(request):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role != 'recruiter':
        return redirect('home')
    
    # Get recruiter's posted jobs
    my_jobs = Job.objects.filter(posted_by=request.user).prefetch_related('application_set')
    
    # Calculate statistics
    total_jobs = my_jobs.count()
    total_applications = Application.objects.filter(job__posted_by=request.user).count()
    
    # Get recent applications for recruiter's jobs
    recent_applications = Application.objects.filter(
        job__posted_by=request.user
    ).select_related('user__profile', 'job').order_by('-applied_at')[:10]
    
    return render(request, 'jobs/recruiter_dashboard.html', {
        'profile': profile,
        'my_jobs': my_jobs,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'recent_applications': recent_applications,
    })

@login_required
def recruiter_add_job(request):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role != 'recruiter':
        return redirect('home')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            # Set company name from recruiter's profile
            if not job.company:
                job.company = profile.company_name
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('recruiter_dashboard')
        else:
            # Show specific form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        # Pre-fill company name
        form = JobForm(initial={'company': profile.company_name})
    
    return render(request, 'jobs/recruiter_add_job.html', {'form': form, 'profile': profile})

@login_required
def recruiter_edit_job(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role != 'recruiter':
        return redirect('home')
    
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('recruiter_dashboard')
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/recruiter_edit_job.html', {'form': form, 'job': job, 'profile': profile})

@login_required
def recruiter_delete_job(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role != 'recruiter':
        return redirect('home')
    
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    job.delete()
    messages.success(request, 'Job deleted successfully!')
    return redirect('recruiter_dashboard')

@login_required
def recruiter_view_applicants(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role != 'recruiter':
        return redirect('home')
    
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    
    # Handle search and filter
    applications = Application.objects.filter(job=job).select_related('user__profile')
    
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    sort_by = request.GET.get('sort', '-applied_at')
    
    if search_query:
        applications = applications.filter(
            Q(user__username__icontains=search_query) |
            Q(user__email__icontains=search_query) |
            Q(user__profile__skills__icontains=search_query)
        )
    
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    # Sort by different criteria
    if sort_by == 'match':
        # Sort by skill match (calculated in template, so we get all and sort in Python)
        applications = sorted(applications, key=lambda a: a.skill_match_percentage(), reverse=True)
    elif sort_by == 'name':
        applications = applications.order_by('user__username')
    else:
        applications = applications.order_by(sort_by)
    
    return render(request, 'jobs/recruiter_view_applicants.html', {
        'job': job,
        'applications': applications,
        'profile': profile,
        'search_query': search_query,
        'status_filter': status_filter,
        'sort_by': sort_by
    })

@login_required
def update_application_status(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role != 'recruiter':
        return redirect('home')
    
    application = get_object_or_404(Application, pk=pk, job__posted_by=request.user)
    
    if request.method == 'POST':
        old_status = application.status
        new_status = request.POST.get('status')
        notes = request.POST.get('notes', '')
        
        if new_status in dict(Application.STATUS_CHOICES):
            application.status = new_status
            application.recruiter_notes = notes
            application.save()
            
            # Send email notification if status changed
            if old_status != new_status:
                from .email_notifications import send_status_update_to_student
                send_status_update_to_student(application)
            
            messages.success(request, f'Application status updated to {application.get_status_display()}')
        
        return redirect('recruiter_view_applicants', pk=application.job.pk)
    
    return redirect('recruiter_dashboard')
