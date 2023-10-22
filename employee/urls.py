from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.EmployeeAddShowView.as_view(), name="addandshow"),
    path('delete/<int:id>/', views.EmployeeDeleteView.as_view(), name="delete_emp"),
    path('update/<int:id>/', views.EmployeeUpdateView.as_view(), name="update_emp"),
]
