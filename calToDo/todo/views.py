from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from todo.models import Thing
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib import messages
	
# Create your views here.
def home_view(request):
    post_list = Thing.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

def new_view(request):
    if request.method == "GET":
        return render(request,'add_thing.html')
    if request.method == "POST":
        title = request.POST['title']
        name = request.POST['name']
        status = request.POST['status']
        if title != None:
        	new_thing = Thing.objects.create(title=title,name=name,status=status)
        	new_thing.save()
        return redirect('../home')

def del_view(request, id):
    if request.method == "GET":	
        try:
            post = Thing.objects.get(id=str(id))
        except Thing.DoesNotExist:
            raise Http404
        return render(request,'del.html', {'post' : post})

    if request.method == "POST":
        a_id = request.POST["id"]
        Thing.objects.filter(id=a_id).delete()
        print('render')
        return redirect('../../home')

def edit_view(request,id):
    if request.method == 'GET':
        try:
            post = Thing.objects.get(id=str(id))
        except Thing.DoesNotExist:
            raise Http404
        return render(request,'edit.html',{'post':post})
        



'''
def detail_view(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def hugo_view(request):
 	post_list = Article.objects.all()  #获取全部的Article对象
 	return render(request,'hugo.html',{'post_list' : post_list})
'''