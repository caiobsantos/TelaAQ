from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('configuracao/', views.ConfiguracaoList.as_view()),
    path('configuracao/<int:pk>/', views.ConfiguracaoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)