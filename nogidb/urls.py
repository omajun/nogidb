from django.urls import path
from nogidb import views
from django.contrib import admin

app_name = 'nogidb'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.member_list, name='member_list'),
    path('list/<int:condition>/', views.condition, name='condition'),
    path('detail/<int:member_id>/', views.member_detail, name='detail'),
    path('grade/', views.grade, name='grade'),
    path('grade/<int:status>/', views.grade_condition, name='grade_condition'),
    path('admin/', admin.site.urls, name='admin')

]