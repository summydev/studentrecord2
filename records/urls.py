# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.StudentListView.as_view(), name='student_list'),
#     path('new/', views.StudentCreateView.as_view(), name='student_create'),
#     path('<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),
#     path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for listing all students or creating a new one
    path('api/students/', views.StudentListCreateAPIView.as_view(), name='api_student_list_create'),
    
    # Endpoint for viewing, updating, or deleting a specific student (e.g., /api/students/1/)
    path('api/students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='api_student_detail'),
]