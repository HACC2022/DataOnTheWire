from input.models import ProjectFactSheet
from django.forms import ModelForm


class ProjectFactSheetForm(ModelForm):
    class Meta:
        model = ProjectFactSheet
        fields = ['project_ID', 'project_Phase', 'source_of_Funding', 'funding_Received', 'year_Funding_Received', 'project_Status_Update', 'links_report_studies', 'links_images', 'inputPOC_lastname', 'inputPOC_firstname', 'inputPOC_email']


# Creating a form to add a ProjectFactSheet
form = ProjectFactSheetForm()


