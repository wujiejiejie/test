from django.urls import path,include
from . import views

app_name = 'todolist'

#起一个app的名字，指定前缀
#起一个name,用于访问
#避免网址名，网页名冲突


urlpatterns = [
    path('home/', views.home,name='主页'),
    path('about/', views.about,name='关于'),
    path('edit/<forloop_counter>', views.edit,name='编辑'),
    path('del/<forloop_counter>', views.delete,name='删除'),
    path('cross/<forloop_counter>', views.cross,name='划掉'),
]

#子路由
#传一个变量