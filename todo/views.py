from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import PostIt, Task, PostItList, TaskList
from users.models import Profile

# Create your views here.


@login_required()
def todo(request):
    post_it_list = []
    task_list = []
    # current_profile = Profile.objects.all().filter(user=request.user).first()
    current_user = request.user
    postit_query = PostItList.objects.all().filter(user=current_user)
    for _postit in postit_query:

        task_query = TaskList.objects.all().filter(postit_obj=_postit.postit_obj)

        if task_query.exists():
            task_list.append(task_query)
        else:
            task_list.append([])
        post_it_list.append(_postit.postit_obj)

    if post_it_list:
        occupied = True
    else:
        occupied = False

    context = {"post_it_list": post_it_list,
               "task_list": task_list,
               "occupied": occupied}

    return render(request, 'todo/todo.html', context)


def contains(num, List):
    for element in List:
        if num == element:
            return True
    return False


def addTodoNote(request):
    if request.method == 'POST':
        postItTitle = request.POST.get('PostItTitle', None)
        if postItTitle:
            _user = request.user
            tempNote = PostIt(noteTitle=postItTitle)
            tempNote.save()
            tempRelation = PostItList(user=_user, postit_obj=tempNote)
            tempRelation.save()

    return HttpResponseRedirect('/todo/')


def deleteTodoTask(request):
    if request.method == 'POST':
        taskID = request.POST.get("task-id-to-delete", None)
        Task.objects.filter(id=taskID).delete()
    return HttpResponseRedirect('/todo/')


def deleteTodoNote(request):
    if request.method == 'POST':

        postID = request.POST.get("PostItID", None)
        PostIt.objects.filter(id=postID).delete()

    return HttpResponseRedirect('/todo/')


def addTodoTask(request):
    if request.method == 'POST':
        _taskTitle = request.POST.get('added-point')
        _postit_obj = PostIt.objects.all().filter(id=request.POST.get('post-id')).first()

        if _taskTitle:
            _user = request.user
            tempTask = Task(TaskTitle=_taskTitle, isDone=False)
            tempTask.save()
            tempRelation = TaskList(postit_obj=_postit_obj, task_obj=tempTask)
            tempRelation.save()

    return HttpResponseRedirect('/todo/')


def finishTodo(request):
    if request.method == 'POST':

        _postit_obj = PostIt.objects.all().filter(id=request.POST.get('post-id')).first()

        finishDict = request.POST.getlist("popup-box")
        unchangedBoxList = request.POST.getlist("popup-checked-box")

        finishedTasks = []
        for task in Task.objects.all().filter(isDone=True):
            currentTaskList = TaskList.objects.all().filter(postit_obj=_postit_obj)
            for sharedTask in currentTaskList:
                if task == sharedTask:
                    finishedTasks.append(str(task.pk))

        # for pk in finishedTasks:
        #     if contains(pk, unchangedBoxList):
        #         pass
        #     else:
        #         checkbox = Task.objects.all().filter(id=pk).first()
        #         checkbox.isDone = False
        #         checkbox.save()

        if finishDict is not None:
            for _id in finishDict:
                checkbox = Task.objects.all().filter(id=_id).first()
                if checkbox:
                    checkbox.isDone = True
                    checkbox.save()

    return HttpResponseRedirect('/todo/')



    # print(current_profile.postits.all())
    # for post in current_profile.postits.all():
    #     print("x")
    #     print(post)
    #user_post_its = .objects.all().filter(author=request.user, isDone=False)
    # return_user_finished_points = Checklist.objects.all().filter(author=request.user, isDone=True)

    # if return_user_points.exists():
    #     empty = False
    # else:
    #     empty = True
    #
    # if return_user_finished_points.exists():
    #     finished_empty = False
    # else:
    #     finished_empty = True
    # {'all_points': return_user_points,
    #  'all_finished_points': return_user_finished_points,
    #  'empty': empty,
    #  'finished_empty': finished_empty}



#
# def addTodo(request):
#     if request.POST.get('added-point') is not None and request.POST.get('added-point') != '':
#         new_item = Checklist(point=request.POST.get('added-point'), author=request.user, isDone=False)
#         new_item.save()
#
#     return HttpResponseRedirect('/todo/')
#
#
# def finishTodo(request):
#     if request.method == 'POST':
#         finishDict = request.POST.getlist("box")
#         if finishDict is not None:
#             for _id in finishDict:
#                 checkbox = Checklist.objects.all().filter(id=_id).first()
#                 if checkbox:
#                     checkbox.isDone = True
#                     checkbox.save()
#
#     return HttpResponseRedirect('/todo/')
#
#
# def deleteTodo(request, point_id):
#
#     checkToDelete = get_object_or_404(Checklist, id=point_id)
#     if request.method == 'POST':
#         checkToDelete.delete()
#
#     return HttpResponseRedirect('/todo/')
