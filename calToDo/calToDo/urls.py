"""calToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from todo.views import home_view,new_view,del_view,edit_view
from login.views import login_view,logout_view
from comment.views import comment_view,add_comment_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home_view),
    path('',home_view),
    path('login/',login_view),
    path('logout/',logout_view),
    path('add/',new_view),
    path('del/<int:id>',del_view, name='thing-id1'),
    path('edit/<int:id>',edit_view, name='thing-id2'),
    path('comments/',comment_view),
    path('add_comment/',add_comment_view)
]