from django.shortcuts import render
from django.http import HttpResponse
from input.forms import ProjectFactSheetForm

# Create your views here.


def project_fact_sheet_view(request):
    context = {}
    # create object of form
    form = ProjectFactSheetForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form'] = form
    return render(request, "input/project_fact_sheet.html", {'form': form})