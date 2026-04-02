# 🚀 Quick Start Guide

Get HireHub up and running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- Git installed
- 10-15 minutes of your time ⏰

---

## Installation Steps

### 1️⃣ Clone and Navigate

```bash
git clone https://github.com/yourusername/hirehub.git
cd hirehub
cd campusconnect
```

### 2️⃣ Create Virtual Environment

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Set Up Database

```bash
python manage.py migrate
```

### 5️⃣ Create Admin Account

```bash
python manage.py createsuperuser

# Enter:
# Username: admin
# Email: admin@example.com
# Password: (your secure password)
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

### 7️⃣ Access Application

Open your browser and go to:

- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## First Steps After Installation

### As Admin

1. Go to: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Explore the admin panel

### As Student

1. Click "Register" on homepage
2. Select "Student" as role
3. Fill in registration details
4. Login and complete your profile
5. Start browsing jobs!

### As Recruiter

1. Click "Register" on homepage
2. Select "Recruiter" as role
3. Fill in company details
4. Wait for admin approval
5. Login and start posting jobs!

---

## Common Commands

```bash
# Start server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Django shell
python manage.py shell
```

---

## Project Structure

```
hirehub/
├── campusconnect/        # Django project configuration
│   ├── settings.py       # Settings (campusconnect.settings)
│   ├── urls.py           # URL routing
│   ├── asgi.py           # ASGI config
│   └── wsgi.py           # WSGI config
├── jobs/                 # Main app
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── forms.py          # Form handling
│   ├── urls.py           # App URLs
│   └── templates/        # HTML templates
├── static/               # Static files (CSS, JS)
├── media/                # User uploads
├── manage.py             # Django management
└── requirements.txt      # Dependencies
```

---

## Key Features to Try

### 1. Student Profile
- Add your skills (comma-separated)
- Create projects in format: `Title | Description | Technologies | Link`
- Add GitHub, LinkedIn, Portfolio links

### 2. Job Posting (Recruiter)
- Post a job with required skills
- View applications in resume format
- Update application status

### 3. Application Process (Student)
- Browse available jobs
- Apply with one click
- Track application status

---

## Sample Data

### Sample Skills
```
Python, Django, JavaScript, React, PostgreSQL, Git, HTML, CSS, 
TailwindCSS, REST API, Machine Learning, Data Science
```

### Sample Project Format
```
E-commerce Platform | Full-stack online store with payment integration | Django, React, PostgreSQL, Stripe | https://github.com/user/project

Weather Dashboard | Real-time weather app with geolocation | JavaScript, HTML, CSS, OpenWeather API | https://weather-app.vercel.app

Task Manager API | RESTful API with authentication | Node.js, Express, MongoDB | https://github.com/user/api
```

---

## Troubleshooting

### Port Already in Use

```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or use different port
python manage.py runserver 8080
```

### Database Locked (SQLite)

```bash
# Remove database and recreate
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Module Not Found

```bash
# Reinstall requirements
pip install -r requirements.txt
```

### Static Files Not Loading

```bash
# Collect static files
python manage.py collectstatic --clear --no-input
```

---

## Next Steps

📚 **Read Full Documentation:**
- [README.md](README.md) - Complete guide
- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [DEPLOYMENT.md](DEPLOYMENT.md) - Production deployment

🎓 **Learn More:**
- Django Documentation: https://docs.djangoproject.com/
- TailwindCSS: https://tailwindcss.com/docs
- PostgreSQL: https://www.postgresql.org/docs/

🤝 **Get Help:**
- Open an issue on GitHub
- Join our Discord community
- Email: support@hirehub.com

---

## Demo Accounts (After Setup)

Create these accounts for testing:

### Student Account
```
Username: student1
Email: student@test.com
Password: Test123!@#
Role: Student
```

### Recruiter Account
```
Username: recruiter1
Email: recruiter@company.com
Password: Test123!@#
Role: Recruiter
Company: Tech Corp
```

---

## Quick Configuration

### Enable Email (Optional)

Create `.env` file in project root:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Use PostgreSQL (Optional)

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=hirehub_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Development Tips

### Auto-reload Server

The development server auto-reloads when you save files.

### Django Shell

```bash
python manage.py shell

>>> from jobs.models import Job, Profile
>>> jobs = Job.objects.all()
>>> print(jobs.count())
```

### Create Test Data

```bash
python manage.py shell

>>> from django.contrib.auth.models import User
>>> from jobs.models import Profile, Job

# Create test user
>>> user = User.objects.create_user('testuser', 'test@test.com', 'testpass')
>>> Profile.objects.create(user=user, role='student', skills=['Python', 'Django'])
```

---

## Useful Links

- **Documentation**: [README.md](README.md)
- **License**: [LICENSE](LICENSE)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)
- **Issues**: https://github.com/yourusername/hirehub/issues
- **Wiki**: https://github.com/yourusername/hirehub/wiki

---

**🎉 Congratulations! You're all set up!**

Start exploring HireHub and building your campus recruitment platform.

Need help? Check out our [full documentation](README.md) or open an issue on GitHub.

---

**Made with ❤️ by the HireHub Team**