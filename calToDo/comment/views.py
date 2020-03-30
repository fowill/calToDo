from django.shortcuts import render,redirect
from comment.models import Comment

# Create your views here.
def comment_view(request):
    post_list = Comment.objects.all()  #获取全部的Comment对象
    return render(request, 'comment.html', {'post_list' : post_list})

def add_comment_view(request):
	if request.method == "GET":	
		return render(request, 'add_comment.html')
	if request.method == "POST":
		name = request.POST["name"]
		text = request.POST["text"]
		if name != None and text != None:
			new_comment = Comment.objects.create(name=name,text=text)
			new_comment.save()
		return redirect('../comments')