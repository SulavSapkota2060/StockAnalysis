from django.urls import path
from . import views


urlpatterns = [
    path('',views.allTodos, name= 'All Todos'),
    path('create/',views.createTodo, name= 'Create'),
    path('update/<str:pk>/',views.updateTodo, name= 'Update'),
    path('updateStatus/',views.updateStatus, name= 'UpdateStat'),
    path('delete/<str:pk>',views.deleteTodo, name= 'Delete'),
    path('stock_list', views.stock_list,name='stocks'),
    path('status/',views.upStatus, name = 'Status')
]