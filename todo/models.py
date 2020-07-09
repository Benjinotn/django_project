from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


# class Checklist(models.Model):
#     point = models.CharField(max_length=100)
#     isDone = models.BooleanField(default=False)
#     noteTitle = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.point


class PostIt(models.Model):
    noteTitle = models.CharField(max_length=30)

    def __str__(self):
        return self.noteTitle

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Task(models.Model):
    TaskTitle = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return self.TaskTitle

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class PostItList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postit_obj = models.OneToOneField(PostIt, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class TaskList(models.Model):
    postit_obj = models.ForeignKey(PostIt, on_delete=models.CASCADE)
    task_obj = models.OneToOneField(Task, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)






# class Task(models.Model):
#
#     TaskTitle = models.CharField(max_length=100)
#     isDone = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.TaskTitle
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#
#
# class PostIt(models.Model):
#     noteTitle = models.CharField(max_length=30)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tasks = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
#
#     def __str__(self):
#         return self.noteTitle
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#









