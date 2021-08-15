from typing import Callable
from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic, View

from .forms import CategoryModelForm, TodoModelForm

from .models import (
    Todo,
    Category
)

########################
######## TODO ##########

class HomePage(generic.ListView):
    template_name = 'todo/todo_home.html'
    context_object_name = "todolists"
    # queryset = Todo.objects.all()

    def get_queryset(self):
        # Get the special astribute
        pk = self.kwargs.get('pk')
        category = Category.objects.filter(id=pk)[0]

        queryset = Todo.objects.filter(category__category=category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['pk'] = int(pk)
        return context

# Todo Create
class CreateTodoView(generic.CreateView):
    template_name = 'todo/todo_create.html'
    form_class = TodoModelForm

    def get_initial(self):
        pk = self.request.path.split("/")[1]
        print(pk)
        category = Category.objects.filter(id=pk)[0]
        return {'category':category}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['pk'] = int(pk)
        return context


    def get_success_url(self):
        pk = self.kwargs.get('pk')     
        return reverse('todo:todo-home', kwargs={'pk': pk})

# Todo Update
class UpdateTodoView(generic.UpdateView):
    template_name = 'todo/todo_update.html'
    form_class = TodoModelForm
    context_object_name = "context"
    
    def get_object(self):
        pk = self.kwargs.get('pk2')
        # Get the instance of queryset
        obj = Todo.objects.filter(id=pk).first()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk1 = self.kwargs.get('pk1')
        pk2 = self.kwargs.get('pk2')
        context['pk1'] = int(pk1)
        context['pk2'] = int(pk2)
        return context

    def get_success_url(self):
        pk = self.kwargs.get('pk1') 
        return reverse('todo:todo-home', kwargs={'pk': pk})
# Todo Delete
class DeleteTodoView(generic.DeleteView):
    template_name = 'todo/todo_delete.html'
    model = Todo
    context_object_name = "context"

    def get_object(self):
        pk = self.kwargs.get('pk2')
        queryset = Todo.objects.filter(id=pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk1 = self.kwargs.get('pk1')
        pk2 = self.kwargs.get('pk2')
        context['pk1'] = int(pk1)
        context['pk2'] = int(pk2)
        return context

    def get_success_url(self):
        pk = self.kwargs.get('pk1') 
        return reverse('todo:todo-home', kwargs={'pk': pk})

##########################
####### Category #########
    
class LandingPage(generic.ListView):
    template_name = 'todo/todo_landing.html'
    context_object_name = "categories"

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

# Create A category
class CrateCategoryView(generic.CreateView):
    template_name = 'todo/category_create.html'
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse('todo:landing')

# Update A Category
class UpdateCategoryView(generic.UpdateView):
    template_name = 'todo/category_update.html'
    form_class = CategoryModelForm

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        obj = Category.objects.filter(id=pk)
        return obj

    def get_success_url(self):
        return reverse('todo:landing')

# Delete A Category
class DeleteCategoryView(generic.DeleteView):
    template_name = 'todo/category_delete.html'
    model = Category
    def get_success_url(self):
        return reverse('todo:landing')