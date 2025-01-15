from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('complete/<int:id>', views.complete, name='complete'),
    path('pending/<int:id>', views.pending, name='pending'),


    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_user, name='logout_user'),




    path('category/new', views.new_category, name='new_category'),
    path('category/delete', views.delete_category, name='delete_category'),
    path('category/<slug:slug>/todos', views.todos_category, name='todos_category'),
]