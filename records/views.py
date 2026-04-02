 
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated

# ==========================================
# 1. HTML WEB VIEWS (For Humans)
# ==========================================
class StudentListView(ListView):
    model = Student
    template_name = 'records/student_list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'records/student_form.html'
    fields = ['first_name', 'last_name', 'email', 'course']
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'records/student_form.html'
    fields = ['first_name', 'last_name', 'email', 'course']
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'records/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')


# ==========================================
# 2. API VIEWS (For Machines/Frontend Devs)
# ==========================================
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated] 

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
# NEW: The Signup View
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny] # This leaves the door open for new users
    serializer_class = RegisterSerializer