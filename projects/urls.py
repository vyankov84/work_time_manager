from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.dashboard, name='home'),

    path('list/', views.project_list, name='project-list'),

    path('<int:pk>/', views.project_details, name='project-detail'),

    path('create/', views.project_create, name='project-create'),

    path('<int:pk>/edit/', views.project_update, name='project-update'),

    path('<int:pk>/delete/', views.project_delete, name='project-delete'),
]
