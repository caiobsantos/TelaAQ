from django.urls import path
from . import views

urlpatterns =[
    path('troca/', views.DecomolTrocaList.as_view()),
    path('troca/<int:pk>/', views.DecomolTrocaDetail.as_view()),
]
