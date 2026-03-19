from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# GET (List all students) and POST (Create a new student)
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# GET (Retrieve one), PUT (Update), and DELETE (Destroy a student)
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer