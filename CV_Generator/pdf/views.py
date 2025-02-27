from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io



# Create your views here.

from django.shortcuts import render, redirect
from .models import Profile, Education, Experience, Project, Certification

def accept(request):
    if request.method == 'POST':
        # Retrieve basic profile information
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        skills = request.POST.get("skills", "")
        github = request.POST.get("github", "")
        linkedin = request.POST.get("linkedin", "")

        # Create a new Profile instance
        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            skills=skills,
            github=github,
            linkedin=linkedin
        )
        profile.save()  # Save the profile to the database

        # Handle multiple education entries
        degrees = request.POST.getlist("degree[]")
        institutions = request.POST.getlist("institution[]")
        durations = request.POST.getlist("duration[]")
        boards = request.POST.getlist("board[]")

        for i in range(len(degrees)):
            education = Education(
                degree=degrees[i],
                institution=institutions[i],
                duration=durations[i],
                board=boards[i] if i < len(boards) else None
            )
            education.save()  # Save each education entry
            profile.education.add(education)  # Associate with the profile

        # Handle multiple experience entries
        job_titles = request.POST.getlist("job_title[]")
        companies = request.POST.getlist("company[]")
        experience_durations = request.POST.getlist("experience_duration[]")
        responsibilities = request.POST.getlist("responsibilities[]")

        for i in range(len(job_titles)):
            experience = Experience(
                job_title=job_titles[i],
                company=companies[i],
                duration=experience_durations[i],
                responsibilities=responsibilities[i]
            )
            experience.save()  # Save each experience entry
            profile.experience.add(experience)  # Associate with the profile

        # Handle multiple project entries
        project_titles = request.POST.getlist("project_title[]")
        technologies = request.POST.getlist("technologies[]")
        project_descriptions = request.POST.getlist("project_description[]")

        for i in range(len(project_titles)):
            project = Project(
                title=project_titles[i],
                technologies=technologies[i],
                description=project_descriptions[i]
            )
            project.save()  # Save each project entry
            profile.projects.add(project)  # Associate with the profile

        # Handle multiple certification entries
        certification_titles = request.POST.getlist("certification_title[]")
        issuing_organizations = request.POST.getlist("issuing_organization[]")
        date_issued = request.POST.getlist("date_issued[]")

        for i in range(len(certification_titles)):
            certification = Certification(
                title=certification_titles[i],
                issuing_organization=issuing_organizations[i],
                date_issued=date_issued[i]
            )
            certification.save()  # Save each certification entry
            profile.certifications.add(certification)  # Associate with the profile

        return redirect('/list')  # Redirect to a list of resumes or another page

    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    skills_list = user_profile.skills.split(",")
    template = loader.get_template("pdf/resume.html")
    html = template.render({'user_profile': user_profile, "skills_list":skills_list}, )

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }

    # Specify the correct path to wkhtmltopdf
    path_wkhtmltopdf = r"F:\Python\Django\wkhtmltox-0.12.6-1.mxe-cross-win64\wkhtmltox\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # Generate PDF
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    return response

# list of resume
def list(request):
    profiles = Profile.objects.all()
    return render(request, "pdf/list.html", {'profiles':profiles})


def see(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, 'pdf/resume.html', {'user_profile':user_profile})

