from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('historico/decomol', views.DecomolHistoricoList.as_view()),
    path('historico/decomol/<int:pk>/', views.DecomolHistoricoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)