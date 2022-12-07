from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("railway ticket")


def ticket(request):
    task = ""
    taskno = ""
    details = ""
    status = ""
    if request.GET:
        task = request.GET["task"]
        taskno = request.GET["taskno"]
        details = request.GET["details"]
        status = request.GET["status"]
        # print(task, taskno, details, status)

    return render(request, "tickets.html")


def ticketUser(request):
    return HttpResponse("Create")
