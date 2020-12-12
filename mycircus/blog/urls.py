
from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.landing_page,name='landing_page'),
    path('blogs/',views.blog_index,name='blog_index'),
     path('blog/edit/<int:pk>/', views.blog_edit, name='blog_edit'), 
    path('blogs/<int:pk>/',views.blog_detail,name='blog_detail'),
    path('create_blog/',views.blog_create,name='blog_create'),
     path('blog/delete/<int:pk>/', views.blog_delete, name='blog_delete'), 
    path('contact/', views.contact, name='contact'),
     path('project/', views.project, name='project'),
      
      
]

