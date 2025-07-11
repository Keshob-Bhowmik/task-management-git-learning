from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse("Welcome to the home")
def Contact(Request):
    return HttpResponse("<button style='color: blue'>This is Contact Page</button>")
def Show_Tasks(request):
    return HttpResponse("You Can show all the taksk here")
def show_specific_task(request, id):
    print("id", id)
    print("id type", type(id))
    return HttpResponse(f"This is specific task page {id}")