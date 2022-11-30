from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('pulmao/', views.PulmaoList.as_view()),
    path('pulmao/<int:pk>/', views.PulmaoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)