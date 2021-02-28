from django.shortcuts import render
from datetime import datetime

tasks = ["test1", "test2", "test3"]

# Create your views here.

def index(request):
    currentDate = datetime.now().strftime("%A, %d. %b. %Y")
    return render(request, "taskmanager/index.html", {
        "tasks": tasks,
        "currentDate": currentDate
    })