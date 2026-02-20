from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.employee_list, name='employee-list'),
    path('<int:pk>/', views.employee_details, name='employee-details'),
    path('create/', views.employee_create, name='employee-create'),
    path('<int:pk>/edit/', views.employee_update, name='employee-update'),
]
