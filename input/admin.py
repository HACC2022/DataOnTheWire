from django.contrib import admin
from input.models import ProjectFactSheet


# Register your models here.
class ProjectFactSheetAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectFactSheet, ProjectFactSheetAdmin)
