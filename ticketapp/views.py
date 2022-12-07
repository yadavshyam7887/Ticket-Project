from django.shortcuts import render
from django.http import HttpResponse
from .models import TicketsModels


# Create your views here.


def index(request):
    return HttpResponse("railway ticket")


def ticket(request):
    if request.GET:
        taskno= request.GET["task"]
        taskname = request.GET["task_name"]
        details = request.GET["details"]
        status = request.GET["status"]
        task = TicketsModels(task=taskname, taskno=taskno, details=details, status=status)
        task.save()
    return render(request, "tickets.html",{"taskno":taskno,"taskname":taskname,"details":details,"status":status})


def edit(request):
    return render(request,"edit.html")
