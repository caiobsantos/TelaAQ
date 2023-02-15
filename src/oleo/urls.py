from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('oleo/', views.OleoList.as_view()),
    path('oleo/<int:pk>/', views.OleoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)