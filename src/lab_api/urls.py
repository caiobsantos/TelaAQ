from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('decomol/', views.DecomolList.as_view()),
    path('decomol/<int:pk>/', views.DecomolDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)