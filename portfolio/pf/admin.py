from django.contrib import admin

from .models import Project, Skill, Technology, ProjectImage, UserProfile

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Technology)
admin.site.register(ProjectImage)
admin.site.register(UserProfile)
