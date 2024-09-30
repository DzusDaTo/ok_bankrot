from django.urls import path
from .views import DepartmentListView, EmployeeListView, EmployeeDetailView


urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]
