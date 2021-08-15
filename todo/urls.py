from django.urls import path
from .views import (
    HomePage,
    LandingPage,
    CrateCategoryView,
    DeleteCategoryView,
    UpdateCategoryView,
    CreateTodoView,
    DeleteTodoView,
    UpdateTodoView,
)

app_name = "todo"

urlpatterns = [
    # Todo
    path('<int:pk>/', HomePage.as_view(), name="todo-home"),
    path('<int:pk1>/<int:pk2>/delete/', DeleteTodoView.as_view(), name="todo-delete"),
    path('<int:pk1>/<int:pk2>/update/', UpdateTodoView.as_view(), name="todo-update"),
    path('<int:pk>/create/', CreateTodoView.as_view(), name="todo-create"),
    # Category
    path('create/',CrateCategoryView.as_view(), name='category-create'),  
    path('<int:pk>/delete/',DeleteCategoryView.as_view(), name='category-delete'), 
    path('<int:pk>/update/',UpdateCategoryView.as_view(), name='category-update'), 
    path('', LandingPage.as_view(), name="landing"),
]