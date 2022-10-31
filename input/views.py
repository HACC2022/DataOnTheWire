from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from input.forms import ProjectFactSheetForm


# Create your views here.
@login_required
def project_fact_sheet_view(request):
    context = {}
    if request.method == 'POST':
        # create object of form
        form = ProjectFactSheetForm(request.POST or None, request.FILES or None)

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