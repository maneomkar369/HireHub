# 🎓 HireHub - Campus Recruitment Portal

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0+-38B2AC.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**A modern, feature-rich campus recruitment management system connecting students with recruiters.**

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [License](#-license)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Database Schema](#-database-schema)
- [Installation Guide](#-installation-guide)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## 🌟 Overview

**HireHub** is a comprehensive web-based platform designed to streamline the campus recruitment process. It bridges the gap between students seeking opportunities and recruiters looking for talented candidates. The platform provides role-based dashboards, application tracking, skill matching algorithms, and professional resume management.

### Key Highlights

- 🎯 **Role-Based Access**: Separate dashboards for Students, Recruiters, and Admins
- 🔍 **Smart Job Matching**: AI-powered skill matching algorithm
- 📊 **Analytics Dashboard**: Real-time statistics and insights
- 📄 **Resume Management**: Professional resume viewing and printing
- 🚀 **Project Showcase**: GitHub-style project portfolio for students
- 📧 **Email Integration**: Direct communication between recruiters and candidates
- 🔐 **Secure Authentication**: Django's built-in authentication system
- 📱 **Responsive Design**: Mobile-first approach using TailwindCSS

---

## ✨ Features

### For Students

- ✅ **Profile Management**
  - Personal information, education, and skills
  - Portfolio links (GitHub, LinkedIn, Personal Website)
  - Project showcase with technologies and descriptions
  - Certifications and achievements

- ✅ **Job Discovery**
  - Browse available job listings
  - Advanced search and filtering
  - Skill-based job recommendations
  - Application tracking and status updates

- ✅ **Application Management**
  - One-click job applications
  - Track application status (Pending, Shortlisted, Interviewed, Accepted, Rejected)
  - View application history

### For Recruiters

- ✅ **Job Posting**
  - Create and manage job listings
  - Specify required skills and qualifications
  - Set application deadlines
  - Add external application links

- ✅ **Applicant Management**
  - View applications in professional resume format
  - Skill match percentage analysis
  - Filter and search candidates
  - Update application status
  - Add recruiter notes

- ✅ **Communication**
  - Direct email integration
  - Pre-filled email templates
  - Contact applicants easily

- ✅ **Analytics**
  - Total jobs posted
  - Application statistics
  - Average applications per job

### For Administrators

- ✅ **User Management**
  - Approve/reject recruiter accounts
  - Manage student profiles
  - View system-wide statistics

- ✅ **Platform Oversight**
  - Monitor all job postings
  - View all applications
  - Generate reports

---

## 🛠 Technology Stack

### Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8+ | Core programming language |
| **Django** | 4.2+ | Web framework |
| **PostgreSQL** | 13+ | Primary database (Production) |
| **SQLite** | 3.x | Development database |

### Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| **HTML5** | - | Structure |
| **TailwindCSS** | 3.0+ | Styling framework |
| **Alpine.js** | 3.x | Lightweight JavaScript framework |
| **CSS3** | - | Custom styling |

### Development Tools

| Tool | Purpose |
|------|---------|
| **Git** | Version control |
| **pip** | Package management |
| **venv** | Virtual environment |
| **Django Debug Toolbar** | Development debugging |

### External Services

- **Email Service**: SMTP (configurable)
- **Static Files**: Django static files handler
- **Media Storage**: Local file system (configurable for cloud)

---

## 🏗 System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Layer (Browser)                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │ Student  │  │Recruiter │  │  Admin   │  │  Public  │     │
│  │Dashboard │  │Dashboard │  │Dashboard │  │  Pages   │     │  
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘     │
└─────────────────────────────────────────────────────────────┘
                            ↓ HTTPS
┌─────────────────────────────────────────────────────────────┐
│                   Presentation Layer                        │
│  ┌────────────────────────────────────────────────────┐     │
│  │         Django Templates (HTML/TailwindCSS)        │     │
│  │  • Jinja2 Template Engine                          │     │
│  │  • Component-based Design                          │     │
│  │  • Responsive Layouts                              │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Application Layer                         │
│  ┌────────────────────────────────────────────────────┐     │
│  │              Django Application (MVT)              │     │
│  │                                                    │     │
│  │  ┌──────────┐  ┌────────────┐   ┌──────────┐       │     │
│  │  │  Views   │  │  Forms     │   │  URLs    │       │     │
│  │  │ (Logic)  │  │(Validation)│   │(Routing) │       │     │
│  │  └──────────┘  └────────────┘   └──────────┘       │     │
│  │                                                    │     │
│  │  ┌────────────────────────────────────────┐        │     │
│  │  │       Business Logic Layer             │        │     │
│  │  │  • Authentication & Authorization      │        │     │
│  │  │  • Skill Matching Algorithm            │        │     │
│  │  │  • Application Status Management       │        │     │
│  │  │  • Email Notifications                 │        │     │
│  │  └────────────────────────────────────────┘        │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Data Access Layer                        │
│  ┌────────────────────────────────────────────────────┐     │
│  │              Django ORM (Models)                   │     │
│  │                                                    │     │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │     │
│  │  │  User    │  │ Profile  │  │   Job    │          │     │
│  │  │  Model   │  │  Model   │  │  Model   │          │     │
│  │  └──────────┘  └──────────┘  └──────────┘          │     │
│  │                                                    │     │
│  │  ┌──────────┐                                      │     │
│  │  │Application│                                     │     │
│  │  │  Model   │                                      │     │
│  │  └──────────┘                                      │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Database Layer                           │
│  ┌────────────────────────────────────────────────────┐     │
│  │         PostgreSQL / SQLite Database               │     │
│  │                                                    │     │
│  │  Tables:                                           │     │
│  │  • auth_user                                       │     │
│  │  • jobs_profile                                    │     │
│  │  • jobs_job                                        │     │
│  │  • jobs_application                                │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

### Application Flow

```
User Request → URL Router → View → Business Logic → Model → Database
                                      ↓
                                   Template
                                      ↓
                                   Response
```

---

## 🗄 Database Schema

### Entity Relationship Diagram

```
┌─────────────────────┐
│      auth_user      │
│─────────────────────│
│ • id (PK)           │
│ • username          │
│ • email             │
│ • password          │
│ • first_name        │
│ • last_name         │
│ • is_active         │
│ • date_joined       │
└─────────────────────┘
          │
          │ 1:1
          ↓
┌─────────────────────┐
│    jobs_profile     │
│─────────────────────│
│ • id (PK)           │
│ • user_id (FK)      │
│ • role              │
│ • phone             │
│ • course            │
│ • skills (JSON)     │
│ • about             │
│ • projects (JSON)   │
│ • certifications    │
│ • github_url        │
│ • linkedin_url      │
│ • portfolio_url     │
│ • company_name      │
│ • is_approved       │
└─────────────────────┘
          │
          │ 1:N (for recruiters)
          ↓
┌─────────────────────┐
│      jobs_job       │
│─────────────────────│
│ • id (PK)           │
│ • posted_by (FK)    │
│ • title             │
│ • company           │
│ • description       │
│ • location          │
│ • job_type          │
│ • skills_required   │
│   (JSON)            │
│ • apply_link        │
│ • last_date         │
│ • views_count       │
│ • created_at        │
│ • updated_at        │
└─────────────────────┘
          │
          │ 1:N
          ↓
┌─────────────────────┐
│  jobs_application   │
│─────────────────────│
│ • id (PK)           │
│ • user_id (FK)      │
│ • job_id (FK)       │
│ • status            │
│ • cover_letter      │
│ • recruiter_notes   │
│ • applied_at        │
│ • updated_at        │
└─────────────────────┘
```

### Table Descriptions

#### User Table (Django's auth_user)
- **Purpose**: Core user authentication
- **Fields**: Basic user information, credentials
- **Relationships**: One-to-one with Profile

#### Profile Table (jobs_profile)
- **Purpose**: Extended user information
- **Fields**: 
  - Role-specific data (student/recruiter/admin)
  - Skills, projects, certifications (JSON fields)
  - Portfolio links
  - Company information (for recruiters)
- **Relationships**: 
  - One-to-one with User
  - One-to-many with Job (for recruiters)

#### Job Table (jobs_job)
- **Purpose**: Job postings
- **Fields**: 
  - Job details (title, description, location)
  - Required skills (JSON array)
  - Application deadline
  - View counter
- **Relationships**: 
  - Many-to-one with Profile (posted_by)
  - One-to-many with Application

#### Application Table (jobs_application)
- **Purpose**: Track job applications
- **Fields**: 
  - Application status
  - Cover letter
  - Recruiter notes
  - Timestamps
- **Relationships**: 
  - Many-to-one with User
  - Many-to-one with Job

---

## 📦 Installation Guide

### Prerequisites

Before installing HireHub, ensure you have:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (included with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **PostgreSQL 13+** (for production) - [Download PostgreSQL](https://www.postgresql.org/download/)
- **Virtual environment tool** (venv, included with Python)

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/hirehub.git

# Navigate to project directory
cd hirehub
cd campusconnect
```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment

# On Linux/Mac:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install these packages:

```bash
pip install django==4.2
pip install psycopg2-binary  # For PostgreSQL
pip install python-decouple   # For environment variables
pip install pillow            # For image handling
```

### Step 4: Environment Configuration

Create a `.env` file in the project root (hirehub/):

```bash
# Create .env file
touch .env
```

Add the following configuration to `.env`:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (PostgreSQL for production)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=hirehub_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# For development, use SQLite (comment out PostgreSQL above)
# DB_ENGINE=django.db.backends.sqlite3
# DB_NAME=db.sqlite3

# Email Configuration (Optional)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Static Files
STATIC_URL=/static/
STATIC_ROOT=staticfiles/
MEDIA_URL=/media/
MEDIA_ROOT=media/
```

### Step 5: Database Setup

#### For SQLite (Development)

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate
```

#### For PostgreSQL (Production)

```bash
# Create PostgreSQL database
createdb hirehub_db

# Or use psql:
psql -U postgres
CREATE DATABASE hirehub_db;
\q

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser

```bash
# Create admin account
python manage.py createsuperuser

# Follow prompts:
# Username: admin
# Email: admin@hirehub.com
# Password: (enter secure password)
```

### Step 7: Collect Static Files

```bash
# Collect static files
python manage.py collectstatic --noinput
```

### Step 8: Run Development Server

```bash
# Start the development server
python manage.py runserver

# Server will start at http://127.0.0.1:8000/
```

### Step 9: Access the Application

Open your browser and navigate to:

- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Student Dashboard**: http://127.0.0.1:8000/dashboard/
- **Recruiter Dashboard**: http://127.0.0.1:8000/recruiter/dashboard/

---

## ⚙️ Configuration

### Settings Overview

The project uses Django settings located in `campusconnect/settings.py`:

```python
# Key configuration sections:

# Security
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Database
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Email Configuration

For email functionality, configure SMTP settings in `.env`:

**Gmail Example:**
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

> **Note**: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833)

### Production Settings

For production deployment, ensure:

1. **Set DEBUG to False**
   ```env
   DEBUG=False
   ```

2. **Generate Strong SECRET_KEY**
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

3. **Configure ALLOWED_HOSTS**
   ```env
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

4. **Use PostgreSQL Database**
   ```env
   DB_ENGINE=django.db.backends.postgresql
   ```

5. **Set up HTTPS**
   ```python
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

---

## 📖 Usage Guide

### For Students

#### 1. Registration
- Navigate to the registration page
- Select "Student" as role
- Fill in your details
- Verify your email (if configured)

#### 2. Profile Setup
- Go to your dashboard
- Click "Update Profile"
- Add your:
  - Personal information
  - Skills (comma-separated)
  - Projects (format: Title | Description | Technologies | Link)
  - Portfolio links (GitHub, LinkedIn, Website)
  - Certifications

#### 3. Job Search
- Browse available jobs
- Use filters to search by:
  - Job type
  - Location
  - Skills
- Click "View Details" to see full job description

#### 4. Applying for Jobs
- Click "Apply Now" on job listing
- Optionally add a cover letter
- Track application status in your dashboard

### For Recruiters

#### 1. Registration & Approval
- Register as "Recruiter"
- Wait for admin approval
- Receive notification when approved

#### 2. Posting Jobs
- Go to Recruiter Dashboard
- Click "Post Job" tab
- Fill in job details:
  - Title and company
  - Description
  - Location and job type
  - Required skills (comma-separated)
  - Application deadline

#### 3. Managing Applications
- View all applications in "Applications" tab
- Filter by status
- Review candidate resumes
- Update application status:
  - Pending → Shortlisted
  - Shortlisted → Interviewed
  - Interviewed → Accepted/Rejected

#### 4. Contacting Candidates
- Click "Send Email" to contact applicant
- Pre-filled email templates available
- Print resumes for offline review

### For Admins

#### 1. Access Admin Panel
- Navigate to `/admin/`
- Login with superuser credentials

#### 2. User Management
- Approve/reject recruiter accounts
- View all user profiles
- Manage permissions

#### 3. Content Moderation
- Review job postings
- Monitor applications
- Handle reports

---

## 🔌 API Documentation

### Authentication Endpoints

```
POST /accounts/login/
POST /accounts/register/
POST /accounts/logout/
```

### Job Endpoints

```
GET  /jobs/                    # List all jobs
GET  /jobs/<id>/               # Job details
POST /jobs/apply/<id>/         # Apply to job
```

### Dashboard Endpoints

```
GET /dashboard/                     # Student dashboard
GET /recruiter/dashboard/           # Recruiter dashboard
GET /admin/dashboard/               # Admin dashboard
```

### Profile Endpoints

```
GET  /profile/update/               # View/update profile
POST /profile/update/               # Save profile changes
```

---

## 🤝 Contributing

We welcome contributions to HireHub! Here's how you can help:

### Getting Started

1. **Fork the Repository**
   ```bash
   # Click 'Fork' on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/yourusername/hirehub.git
   cd hirehub
   cd campusconnect
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**
   - Write clean, documented code
   - Follow PEP 8 style guide
   - Add tests for new features

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

6. **Push to GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

For support and questions:

- **GitHub Issues**: https://github.com/yourusername/hirehub/issues
- **Email**: support@hirehub.com
- **Documentation**: See [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)

---

**Made with ❤️ by the HireHub Team**