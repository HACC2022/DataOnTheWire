from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from input.models import ProjectFactSheet
from django.http import HttpResponse
from input.forms import ProjectFactSheetForm
import csv


# Create your views here.
@permission_required('users.is_admin')
def export_to_csv(request):
    sheets = ProjectFactSheet.objects.filter(approved_by_staff=True)
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=sheets_export.csv'
    writer = csv.writer(response)
    writer.writerow([
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
    ])
    sheet_fields = sheets.values_list(
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
    )
    for sheet in sheet_fields:
        writer.writerow(sheet)
    return response


@login_required
def project_fact_sheet_view(request):
    context = {}
    if request.method == 'POST':
        # create object of form
        form = ProjectFactSheetForm(request.POST)

        # check if form data is valid
        if form.is_valid():
            # save the form data to model
            project_fact_sheet = form.save()
            project_fact_sheet.save()
            # context['form'] = form
            return redirect('login')
    else:
        form = ProjectFactSheetForm()
    return render(request, 'input/project_fact_sheet.html', {'form': form})


def show_project_fact_sheets(request):
    project_fact_sheets = ProjectFactSheet.objects.all()
    return render(request, 'input/show_project_fact_sheets.html', {'project_fact_sheets': project_fact_sheets})


def show_project_fact_sheet(request, project_id):
    project_fact_sheet = ProjectFactSheet.objects.get(pk=project_id)
    return render(request, 'input/show_project_fact_sheet.html', {'project_fact_sheet': project_fact_sheet})


def update_project_fact_sheet(request, project_id):
    project_fact_sheet = ProjectFactSheet.objects.get(pk=project_id)
    form = ProjectFactSheetForm(request.POST or None, instance=project_fact_sheet)
    if form.is_valid():
        # save the form data to model
        project_fact_sheet = form.save()
        project_fact_sheet.save()
        # context['form'] = form
        return redirect('show-project-fact-sheets')
    return render(request, 'input/update_project_fact_sheet.html', {'project_fact_sheet': project_fact_sheet, 'form':form})


