from django.urls import path
from . import views
from .views import expense_list, expense_detail


urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('expenses/', expense_list, name='expense-list'),

    path('expenses/<int:pk>/', expense_detail, name='expense-detail'),

]
