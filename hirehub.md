# HireHub – Off-Campus Job & Internship Portal  
Modern web platform that helps students find and apply for jobs while enabling companies/admins to post openings.

---

## 1. Overview
HireHub is a responsive job portal designed for college students to discover off-campus jobs and internships. The platform allows students to create profiles, upload resumes, save jobs, apply for positions, and track applications. Recruiters or admins can post, edit, and manage job listings.

---

## 2. Goals & Success Criteria
### **Goals**
- Provide easy access to verified job & internship opportunities.
- Allow students to maintain an updatable profile and resume.
- Provide recruiters/admins a simple workflow to post and manage jobs.
- Offer job search with filters (location, role, type, company).

### **Success Criteria**
| Criteria | Measure |
|--------|---------|
| Students can sign up & create profile | Profile page works with resume upload |
| Jobs list displays clearly with filters | Search + filter returns correct results |
| Job Detail page displays full information | “Apply Now” opens external link / tracks status |
| Admin can post/edit/delete jobs | Admin dashboard functional |
| UI is responsive | Works on mobile, tablet, desktop |

---

## 3. User Stories
**Student**
- I want to register and log in.
- I want to search jobs by role, company, type, and location.
- I want to save jobs for later.
- I want to apply and see my application history.
- I want to update my profile and resume.

**Admin / Recruiter**
- I want to log in as admin.
- I want to post new job openings.
- I want to edit or remove outdated job listings.
- I want to view student profiles and eligibility.

---

## 4. Pages & UI Flow
| Page | Description |
|------|-------------|
| Home | Hero banner, search bar, recent jobs |
| Jobs Listing | Search + filters + job cards grid |
| Job Detail | Full description + Apply + Save Job |
| Login / Register | Authentication |
| User Dashboard | Saved jobs, applications, profile edit |
| Profile Page | Resume upload, skills, details |
| Admin Dashboard | Manage jobs, view students |
| Post Job Page | Admin form to create job listing |

---

## 5. Authentication (Signup/Signin)
- Authentication handled via Django Auth.
- Email + Password login.
- Password hashing enabled.
- Separate roles: **Student** and **Admin**.

---

## 6. User Dashboard (Tabs)
| Tab | Function |
|-----|----------|
| Profile | Name, course, resume, about, skills |
| Saved Jobs | Jobs bookmarked by the user |
| Applied Jobs | Jobs the user actually applied for |
| Settings | Change password, update info |

---

## 7. Admin Dashboard
**Sidebar Sections:**
- Manage Jobs (list + delete + edit)
- Add Job (form)
- View Students (search + sort)
- Profile Settings

Admin can:
✔ Approve / edit / delete jobs  
✔ View applicant profiles  

---

## 8. Job Application Flow (Detailed)
1. User opens Job Detail page.
2. Clicks **Apply Now** → opens external application link.
3. System stores:
   - Job ID
   - User ID
   - Timestamp
4. Appears under **Applied Jobs** tab in Dashboard.
5. If user tries to apply again → system prevents duplicate entry.

---

## 9. Data Models (Schema + Example JSON)

### **User Profile**
```json
{
  "user_id": 12,
  "name": "Varsha",
  "email": "varsha@example.com",
  "skills": ["Python", "Django", "SQL"],
  "resume_url": "uploads/resume.pdf",
  "about": "Computer Science student passionate about backend dev"
}
Job
json
Copy code
{
  "job_id": 101,
  "title": "Software Intern",
  "company": "Google",
  "location": "Remote",
  "job_type": "Full-time Internship",
  "skills_required": ["Python", "API Development"],
  "apply_link": "https://careers.google.com/apply",
  "last_date": "2025-03-15"
}
Saved Job
json
Copy code
{
  "user_id": 12,
  "job_id": 101
}
Application Record
json
Copy code
{
  "user_id": 12,
  "job_id": 101,
  "applied_at": "2025-01-10T10:00:00"
}
10. API Design (Endpoints + Contracts)
Method	Endpoint	Description
GET	/jobs/	Get job list with search filters
GET	/job/<id>/	Get job details
POST	/profile/update/	Update user profile
POST	/job/save/	Save job
POST	/job/apply/	Record job application
POST	/admin/job/add/	Add job (admin only)
POST	/admin/job/edit/<id>/	Edit job
DELETE	/admin/job/delete/<id>/	Delete job

11. Security & Admin Policy
Role-based access control.

Admin pages require staff login.

File uploads sanitized.

Prevent duplicate applications.

12. Resume & Eligibility Check
Resume stored on server.

System compares skill tags with job requirements.

UI display:

✅ Match

⚠️ Partial Match

❌ Not Eligible

13. Receipts & Export
Admin can export:

Job Applicants CSV

Student Profile List CSV

14. Edge Cases & Validations
Case	Handling
Resume not uploaded	Prompt user to upload
Empty job search	Display friendly “No results found”
Invalid apply link	Validate URL format

15. Suggested Tech Stack & Architecture
Layer	Technology
Frontend	HTML + Tailwind CSS + Alpine.js (optional)
Backend	Django / Django ORM
Database	SQLite (development) → PostgreSQL (production)
Deployment	PythonAnywhere / Railway / Vercel Edge (backend)

16. Setup & Development Notes
bash
Copy code
git clone <repo>
cd hirehub
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
17. Tests & QA Suggestions
Test search filters.

Test eligibility suggestion logic.

Test admin role restrictions.

Test resume uploading on mobile and desktop.

18. Next Steps / Optional Features
Email job alerts

AI resume scoring

Company verification badge

Real-time chat between recruiters & students