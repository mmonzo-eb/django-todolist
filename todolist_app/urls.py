from django.urls import path
from .views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoReassignView,
    TodoDetailView,
)

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', TodoListView.as_view(
        paginate_by=2,
        allow_empty=True,
    ), name='todo_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('update/<pk>', TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<pk>', TodoDeleteView.as_view(), name='todo_delete'),
    path('reassign/<pk>', TodoReassignView.as_view(), name='todo_reassign'),
    path('todo/<pk>', TodoDetailView.as_view(), name='todo_detail'),
]
