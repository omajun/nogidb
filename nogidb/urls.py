from django.urls import path
from nogidb import views

app_name = 'nogidb'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.member_list, name='member_list'),
    path('list/<int:condition>/', views.condition, name='condition'),
]