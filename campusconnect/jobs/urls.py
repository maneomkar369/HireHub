from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs_list, name='jobs_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/save/', views.save_job, name='save_job'),
    path('job/<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('settings/', views.settings, name='settings'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/job/add/', views.add_job, name='add_job'),
    path('admin/job/<int:pk>/edit/', views.edit_job, name='edit_job'),
    path('admin/job/<int:pk>/delete/', views.delete_job, name='delete_job'),
    path('admin/job/<int:pk>/applicants/', views.view_applicants, name='view_applicants'),
    path('export/applications/', views.export_applications, name='export_applications'),
    path('export/students/', views.export_students, name='export_students'),
    # Recruiter URLs
    path('recruiter/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('recruiter/job/add/', views.recruiter_add_job, name='recruiter_add_job'),
    path('recruiter/job/<int:pk>/edit/', views.recruiter_edit_job, name='recruiter_edit_job'),
    path('recruiter/job/<int:pk>/delete/', views.recruiter_delete_job, name='recruiter_delete_job'),
    path('recruiter/job/<int:pk>/applicants/', views.recruiter_view_applicants, name='recruiter_view_applicants'),
    path('recruiter/application/<int:pk>/status/', views.update_application_status, name='update_application_status'),
]