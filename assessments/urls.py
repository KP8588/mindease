from django.urls import path
from .views import SubmitAssessmentView, AssessmentHistoryView

urlpatterns = [
    path('submit/', SubmitAssessmentView.as_view(), name='submit-assessment'),
    path('history/', AssessmentHistoryView.as_view(), name='assessment-history'),
]