from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task


@login_required
def index(request):
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
    }

    return render(request, "todo/index.html", context=context)


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task

