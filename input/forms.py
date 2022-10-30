from input.models import ProjectFactSheet
from django.forms import ModelForm


class ProjectFactSheetForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ProjectFactSheetForm, self).__init__(*args, **kwargs)
    #     if self.instance:
    #         if self.instance.project == '':

    class Meta:
        model = ProjectFactSheet
        fields = ['project_ID', 'project_Phase', 'source_of_Funding', 'funding_Received', 'year_Funding_Received', 'project_Status_Update', 'links_Report_Studies', 'links_Images', 'input_POC_Last_Name', 'input_POC_First_Name', 'input_POC_Email']


# Creating a form to add a ProjectFactSheet
form = ProjectFactSheetForm()


