from django.urls import path

from todo.views import (
    index,
    TagListView,
    TagCreateView,
    TaskListView,
    TaskDetailView,
)

urlpatterns = [
    path("", index, name="index"),

    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),

    path(
        "tags/create",
        TagCreateView.as_view(),
        name="tag-create"
    ),

    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),

    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
]

app_name = "todo"
