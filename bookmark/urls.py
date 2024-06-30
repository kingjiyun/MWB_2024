from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmark_list, name='bookmark_list'),
    path('new/', views.bookmark_create, name='bookmark_create'),
    path('detail/<int:id>/', views.bookmark_detail, name='bookmark_detail'),
    path('edit/<int:id>/', views.bookmark_edit, name='bookmark_edit'),
    path('delete/<int:id>/', views.bookmark_delete, name='bookmark_delete'),
]
