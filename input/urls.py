from django.urls import path
from . import views

urlpatterns = [
    path('project_fact_sheet/', views.project_fact_sheet_view, name='input-project-fact-sheet')
]