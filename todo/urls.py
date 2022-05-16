from django.urls import path
from todo.views import TodoDetailView, TodoListView, NotesListView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:task_id>', TodoDetailView.as_view(), name='task'),
    path('notes', NotesListView.as_view(), name='note')
]
