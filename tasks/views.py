from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task
# Create your views here.
def user_dashboard(request):
    return render(request, "dashboard/managerDash.html")
def manager_dashboard(request):
    return render(request, "dashboard/userDash.html")
def test(request):
    context = {
        "name" : ['keshob', 'topa', 'joyonti', 'shopna'],
        "age" : 25
    }
    return render(request, "test.html", context)
def create_task(request):
    employees = Employee.objects.all()
    form = TaskModelForm()
    context = {
        "form" : form
    }
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """ For Django Model Form """
            form.save()
            return render(request, 'create_task.html', {"form": form, "message":"Task Added Successfully"})
            ''' For Django Form '''
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')
            # task = Task.objects.create(tilte = title, description = description, due_date=due_date)
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)
        # return HttpResponse("task added successfully")

    return render(request, "create_task.html", context)