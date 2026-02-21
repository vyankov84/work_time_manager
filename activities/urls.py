from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.activity_list, name='activity-list'),
    path('create/', views.activity_create, name='activity-create'),
    path('<int:pk>/edit/', views.activity_update, name='activity-update'),
    path('<int:pk>/delete/', views.activity_delete, name='activity-delete'),

]

