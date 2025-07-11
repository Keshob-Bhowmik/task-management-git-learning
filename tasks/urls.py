from django.urls import path
from .views import Show_Tasks
urlpatterns=[
    path('show-tasks/', Show_Tasks)
]