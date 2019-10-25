from django.urls import path
from nogidb import views

app_name = 'nogidb'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.member_list, name='member_list'),
    path('list/<int:condition>/', views.condition, name='condition'),
    #path('list/age/', views.age, name='age'),
    #path('list/join_class/', views.join_class, name='join_class'),
    #path('list/status/', views.status, name='status'),
    #path('list/name/', views.name, name='name'),

]