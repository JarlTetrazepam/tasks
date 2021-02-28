from django import forms
from django.shortcuts import render
from datetime import datetime

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add a new task")

# Create your views here.

def index(request):
    current_date = datetime.now().strftime("%A, %d. %b. %Y")

    if "tasks" not in request.session:
        request.session["tasks"] = []   

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data["task"]
            request.session["tasks"] += [new_task]
        else:
            return render(request, "taskmanager/index.html", {
                "form": form
            })

    return render(request, "taskmanager/index.html", {
        "tasks": request.session["tasks"],
        "currentDate": current_date,
        "form": NewTaskForm()
    })