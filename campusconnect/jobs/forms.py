from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Job, Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[('student', 'Student'), ('recruiter', 'Recruiter')], required=True)
    company_name = forms.CharField(max_length=200, required=False, help_text='Required for recruiters')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                role=self.cleaned_data['role'],
                company_name=self.cleaned_data.get('company_name', '')
            )
        return user

class JobForm(forms.ModelForm):
    # Override skills_required to use CharField instead of JSONField for form input
    skills_required = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter skills as comma-separated values (e.g., Python, Django, REST API)',
            'rows': 3,
            'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200'
        }),
        required=True,
        label='Skills Required',
        help_text='Enter skills separated by commas'
    )
    
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'job_type', 'description', 'skills_required', 'apply_link', 'last_date']
        widgets = {
            'last_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Job description and requirements', 'rows': 5}),
        }

    def clean_skills_required(self):
        """Convert comma-separated string to list for JSONField"""
        skills = self.cleaned_data.get('skills_required', '')
        if isinstance(skills, str):
            # Split by comma and clean up whitespace
            skills_list = [s.strip() for s in skills.split(',') if s.strip()]
            if not skills_list:
                raise forms.ValidationError('Please enter at least one skill.')
            return skills_list
        elif isinstance(skills, list):
            # Already a list, just clean it up
            return [str(s).strip() for s in skills if s]
        return []

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['course', 'about', 'github_url', 'linkedin_url', 'portfolio_url', 'resume']
        widgets = {
            'course': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'e.g., Computer Science, Engineering'
            }),
            'about': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 resize-vertical',
                'placeholder': 'Tell us about yourself, your interests, and career goals',
                'rows': 4
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'https://github.com/yourusername'
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'https://linkedin.com/in/yourprofile'
            }),
            'portfolio_url': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'https://yourportfolio.com'
            }),
            'resume': forms.FileInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'accept': '.pdf,.doc,.docx,.txt'
            }),
        }
    
    # Define skills as a separate CharField to avoid JSON validation
    skills = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 resize-vertical',
            'placeholder': 'Enter your skills separated by commas (e.g., Python, JavaScript, Data Analysis)',
            'rows': 3
        }),
        required=False,
        label='Skills',
        help_text='Enter your skills separated by commas'
    )
    
    projects = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-vertical',
            'placeholder': 'Enter projects in JSON format or use the format:\nTitle | Description | Technologies | Link\n\nExample:\nE-commerce Website | Built a full-stack online store with payment integration | Django, React, PostgreSQL | https://github.com/user/ecommerce\nWeather App | Real-time weather application using API | JavaScript, HTML, CSS | https://weather-app.com',
            'rows': 8
        }),
        required=False,
        label='Projects',
        help_text='Enter each project on a new line. Format: Title | Description | Technologies | Link (optional)'
    )
    
    certifications = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 resize-vertical',
            'placeholder': 'Enter your certifications, one per line\nExample:\nAWS Certified Solutions Architect - 2023\nGoogle Data Analytics Professional Certificate - 2024',
            'rows': 4
        }),
        required=False,
        label='Certifications',
        help_text='List your professional certifications, one per line'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Convert skills list to comma-separated string for display
        if self.instance and self.instance.pk:
            skills_data = self.instance.skills
            if isinstance(skills_data, list):
                self.fields['skills'].initial = ', '.join(skills_data)
            elif skills_data:
                self.fields['skills'].initial = str(skills_data)
            
            # Convert projects list to formatted string for display
            projects_data = self.instance.projects
            if isinstance(projects_data, list) and projects_data:
                # Convert structured project data to display format
                project_lines = []
                for proj in projects_data:
                    if isinstance(proj, dict):
                        # Structured format: dict with title, description, technologies, link
                        title = proj.get('title', '')
                        description = proj.get('description', '')
                        technologies = proj.get('technologies', '')
                        if isinstance(technologies, list):
                            technologies = ', '.join(technologies)
                        link = proj.get('link', '')
                        project_lines.append(f"{title} | {description} | {technologies} | {link}")
                    else:
                        # Old format: simple string
                        project_lines.append(str(proj))
                self.fields['projects'].initial = '\n'.join(project_lines)
            elif projects_data:
                self.fields['projects'].initial = str(projects_data)
            
            # Convert certifications list to line-separated string for display
            certifications_data = self.instance.certifications
            if isinstance(certifications_data, list) and certifications_data:
                self.fields['certifications'].initial = '\n'.join(certifications_data)
            elif certifications_data:
                self.fields['certifications'].initial = str(certifications_data)

    def clean_skills(self):
        skills = self.cleaned_data.get('skills', '')
        if isinstance(skills, str):
            # Split by comma and clean up whitespace
            skills_list = [s.strip() for s in skills.split(',') if s.strip()]
            return skills_list
        return skills if skills else []
    
    def clean_projects(self):
        projects = self.cleaned_data.get('projects', '')
        if isinstance(projects, str):
            # Parse structured project format
            projects_list = []
            for line in projects.split('\n'):
                line = line.strip()
                if not line:
                    continue
                
                # Try to parse structured format: Title | Description | Technologies | Link
                if '|' in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 3:
                        project_dict = {
                            'title': parts[0],
                            'description': parts[1],
                            'technologies': [t.strip() for t in parts[2].split(',') if t.strip()],
                            'link': parts[3] if len(parts) > 3 and parts[3] else ''
                        }
                        projects_list.append(project_dict)
                    else:
                        # Not enough parts, save as simple string
                        projects_list.append(line)
                else:
                    # Old format: simple string
                    projects_list.append(line)
            
            return projects_list
        return projects if projects else []
    
    def clean_certifications(self):
        certifications = self.cleaned_data.get('certifications', '')
        if isinstance(certifications, str):
            # Split by newline and clean up whitespace
            certifications_list = [c.strip() for c in certifications.split('\n') if c.strip()]
            return certifications_list
        return certifications if certifications else []
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Save the cleaned skills, projects, and certifications data
        instance.skills = self.cleaned_data.get('skills', [])
        instance.projects = self.cleaned_data.get('projects', [])
        instance.certifications = self.cleaned_data.get('certifications', [])
        if commit:
            instance.save()
        return instance