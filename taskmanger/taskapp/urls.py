from django.urls import path 
from taskapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('completed/',views.completed_tasks,name="completed"),
    path('pending/',views.pending_tasks,name="pending"),
    path('edit/<int:pk>/',views.edit_task,name='edit'),
    path('delete/<int:pk>/',views.delete_task,name='delete')  
]
