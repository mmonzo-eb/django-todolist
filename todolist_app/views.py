from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
# from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied


from .models import Todo


class TodoMixin():

    # def get_object(self):
    #     todo = super().get_object()
    #     if todo.assigned_user != self.request.user:
    #         raise PermissionDenied
    #     return todo
    def get_queryset(self):
        return Todo.objects.filter(assigned_user=self.request.user)


# Create your views here.
class TodoListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Todo.objects.filter(assigned_user=self.request.user)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'done', 'priority']

    def get_success_url(self):
        return reverse('todo_detail', args=(self.object.id,))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.assigned_user = self.request.user
        self.object.created_by = self.request.user
        self.object.updated_by = self.request.user
        return super().form_valid(form)


class TodoUpdateView(TodoMixin, LoginRequiredMixin, UpdateView):
    model = Todo
    fields = [
        'title',
        'description',
        'done',
        'priority',
    ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('todo_detail', args=(self.object.id,))

    def get_object(self):
        todo = super().get_object()
        if todo.assigned_user != self.request.user:
            raise PermissionDenied
        return todo


class TodoDeleteView(TodoMixin, LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')


class TodoReassignView(TodoMixin, LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['assigned_user']
    success_url = reverse_lazy('todo_list')
    template_name_suffix = '_reassign_form'


class TodoDetailView(TodoMixin, LoginRequiredMixin, DetailView):
    model = Todo
