from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import serializers

User = get_user_model()


class TodoList(models.Model):
    user = models.ForeignKey(User, related_name="todo_list", on_delete=models.CASCADE)

    class Meta:
        db_table = "todos"


class Todo(models.Model):
    todo_list = models.ForeignKey(TodoList, related_name="todo", on_delete=models.CASCADE)
    body = models.TextField(blank=True)

    class Meta:
        db_table = "todo"


class Tag(models.Model):
    todo_list = models.ManyToManyField(TodoList, related_name="tags")

    class Meta:
        db_table = "tags"


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "body"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        modes = Tag
        fields = ["id"]


class TodoListSerializer(serializers.ModelSerializer):
    items = TodoSerializer(many=True, source="todo")
    tags = TagSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ["id", "items", "tags"]

    def create(self, validated_data):
        todo_data = validated_data.pop("todo")
        tags = validated_data.pop("tags")
        todo_list = TodoList.objects.create(**validated_data)
        for todo in todo_data:
            Todo.objects.create(todo_list=todo_list, **todo)
        for tag in tags:
            Tag.objects.create(todo_list=todo_list, **tag)
        return todo_list
