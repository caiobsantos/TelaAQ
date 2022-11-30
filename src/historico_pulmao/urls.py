from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('historico/pulmao', views.PulmaoHistoricoList.as_view()),
    path('historico/pulmao/<int:pk>/', views.PulmaoHistoricoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)