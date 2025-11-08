# Contributing to HireHub

First off, thank you for considering contributing to HireHub! 🎉

It's people like you that make HireHub such a great platform for campus recruitment.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Our Standards

**Examples of behavior that contributes to a positive environment:**

- ✅ Using welcoming and inclusive language
- ✅ Being respectful of differing viewpoints and experiences
- ✅ Gracefully accepting constructive criticism
- ✅ Focusing on what is best for the community
- ✅ Showing empathy towards other community members

**Examples of unacceptable behavior:**

- ❌ The use of sexualized language or imagery
- ❌ Trolling, insulting/derogatory comments, and personal or political attacks
- ❌ Public or private harassment
- ❌ Publishing others' private information without explicit permission
- ❌ Other conduct which could reasonably be considered inappropriate

---

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher installed
- Git for version control
- A code editor (VS Code, PyCharm, etc.)
- Basic understanding of Django framework
- Familiarity with HTML/CSS/JavaScript

### Setting Up Development Environment

1. **Fork the Repository**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/hirehub.git
   cd hirehub
   ```

3. **Set Up Upstream Remote**
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/hirehub.git
   ```

4. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set Up Database**
   ```bash
   cd hirehub
   python manage.py migrate
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

---

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates.

**When you create a bug report, include:**

- **Clear Title**: Use a descriptive title
- **Description**: Detailed description of the issue
- **Steps to Reproduce**:
  1. Go to '...'
  2. Click on '...'
  3. Scroll down to '...'
  4. See error
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Screenshots**: If applicable
- **Environment**:
  - OS: [e.g., Ubuntu 20.04]
  - Python Version: [e.g., 3.9.5]
  - Django Version: [e.g., 4.2.1]
  - Browser: [e.g., Chrome 96]

**Template:**
```markdown
## Bug Description
A clear and concise description of what the bug is.

## Steps to Reproduce
1. 
2. 
3. 

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Screenshots
If applicable, add screenshots.

## Environment
- OS: 
- Python Version: 
- Django Version: 
- Browser: 
```

### 💡 Suggesting Features

Feature suggestions are welcome! Before submitting:

- Check if the feature already exists
- Search existing feature requests
- Consider if it aligns with project goals

**When suggesting features, include:**

- **Feature Description**: Clear description of the feature
- **Use Case**: Why is this feature needed?
- **Proposed Solution**: How would you implement it?
- **Alternatives**: Any alternative solutions considered?
- **Additional Context**: Screenshots, mockups, examples

### 📝 Improving Documentation

Documentation improvements are always appreciated:

- Fix typos or grammatical errors
- Add missing documentation
- Improve existing explanations
- Add code examples
- Create tutorials or guides

### 🎨 Design Contributions

Help improve the UI/UX:

- Suggest design improvements
- Create mockups or wireframes
- Improve accessibility
- Optimize responsive layouts

---

## Development Workflow

### 1. Create a Branch

Always create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
```

**Branch Naming Convention:**
- `feature/feature-name` - New features
- `fix/bug-description` - Bug fixes
- `docs/what-changed` - Documentation
- `refactor/what-refactored` - Code refactoring
- `test/what-tested` - Adding tests

### 2. Make Changes

- Write clean, readable code
- Follow the style guidelines
- Add comments for complex logic
- Update documentation if needed
- Write tests for new features

### 3. Test Your Changes

```bash
# Run tests
python manage.py test

# Check code style
flake8 .

# Run the development server
python manage.py runserver
```

**Manual Testing Checklist:**
- [ ] Feature works as expected
- [ ] No console errors
- [ ] Responsive on mobile devices
- [ ] Works in different browsers
- [ ] Doesn't break existing features

### 4. Commit Your Changes

```bash
git add .
git commit -m "Type: Brief description"
```

See [Commit Guidelines](#commit-guidelines) for details.

### 5. Keep Your Branch Updated

```bash
git fetch upstream
git rebase upstream/main
```

### 6. Push Changes

```bash
git push origin feature/your-feature-name
```

### 7. Create Pull Request

Go to GitHub and create a pull request. See [Pull Request Process](#pull-request-process).

---

## Style Guidelines

### Python Code Style (PEP 8)

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines:

**Good Examples:**

```python
# Good: Clear variable names
def calculate_skill_match_percentage(user_skills, required_skills):
    """Calculate the percentage of matching skills."""
    if not required_skills:
        return 0
    
    matching_skills = set(user_skills) & set(required_skills)
    return (len(matching_skills) / len(required_skills)) * 100


# Good: Proper spacing and formatting
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'job']
```

**Bad Examples:**

```python
# Bad: Unclear variable names
def calc(u, r):
    if not r:
        return 0
    m = set(u) & set(r)
    return (len(m) / len(r)) * 100


# Bad: Poor formatting
class JobApplication(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default='pending')
```

### Django Best Practices

```python
# Use class-based views when appropriate
from django.views.generic import ListView

class JobListView(ListView):
    model = Job
    template_name = 'jobs/jobs_list.html'
    context_object_name = 'jobs'
    paginate_by = 10


# Use get_object_or_404 for safety
from django.shortcuts import get_object_or_404

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


# Use select_related for optimization
def view_applicants(request, job_id):
    applications = Application.objects.filter(
        job_id=job_id
    ).select_related('user__profile')
```

### HTML/Template Style

```html
<!-- Good: Proper indentation and structure -->
<div class="job-card">
    <h3 class="job-title">{{ job.title }}</h3>
    <p class="job-company">{{ job.company }}</p>
    {% if job.location %}
        <span class="job-location">{{ job.location }}</span>
    {% endif %}
</div>

<!-- Bad: Poor formatting -->
<div class="job-card"><h3 class="job-title">{{ job.title }}</h3><p class="job-company">{{ job.company }}</p>{% if job.location %}<span class="job-location">{{ job.location }}</span>{% endif %}</div>
```

### CSS/TailwindCSS Style

```html
<!-- Good: Organized classes -->
<button class="
    px-6 py-3 
    bg-blue-600 hover:bg-blue-700 
    text-white font-bold 
    rounded-lg 
    transition-colors duration-200
">
    Apply Now
</button>

<!-- Good: Custom CSS with proper naming -->
.job-card {
    padding: 1.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.job-card:hover {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
}
```

### JavaScript Style

```javascript
// Good: Clear and documented
/**
 * Toggle application status form visibility
 * @param {number} applicationId - The ID of the application
 */
function toggleStatusForm(applicationId) {
    const form = document.getElementById(`status-form-${applicationId}`);
    if (form) {
        form.classList.toggle('hidden');
    }
}

// Bad: Unclear and undocumented
function tsf(id) {
    const f = document.getElementById(`sf-${id}`);
    if (f) f.classList.toggle('hidden');
}
```

---

## Commit Guidelines

### Commit Message Format

```
Type: Brief description (50 chars or less)

More detailed explanatory text, if necessary. Wrap it to about 72
characters. The blank line separating the summary from the body is
critical.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how.

- Bullet points are okay
- Use a hyphen or asterisk for bullets
```

### Commit Types

| Type | Description | Example |
|------|-------------|---------|
| **Add** | New feature or file | `Add: User profile page` |
| **Update** | Modify existing feature | `Update: Improve dashboard layout` |
| **Fix** | Bug fix | `Fix: Application status not updating` |
| **Remove** | Remove feature or file | `Remove: Deprecated API endpoint` |
| **Refactor** | Code refactoring | `Refactor: Simplify skill matching logic` |
| **Document** | Documentation changes | `Document: Add API usage examples` |
| **Test** | Add or update tests | `Test: Add job application tests` |
| **Style** | Code style changes | `Style: Format Python files with Black` |

### Examples

**Good Commits:**

```bash
Add: Student portfolio section to dashboard

- Added GitHub, LinkedIn, and Portfolio URL fields
- Created portfolio links display component
- Updated profile form to handle new fields

Fixes #123
```

```bash
Fix: Skill matching algorithm returning incorrect percentage

The algorithm was not handling empty skill lists correctly.
Now returns 0% when no required skills are specified.

Before: Division by zero error
After: Returns 0% gracefully
```

**Bad Commits:**

```bash
# Too vague
Update stuff

# Not descriptive
Fix bug

# All lowercase, no type
fixed the thing that was broken
```

---

## Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

### Creating Pull Request

1. **Fill Out Template**
   - Description of changes
   - Related issue numbers
   - Type of change
   - Testing performed
   - Screenshots (if UI change)

2. **PR Title Format**
   ```
   Type: Brief description
   
   Example: Add: Student portfolio links feature
   ```

3. **PR Description Template**
   ```markdown
   ## Description
   Brief description of what this PR does.

   ## Related Issues
   Closes #123
   Related to #456

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   - [ ] Unit tests added/updated
   - [ ] Manual testing performed
   - [ ] All tests pass

   ## Screenshots (if applicable)
   Add screenshots here

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Comments added for complex code
   - [ ] Documentation updated
   - [ ] No new warnings generated
   ```

### Review Process

1. **Automated Checks**: CI/CD will run automated tests
2. **Code Review**: Maintainers will review your code
3. **Feedback**: Address any requested changes
4. **Approval**: Once approved, PR will be merged
5. **Cleanup**: Delete your branch after merge

### After Merge

```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull upstream main

# Delete your feature branch
git branch -d feature/your-feature-name
```

---

## Testing Guidelines

### Writing Tests

```python
# tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Job, Profile

class JobModelTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testrecruiter',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            role='recruiter',
            company_name='Test Company'
        )
    
    def test_job_creation(self):
        """Test that a job can be created"""
        job = Job.objects.create(
            title='Software Developer',
            company='Test Company',
            posted_by=self.user,
            location='Remote',
            job_type='Full-time'
        )
        self.assertEqual(job.title, 'Software Developer')
        self.assertEqual(job.posted_by, self.user)
    
    def test_job_str_method(self):
        """Test the string representation"""
        job = Job.objects.create(
            title='Data Scientist',
            posted_by=self.user
        )
        self.assertEqual(str(job), 'Data Scientist')
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test jobs

# Run specific test class
python manage.py test jobs.tests.JobModelTest

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

---

## Community

### Getting Help

- **Discord**: Join our [Discord server](https://discord.gg/hirehub)
- **GitHub Discussions**: Ask questions in discussions
- **Email**: support@hirehub.com

### Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Given credit in documentation

---

## License

By contributing to HireHub, you agree that your contributions will be licensed under the MIT License.

---

## Questions?

Don't hesitate to ask! We're here to help:

- Open an issue with the `question` label
- Join our Discord community
- Email us at support@hirehub.com

**Thank you for contributing to HireHub! 🎉**
