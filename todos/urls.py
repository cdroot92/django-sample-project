from django.urls import path

from . import views

app_name = "todos"
urlpatterns = [path("todo_list", views.AboutTodoList.as_view(), name="about_todo_list")]
