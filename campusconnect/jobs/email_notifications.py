from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_application_notification_to_recruiter(application):
    """Send email to recruiter when a student applies"""
    recruiter = application.job.posted_by
    student = application.user
    job = application.job
    
    subject = f'New Application: {student.username} applied for {job.title}'
    
    html_message = f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                <h2 style="color: #2563eb;">New Job Application Received!</h2>
                
                <p>Hello <strong>{recruiter.username}</strong>,</p>
                
                <p>You have received a new application for your job posting:</p>
                
                <div style="background-color: #f3f4f6; padding: 15px; border-radius: 5px; margin: 20px 0;">
                    <h3 style="margin-top: 0; color: #1f2937;">Job Details:</h3>
                    <p><strong>Position:</strong> {job.title}</p>
                    <p><strong>Company:</strong> {job.company}</p>
                    <p><strong>Location:</strong> {job.location}</p>
                </div>
                
                <div style="background-color: #eff6ff; padding: 15px; border-radius: 5px; margin: 20px 0;">
                    <h3 style="margin-top: 0; color: #1e40af;">Applicant Details:</h3>
                    <p><strong>Name:</strong> {student.username}</p>
                    <p><strong>Email:</strong> {student.email}</p>
                    <p><strong>Applied on:</strong> {application.applied_at.strftime('%B %d, %Y at %I:%M %p')}</p>
                </div>
                
                <p>Login to your recruiter dashboard to view the complete profile and application details.</p>
                
                <div style="text-align: center; margin: 30px 0;">
                    <a href="{settings.SITE_URL}/recruiter/job/{job.pk}/applicants/" 
                       style="background-color: #2563eb; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block;">
                        View Application
                    </a>
                </div>
                
                <p style="color: #6b7280; font-size: 14px; margin-top: 30px;">
                    This is an automated notification from HireHub Job Portal.
                </p>
            </div>
        </body>
    </html>
    """
    
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recruiter.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


def send_status_update_to_student(application):
    """Send email to student when application status changes"""
    student = application.user
    job = application.job
    status = application.get_status_display()
    
    # Status-specific messaging
    status_messages = {
        'pending': {
            'color': '#f59e0b',
            'message': 'Your application is under review.',
        },
        'shortlisted': {
            'color': '#10b981',
            'message': 'Congratulations! You have been shortlisted for the next round.',
        },
        'interviewed': {
            'color': '#3b82f6',
            'message': 'Your interview has been recorded. We will get back to you soon.',
        },
        'accepted': {
            'color': '#10b981',
            'message': 'Congratulations! Your application has been accepted!',
        },
        'rejected': {
            'color': '#ef4444',
            'message': 'Thank you for your interest. Unfortunately, we have decided to move forward with other candidates.',
        },
    }
    
    status_info = status_messages.get(application.status, {'color': '#6b7280', 'message': 'Your application status has been updated.'})
    
    subject = f'Application Status Update: {job.title} - {status}'
    
    html_message = f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                <h2 style="color: #2563eb;">Application Status Update</h2>
                
                <p>Hello <strong>{student.username}</strong>,</p>
                
                <p>The status of your application has been updated:</p>
                
                <div style="background-color: #f3f4f6; padding: 15px; border-radius: 5px; margin: 20px 0;">
                    <h3 style="margin-top: 0; color: #1f2937;">Job Details:</h3>
                    <p><strong>Position:</strong> {job.title}</p>
                    <p><strong>Company:</strong> {job.company}</p>
                    <p><strong>Location:</strong> {job.location}</p>
                </div>
                
                <div style="background-color: {status_info['color']}15; padding: 20px; border-left: 4px solid {status_info['color']}; border-radius: 5px; margin: 20px 0;">
                    <h3 style="margin-top: 0; color: {status_info['color']};">Status: {status}</h3>
                    <p style="margin: 0;">{status_info['message']}</p>
                </div>
                
                {f'<div style="background-color: #fef3c7; padding: 15px; border-radius: 5px; margin: 20px 0;"><p style="margin: 0;"><strong>Note from Recruiter:</strong><br>{application.recruiter_notes}</p></div>' if application.recruiter_notes else ''}
                
                <p>Login to your dashboard to view more details.</p>
                
                <div style="text-align: center; margin: 30px 0;">
                    <a href="{settings.SITE_URL}/dashboard/" 
                       style="background-color: #2563eb; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block;">
                        View Dashboard
                    </a>
                </div>
                
                <p style="color: #6b7280; font-size: 14px; margin-top: 30px;">
                    This is an automated notification from HireHub Job Portal.
                </p>
            </div>
        </body>
    </html>
    """
    
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[student.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


def send_new_job_notification(job, matching_students):
    """Send email to students when a new job matching their skills is posted"""
    for student_profile in matching_students:
        student = student_profile.user
        match_percentage = student_profile.skill_match_percentage(job)
        
        subject = f'New Job Match: {job.title} at {job.company} ({match_percentage}% match)'
        
        html_message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                    <h2 style="color: #2563eb;">New Job Opportunity Matching Your Skills!</h2>
                    
                    <p>Hello <strong>{student.username}</strong>,</p>
                    
                    <p>We found a new job opportunity that matches your skills profile:</p>
                    
                    <div style="background-color: #f3f4f6; padding: 15px; border-radius: 5px; margin: 20px 0;">
                        <h3 style="margin-top: 0; color: #1f2937;">{job.title}</h3>
                        <p><strong>Company:</strong> {job.company}</p>
                        <p><strong>Location:</strong> {job.location}</p>
                        <p><strong>Job Type:</strong> {job.job_type}</p>
                        <p><strong>Last Date:</strong> {job.last_date.strftime('%B %d, %Y')}</p>
                    </div>
                    
                    <div style="background-color: #d1fae5; padding: 15px; border-radius: 5px; margin: 20px 0;">
                        <h4 style="margin-top: 0; color: #065f46;">Skill Match: {match_percentage}%</h4>
                        <p style="margin: 0;">Your skills align well with this position!</p>
                    </div>
                    
                    {f'<div style="margin: 20px 0;"><p><strong>Job Description:</strong></p><p>{job.description[:200]}...</p></div>' if job.description else ''}
                    
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="{settings.SITE_URL}/job/{job.pk}/" 
                           style="background-color: #10b981; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block;">
                            View Job & Apply
                        </a>
                    </div>
                    
                    <p style="color: #6b7280; font-size: 14px; margin-top: 30px;">
                        You received this because your skills match the job requirements. 
                        Update your profile preferences to manage notifications.
                    </p>
                </div>
            </body>
        </html>
        """
        
        plain_message = strip_tags(html_message)
        
        try:
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[student.email],
                html_message=html_message,
                fail_silently=True,
            )
        except Exception as e:
            print(f"Failed to send email to {student.email}: {e}")
            continue
    
    return True
