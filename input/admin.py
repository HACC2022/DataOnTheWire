from django.contrib import admin
from input.models import ProjectFactSheet


# Register your models here.
class ProjectFactSheetAdmin(admin.ModelAdmin):
    model = ProjectFactSheet

    readonly_fields = (
        'project_ID',
        'project_Phase',
        'source_of_Funding',
        'funding_Received',
        'year_Funding_Received',
        'project_Status_Update',
        'links_Report_Studies',
        'links_Images',
        'input_POC_Last_Name',
        'input_POC_First_Name',
        'input_POC_Email',
        'input_Date',
        'approved_by_staff',
    )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if not obj.approved_by_staff:
            return []
        return self.readonly_fields


admin.site.register(ProjectFactSheet, ProjectFactSheetAdmin)
