# Architecture Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Architectural Patterns](#architectural-patterns)
3. [Component Diagram](#component-diagram)
4. [Data Flow](#data-flow)
5. [Security Architecture](#security-architecture)
6. [Scalability Considerations](#scalability-considerations)

---

## System Overview

HireHub follows the **Model-View-Template (MVT)** architectural pattern, which is Django's implementation of the MVC (Model-View-Controller) pattern.

### Core Components

```
┌─────────────────────────────────────────────────────────┐
│                    HireHub System                  │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   Models    │  │    Views    │  │  Templates  │    │
│  │  (Data)     │  │  (Logic)    │  │    (UI)     │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
│         │                 │                 │            │
│         └─────────────────┴─────────────────┘            │
│                           │                               │
│                    ┌──────▼──────┐                       │
│                    │  URL Router │                       │
│                    └─────────────┘                       │
└─────────────────────────────────────────────────────────┘
```

---

## Architectural Patterns

### 1. MVT (Model-View-Template)

#### Models
- Define database schema
- Handle data validation
- Implement business logic methods
- Examples: `User`, `Profile`, `Job`, `Application`

```python
# jobs/models.py
class Job(models.Model):
    title = models.CharField(max_length=200)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    skills_required = models.JSONField(default=list)
    
    def get_applicants_count(self):
        return self.application_set.count()
```

#### Views
- Process HTTP requests
- Execute business logic
- Query models
- Render templates

```python
# jobs/views.py
def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'jobs/jobs_list.html', {'jobs': jobs})
```

#### Templates
- Present data to users
- Handle user interactions
- Responsive design with TailwindCSS

```html
<!-- jobs/templates/jobs/jobs_list.html -->
{% for job in jobs %}
    <div class="job-card">
        <h3>{{ job.title }}</h3>
        <p>{{ job.company }}</p>
    </div>
{% endfor %}
```

### 2. Repository Pattern

Data access is abstracted through Django ORM:

```python
# Instead of raw SQL:
# SELECT * FROM jobs_job WHERE posted_by_id = 1

# Use ORM:
Job.objects.filter(posted_by=user)
```

### 3. Middleware Pattern

Django middleware processes requests/responses:

```
Request → Authentication → Session → CSRF → View → Response
```

---

## Component Diagram

```
┌───────────────────────────────────────────────────────────────┐
│                        Frontend Layer                          │
├───────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   Student    │  │  Recruiter   │  │    Admin     │       │
│  │  Interface   │  │  Interface   │  │  Interface   │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│         │                  │                  │                │
│         └──────────────────┴──────────────────┘                │
│                           │                                     │
└───────────────────────────┼─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                    Application Layer                         │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              URL Router & Dispatcher                 │    │
│  └─────────────────────────────────────────────────────┘    │
│                           │                                   │
│  ┌────────────────┬───────┴────────┬────────────────┐      │
│  │                │                │                │      │
│  ▼                ▼                ▼                ▼      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │  Auth    │  │   Job    │  │  Profile │  │  Admin   │  │
│  │  Views   │  │  Views   │  │  Views   │  │  Views   │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
│       │             │              │              │         │
└───────┼─────────────┼──────────────┼──────────────┼────────┘
        │             │              │              │
┌───────▼─────────────▼──────────────▼──────────────▼────────┐
│                    Business Logic Layer                      │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────┐ │
│  │ Authentication │  │ Skill Matching │  │ Application   │ │
│  │    Service     │  │   Algorithm    │  │  Management   │ │
│  └────────────────┘  └────────────────┘  └───────────────┘ │
│                                                                │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────┐ │
│  │ Email Service  │  │   Validation   │  │   File        │ │
│  │                │  │     Service    │  │   Handler     │ │
│  └────────────────┘  └────────────────┘  └───────────────┘ │
└────────────────────────────────┬─────────────────────────────┘
                                 │
┌────────────────────────────────▼─────────────────────────────┐
│                      Data Access Layer                        │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │   User   │  │ Profile  │  │   Job    │  │Application│   │
│  │  Model   │  │  Model   │  │  Model   │  │  Model    │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│       │             │              │              │           │
└───────┼─────────────┼──────────────┼──────────────┼──────────┘
        │             │              │              │
┌───────▼─────────────▼──────────────▼──────────────▼──────────┐
│                    Database Layer                              │
├──────────────────────────────────────────────────────────────┤
│                  PostgreSQL / SQLite                          │
│                                                                │
│  Tables: auth_user, jobs_profile, jobs_job, jobs_application │
└──────────────────────────────────────────────────────────────┘
```

---

## Data Flow

### 1. User Authentication Flow

```
User → Login Form → POST /accounts/login/
                         ↓
                    Authenticate User
                         ↓
                    Create Session
                         ↓
              ┌──────────┴──────────┐
              │                     │
          Student?              Recruiter?
              │                     │
              ↓                     ↓
       Student Dashboard    Recruiter Dashboard
```

### 2. Job Application Flow

```
Student → Browse Jobs → Select Job → Click Apply
                                         ↓
                              Check if Already Applied
                                         ↓
                                    ┌────┴────┐
                                 Yes│         │No
                                    │         │
                              Show Error  Create Application
                                              ↓
                                     Update Job Stats
                                              ↓
                                      Notify Recruiter
                                              ↓
                                      Show Success
```

### 3. Recruiter Application Review Flow

```
Recruiter → View Applications → Select Applicant
                                      ↓
                             View Resume Format
                                      ↓
                    ┌─────────────────┴─────────────────┐
                    │                                    │
              Print Resume                      Update Status
                    │                                    │
                    ↓                                    ↓
              Save as PDF                    Send to Database
                                                         ↓
                                                 Notify Student
```

### 4. Skill Matching Algorithm Flow

```
Job Posted with Required Skills
         ↓
Student Applies
         ↓
Extract Student Skills from Profile
         ↓
Compare with Job Required Skills
         ↓
Calculate Match Percentage:
  (Matching Skills / Required Skills) × 100
         ↓
Display to Recruiter
```

---

## Security Architecture

### 1. Authentication & Authorization

```
┌─────────────────────────────────────────────┐
│         Django Authentication               │
├─────────────────────────────────────────────┤
│                                             │
│  • Password Hashing (PBKDF2)              │
│  • Session Management                      │
│  • CSRF Protection                         │
│  • XSS Prevention                          │
│  • SQL Injection Protection (ORM)         │
└─────────────────────────────────────────────┘
```

### 2. Authorization Layers

```
Request → Middleware → Authentication Check
                            ↓
                     Is Authenticated?
                            ↓
                    ┌───────┴────────┐
                 Yes│                │No
                    │                │
              Check Role      Redirect to Login
                    ↓
        ┌───────────┼───────────┐
        │           │           │
    Student?   Recruiter?   Admin?
        │           │           │
        ↓           ↓           ↓
   Allow      Check Approval  Allow All
   Student    Status
   Features       ↓
              Approved?
                  ↓
            ┌─────┴─────┐
         Yes│           │No
            │           │
         Allow      Deny Access
      Recruiter
      Features
```

### 3. Data Protection

| Layer | Protection Mechanism |
|-------|---------------------|
| **Transport** | HTTPS (Production) |
| **Session** | Encrypted session cookies |
| **Password** | PBKDF2 with SHA256 |
| **Input** | Django form validation |
| **Output** | Template auto-escaping |
| **Database** | ORM parameterized queries |

---

## Scalability Considerations

### Horizontal Scaling

```
                    Load Balancer
                         │
        ┌────────────────┼────────────────┐
        │                │                │
    Server 1         Server 2         Server 3
        │                │                │
        └────────────────┼────────────────┘
                         │
                  Database Cluster
              (Master-Slave Replication)
```

### Caching Strategy

```
Request → Check Cache
              ↓
         ┌────┴────┐
      Hit│         │Miss
         │         │
    Return     Query DB
    Cached        ↓
    Data      Store in Cache
                  ↓
              Return Data
```

### Database Optimization

1. **Indexing**
   - Index on foreign keys
   - Index on frequently queried fields
   - Composite indexes for multi-column queries

2. **Query Optimization**
   - Use `select_related()` for foreign keys
   - Use `prefetch_related()` for many-to-many
   - Implement pagination

3. **Connection Pooling**
   - Use database connection pooling
   - Implement read replicas

### File Storage

```
Development:
    Media Files → Local File System

Production:
    Media Files → CDN (AWS S3, Cloudinary)
                    ↓
              Edge Locations
              (Faster delivery)
```

---

## Performance Optimization

### 1. Database Level
- Use database indexes
- Optimize queries with `select_related()` and `prefetch_related()`
- Implement database query caching

### 2. Application Level
- Use Django's cache framework
- Implement view-level caching
- Use template fragment caching

### 3. Frontend Level
- Minify CSS and JavaScript
- Use CDN for static files
- Implement lazy loading
- Optimize images

### 4. Server Level
- Use Gunicorn/uWSGI for production
- Configure Nginx as reverse proxy
- Enable gzip compression

---

## Monitoring & Logging

```
┌─────────────────────────────────────────┐
│         Application Monitoring          │
├─────────────────────────────────────────┤
│                                         │
│  • Django Debug Toolbar (Development)  │
│  • Error Tracking (Sentry)            │
│  • Performance Monitoring              │
│  • User Activity Logs                  │
│  • Security Audit Logs                 │
└─────────────────────────────────────────┘
```

---

## Deployment Architecture

### Production Setup

```
Internet
    ↓
[Cloudflare / CDN]
    ↓
[Load Balancer]
    ↓
┌──────────────────┐
│   Nginx          │ (Reverse Proxy)
└──────────────────┘
    ↓
┌──────────────────┐
│  Gunicorn        │ (WSGI Server)
└──────────────────┘
    ↓
┌──────────────────┐
│  Django App      │
└──────────────────┘
    ↓
┌──────────────────┐
│  PostgreSQL      │
└──────────────────┘
```

### Container Architecture (Docker)

```
┌─────────────────────────────────────────┐
│           Docker Compose                │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────┐  ┌──────────┐           │
│  │   Web    │  │   DB     │           │
│  │Container │  │Container │           │
│  └──────────┘  └──────────┘           │
│       │              │                  │
│       └──────┬───────┘                  │
│              │                           │
│        [Shared Volume]                  │
└─────────────────────────────────────────┘
```

---

This architecture documentation provides a comprehensive overview of how HireHub is structured and how its components interact. It serves as a reference for developers working on the system and helps understand the design decisions made during development.
