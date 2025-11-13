"""
Resume Parser Utility
Extracts text and skills from uploaded resumes
"""
import re
from typing import List, Dict, Set


class ResumeParser:
    """Parse resumes and extract relevant information"""
    
    # Common technical skills to look for
    COMMON_SKILLS = {
        # Programming Languages
        'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin',
        'go', 'rust', 'scala', 'r', 'matlab', 'sql', 'html', 'css', 'sass', 'less',
        
        # Frameworks & Libraries
        'react', 'angular', 'vue', 'django', 'flask', 'spring', 'express', 'nodejs', 'node.js',
        'fastapi', 'tensorflow', 'pytorch', 'keras', 'pandas', 'numpy', 'scikit-learn',
        'bootstrap', 'tailwind', 'jquery', 'nextjs', 'next.js', 'gatsby', 'nuxt',
        
        # Databases
        'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch', 'oracle', 'sqlite',
        'cassandra', 'dynamodb', 'firebase', 'mariadb',
        
        # Cloud & DevOps
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'gitlab', 'github',
        'terraform', 'ansible', 'linux', 'bash', 'shell', 'ci/cd', 'git',
        
        # Data Science & AI
        'machine learning', 'deep learning', 'data analysis', 'data science', 'nlp',
        'computer vision', 'ai', 'artificial intelligence', 'data mining', 'statistics',
        'big data', 'hadoop', 'spark', 'tableau', 'power bi',
        
        # Mobile Development
        'android', 'ios', 'react native', 'flutter', 'xamarin', 'ionic',
        
        # Testing & Tools
        'junit', 'pytest', 'selenium', 'jest', 'mocha', 'postman', 'jira', 'agile',
        'scrum', 'restful', 'rest api', 'graphql', 'microservices', 'api',
        
        # Web Technologies
        'http', 'https', 'websockets', 'ajax', 'json', 'xml', 'oauth', 'jwt',
        
        # Other Skills
        'problem solving', 'communication', 'teamwork', 'leadership', 'project management',
        'data structures', 'algorithms', 'oop', 'functional programming', 'design patterns',
    }
    
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """Extract text from PDF file using PyPDF2"""
        try:
            import PyPDF2
            text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            return text
        except ImportError:
            # Fallback if PyPDF2 is not installed
            return ""
        except Exception as e:
            print(f"Error extracting PDF text: {e}")
            return ""
    
    @staticmethod
    def extract_text_from_docx(file_path: str) -> str:
        """Extract text from DOCX file using python-docx"""
        try:
            import docx
            doc = docx.Document(file_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            return text
        except ImportError:
            # Fallback if python-docx is not installed
            return ""
        except Exception as e:
            print(f"Error extracting DOCX text: {e}")
            return ""
    
    @staticmethod
    def extract_text_from_txt(file_path: str) -> str:
        """Extract text from TXT file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                return file.read()
        except Exception as e:
            print(f"Error extracting TXT text: {e}")
            return ""
    
    @classmethod
    def extract_text_from_resume(cls, file_path: str, file_extension: str) -> str:
        """Extract text from resume based on file type"""
        file_extension = file_extension.lower()
        
        if file_extension == '.pdf':
            return cls.extract_text_from_pdf(file_path)
        elif file_extension in ['.docx', '.doc']:
            return cls.extract_text_from_docx(file_path)
        elif file_extension == '.txt':
            return cls.extract_text_from_txt(file_path)
        else:
            return ""
    
    @classmethod
    def extract_skills(cls, text: str) -> List[str]:
        """Extract skills from resume text"""
        if not text:
            return []
        
        text_lower = text.lower()
        found_skills = set()
        
        # Look for each skill in the text
        for skill in cls.COMMON_SKILLS:
            # Use word boundaries to avoid partial matches
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.add(skill.title())
        
        return sorted(list(found_skills))
    
    @classmethod
    def extract_email(cls, text: str) -> str:
        """Extract email from resume text"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(email_pattern, text)
        return match.group(0) if match else ""
    
    @classmethod
    def extract_phone(cls, text: str) -> str:
        """Extract phone number from resume text"""
        # Common phone patterns
        phone_patterns = [
            r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # International
            r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # US format
            r'\d{10}',  # 10 digits
        ]
        
        for pattern in phone_patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
        return ""
    
    @classmethod
    def extract_education(cls, text: str) -> List[str]:
        """Extract education information from resume"""
        education_keywords = [
            'bachelor', 'master', 'phd', 'doctorate', 'diploma', 'degree',
            'b.tech', 'btech', 'm.tech', 'mtech', 'b.e', 'be', 'm.e', 'me',
            'bca', 'mca', 'b.sc', 'bsc', 'm.sc', 'msc', 'mba', 'bba'
        ]
        
        text_lower = text.lower()
        found_education = []
        
        lines = text.split('\n')
        for line in lines:
            line_lower = line.lower()
            for keyword in education_keywords:
                if keyword in line_lower and line.strip():
                    found_education.append(line.strip())
                    break
        
        return found_education[:5]  # Return top 5 education entries
    
    @classmethod
    def analyze_resume(cls, file_path: str, file_extension: str) -> Dict:
        """
        Complete resume analysis
        Returns dictionary with extracted information
        """
        text = cls.extract_text_from_resume(file_path, file_extension)
        
        return {
            'text': text,
            'skills': cls.extract_skills(text),
            'email': cls.extract_email(text),
            'phone': cls.extract_phone(text),
            'education': cls.extract_education(text),
        }
    
    @classmethod
    def get_job_recommendations(cls, user_skills: List[str], all_jobs, limit=10) -> List:
        """
        Get job recommendations based on skills
        Returns list of jobs sorted by match percentage
        """
        if not user_skills:
            return []
        
        user_skills_set = set(skill.lower() for skill in user_skills)
        job_matches = []
        
        for job in all_jobs:
            if not job.skills_required:
                continue
            
            job_skills_set = set(skill.lower() for skill in job.skills_required)
            
            # Calculate match percentage
            matching_skills = user_skills_set.intersection(job_skills_set)
            if job_skills_set:
                match_percentage = (len(matching_skills) / len(job_skills_set)) * 100
            else:
                match_percentage = 0
            
            if match_percentage > 0:
                job.match_percentage = round(match_percentage, 1)
                job.matching_skills = list(matching_skills)
                job_matches.append(job)
        
        # Sort by match percentage (descending)
        job_matches.sort(key=lambda x: x.match_percentage, reverse=True)
        
        return job_matches[:limit]
