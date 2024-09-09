from django.shortcuts import render, redirect
from todoApp2.models import Task
from todoApp2.froms import SearchForm, TaskForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    # ata ki url ar completed?
    isCompleted = request.GET.get("completed")
    # isT = request.GET.get('t')
    # print(isCompleted,isT)
    if isCompleted == "1":
        tasks = tasks.filter(completed=True)
    elif isCompleted == "0":
        tasks = tasks.filter(completed=False)

    # import search form
    # search_form = SearchForm()
    search_form = SearchForm(request.GET)
    search_query = ""
    if search_form.is_valid():
        search_query = search_form.cleaned_data["query"]
        # tasks = tasks.filter(title__icontains=search_query)  # for case-insensitive search

    # i want to search by title
    # search_query = request.GET.get("query", "")
    task_arr = []

    for task in tasks:
        if search_query and search_query.lower() in task.title.lower():
            task_arr.append(task)
            tasks = task_arr

    # if search_query:
    #     # tasks = tasks.filter(title=search_query)
    #     tasks = tasks.filter(title__icontains=search_query) # for case-insensitive search

    # search form

    context = {
        "tasks": tasks,
        "search_form": search_form,
    }
    return render(request, "todoApp2/task_list.html", context=context)


def task_details(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        return render(request, "todoApp2/task_details.html", {"task": task})
    except Task.DoesNotExist:
        return HttpResponse("id is not abailable" + str(pk))


def add_task(request):
    title = "Dinner"
    description = "Are you complete Dinner"
    completed = False

    tasks = Task(
        title=title,
        description=description,
        completed=completed,
    )
    tasks.save()

    # return HttpResponse("hello add ")
    return redirect("task_list")


#  delete task
def delete_task(request, pk):

    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect("task_list")
    except Task.DoesNotExist:
        return HttpResponse("id is not abailable" + str(pk))

    # return HttpResponse("delete id is" + str(pk))


# update task
def update_task(reruest, pk):
    task = Task.objects.get(pk=pk)
    task.title = "update task"
    task.save()
    return redirect("task_list")


def add_task_form(request):
    if request.method == "POST":
        addForm = TaskForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            return redirect("task_list")
        else:
            constext = {"taskform": addForm}
            return render(request, "todoApp2/addTask.html", context=constext)
    else:
        addForm = TaskForm()
        context = {"taskform": addForm}
        return render(request, "todoApp2/addTask.html", context=context)


# update task form
def update_task_form(request, pk):

    try:
        task = Task.objects.get(pk=pk)

        if request.method == "POST":
            update_form = TaskForm(request.POST, instance=task)

            if update_form.is_valid():
                update_form.save()
                return redirect("task_list")
            else:
                constext = {"update_form": update_form}
                return render(request, "todoApp2/updateTask.html", context=constext)

        update_form = TaskForm(instance=task)

        context = {
            "update_form": update_form,
        }
        # if request.method == "POST":
        # return HttpResponse("hi update "+ str(pk))
        return render(request, "todoApp2/updateTask.html", context=context)
    except Task.DoesNotExist:
        return HttpResponse("id is not abailable" + str(pk))



# task by user id 
def taskByUserId(request, pk):
#  -------------------------------------------1------------------------------------
    # tasks = Task.objects.filter(user_id= user_id).values()
    # return JsonResponse({"tasks": list(tasks)})
#  -------------------------------------------2------------------------------------
    # tasks = Task.objects.filter(user_id=user_id)
    # task_arr = []
    # for task in tasks:
    #     task_arr.append({
    #         "id": task.id,
    #         "title": task.title,
    #         "description": task.description,
    #         "completed": task.completed,
    #         "user": task.user.email
    #     })

    # return JsonResponse({"tasks": task_arr})
#  -------------------------------------------3------------------------------------
    user = User.objects.get(pk = pk)
    # if i don't use related_name in models i have to access task by task_set in user.tasks
    tasks = user.tasks.all().values()
    return JsonResponse({"tasks": list(tasks)}) 


