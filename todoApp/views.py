from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return HttpResponse("hello")


# def homepage(request):
#     return HttpResponse("home page")


def homepage(request, name=None):
    if name == None:
        name = "Guest"  # default name if no name provided
    data = {
        "title": "To-Do List",
        "tasks": [
            "Task 1",
            "Task 2",
            "Task 3",
            "Task 4",
            "Task 5",
            "Task 6",
            "Task 7",
            "Task 8",
            "Task 9",
            "Task 10",
        ],
        "footer_text": "Created by John Doe",
        "name": name,
    }
    return render(request, "todoApp/index.html", context=data)


def about(request):
    # ata sudu dictonary read korte pare?
    # data = [
    #     {"name": "John Doe", "email": "john.doe@example.com"},
    #     {"name": "Jane Smith", "email": "jane.smith@example.com"},
    #     {"name": "Alice Johnson", "email": "alice.johnson@example.com"},
    # ]
    return render(request, "todoApp/about.html")


def contact(request):
    return render(request, "todoApp/contact.html")
