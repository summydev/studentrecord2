from django.urls import path
from . import views

urlpatterns = [
    # Web Routes (HTML)
    path('', views.StudentListView.as_view(), name='student_list'),
    path('new/', views.StudentCreateView.as_view(), name='student_create'),
    path('<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    
    # API Routes (JSON)
    path('api/students/', views.StudentListCreateAPIView.as_view(), name='api_student_list_create'),
    path('api/students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='api_student_detail'),
    path('api/register/', views.RegisterAPIView.as_view(), name='api_register'),
]