from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TodoListForm
from .models import TodoList 



def ListTodo(request):
	todo_list = TodoList.objects.all().order_by('-created')
	context = {
		'todo_list': todo_list,
	}
	return render(request, 'list/index.html', context)


def CreateTodo(request):
	form = TodoListForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			title = form.cleaned_data.get('title')
			complete = form.cleaned_data.get('complete' or None)
			todo_list = TodoList.objects.create(title=title, complete=complete)
			print(todo_list)
		return redirect('/')
	context = {
		'form': form,
	}
	return render (request, 'list/create.html', context)


def UpdateTodo(request, id):
	obj = get_object_or_404(TodoList, id=id)
	form = TodoListForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('/')
	context = {
		'form': form,
	}
	return render (request, 'list/update.html', context)

def DeleteTodo(request, id):
	obj = get_object_or_404(TodoList, id=id)
	if request.POST:
		obj.delete()
		return redirect('/')
	context = {
		'obj': obj
	}
	return render (request, 'list/delete.html', context)
