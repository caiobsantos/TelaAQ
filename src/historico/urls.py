from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('historico/', views.DecomolHistoricoList.as_view()),
    path('historico/<int:pk>/', views.DecomolHistoricoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)