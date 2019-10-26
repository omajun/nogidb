from django.urls import path
from nogidb import views

app_name = 'nogidb'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.member_list, name='member_list'),
    path('list/<int:condition>/', views.condition, name='condition'),
    path('detail/<int:member_id>/', views.member_detail, name='detail'),
    path('grade/', views.grade, name='grade'),
]