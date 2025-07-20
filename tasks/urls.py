from django.urls import path
from .views import user_dashboard, manager_dashboard, test, create_task
urlpatterns=[
    path("user-dashboard/", manager_dashboard ),
    path("manager-dashboard/", user_dashboard),
    path("test/", test),
    path("create-task/", create_task)
]