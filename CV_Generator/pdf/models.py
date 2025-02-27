from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    board = models.CharField(max_length=100, blank=True, null=True)  # Optional field for board/university

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    technologies = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    date_issued = models.DateField()

    def __str__(self):
        return f"{self.title} from {self.issuing_organization}"

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    summary = models.TextField(max_length=2200)
    skills = models.TextField(max_length=1000)

    # Links to online profiles
    github = models.URLField(max_length=200, blank=True)  # Optional GitHub profile link
    linkedin = models.URLField(max_length=200, blank=True)  # Optional LinkedIn profile link

    # Relationships
    education = models.ManyToManyField(Education, blank=True)
    experience = models.ManyToManyField(Experience, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    certifications = models.ManyToManyField(Certification, blank=True)

    def __str__(self):
        return self.name