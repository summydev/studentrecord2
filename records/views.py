from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student

# READ: Displays all students
class StudentListView(ListView):
    model = Student
    template_name = 'records/student_list.html'
    context_object_name = 'students'

# CREATE: Shows a form to add a new student
class StudentCreateView(CreateView):
    model = Student
    template_name = 'records/student_form.html'
    fields = ['first_name', 'last_name', 'email', 'course']
    success_url = reverse_lazy('student_list')

# UPDATE: Shows a form to edit an existing student
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'records/student_form.html'
    fields = ['first_name', 'last_name', 'email', 'course']
    success_url = reverse_lazy('student_list')

# DELETE: Asks for confirmation before deleting
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'records/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')