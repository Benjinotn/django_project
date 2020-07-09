from django.contrib import admin
from .models import Post
from todo.models import PostIt, Task, PostItList, TaskList

admin.site.register(Post)
admin.site.register(PostIt)
admin.site.register(Task)
admin.site.register(PostItList)
admin.site.register(TaskList)

# Register your models here.
