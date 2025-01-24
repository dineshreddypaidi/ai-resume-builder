from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=12,null=True,blank=True,default='')
    
    github = models.URLField()
    linkedin = models.URLField()
    personal_site = models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username

class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    gpa = models.FloatField()
    achievement = models.TextField()
    
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='experiences')
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.role} at {self.company}"

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(max_length=255)

    github = models.URLField()
    deployed_link = models.URLField()
    
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    ])

    def __str__(self):
        return f"{self.name} ({self.proficiency})"

class JobDescription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='job_descriptions')
    description = models.TextField()

    def __str__(self):
        return f"Job Description for {self.user.username}"


class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resumes')
    generated_file = models.FileField(upload_to='resumes/')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resume for {self.user.username}"


class SimilarityScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='similarity_scores')
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE, related_name='similarity_scores')
    field = models.CharField(max_length=50, choices=[
        ('skills', 'Skills'),
        ('education', 'Education'),
        ('experience', 'Experience'),
        ('projects', 'Projects'),
    ])
    score = models.FloatField()

    def __str__(self):
        return f"{self.field} Similarity Score: {self.score}"
