from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='api_create'),
    path('get_all', views.get_all, name='api_get_all'),
    path('delete/<int:id>', views.delete, name='api_delete'),
    path('update/<int:id>', views.update, name='api_update'),
    path('complete/<int:id>', views.complete, name='api_complete'),
    path('pending/<int:id>', views.pending, name='api_pending'),
]