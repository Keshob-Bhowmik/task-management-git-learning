from django.urls import path
from .views import Show_Tasks, show_specific_task
urlpatterns=[
    path('show-tasks/', Show_Tasks)
    path('show-tasks/<int:id>', show_specific_task)
]