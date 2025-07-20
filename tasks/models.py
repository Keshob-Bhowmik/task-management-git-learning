from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1)
    assigned_to = models.ManyToManyField(Employee, related_name='tasks')
    tilte = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task_details(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium',),
        (LOW, 'Low')
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='details')
    assigned_to = models.CharField(max_length=200)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)


class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()