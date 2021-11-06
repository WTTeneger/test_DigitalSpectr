from django.urls import path

from . import views

urlpatterns = [
    path('api/filter/', views.GetUsersInfoView.as_view()),
    path('', views.main_page, name='main_page'),
    path('add/', views.add_page, name='add_page'),
]
