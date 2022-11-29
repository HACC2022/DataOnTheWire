from django.urls import path
from . import views

urlpatterns = [
    path('project_fact_sheet/', views.project_fact_sheet_view, name='input-project-fact-sheet'),
    path('show_project_fact_sheets/', views.show_project_fact_sheets, name='show-project-fact-sheets'),
    path('show_project_fact_sheets/<project_id>', views.show_project_fact_sheet, name='show-project-fact-sheet')
]