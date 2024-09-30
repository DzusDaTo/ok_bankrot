from rest_framework import generics, permissions
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework.pagination import PageNumberPagination


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]  # Доступно всем
    pagination_class = None


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только для авторизованных
    pagination_class = PageNumberPagination  # Пагинация по умолчанию

    def get_queryset(self):
        queryset = super().get_queryset().select_related('department')
        last_name = self.request.query_params.get('last_name')
        department_id = self.request.query_params.get('department_id')
        if last_name:
            queryset = queryset.filter(full_name__icontains=last_name)
        if department_id:
            queryset = queryset.filter(department__id=department_id)
        return queryset


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только для авторизованных

