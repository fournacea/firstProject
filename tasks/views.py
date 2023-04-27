from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


# Initialize task list variable
tasks= []

#Create a base form
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

#View tasks
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

#Add tasks
def add(request):
    #Check if method is POST
    if request.method == "POST":

        #Take in data the user submitted as form
        form = NewTaskForm(request.POST)

        #Check if form is valid (server-side)
        if form.is_valid():

            #Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            #Add the new task to our list of tasks
            tasks.append(task)

            #Redirect the user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))
        
        else:
            #If the form is invalid, re-render the page with the existing information
            return render(request, "tasks/add.html", {
                "form": form
            })
    
    #If method == GET
    return render(request, "tasks/add.html", {
       "form": NewTaskForm() 
    })