from django.contrib import admin
from .models import Profile, Education, Experience, Project, Certification

# Register your models here.
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Certification)