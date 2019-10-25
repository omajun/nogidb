from django.urls import path
from . import views

app_name = 'album'
urlpatterns = [
    path('<int:member_id>', views.member_detail, name='detail'),
]