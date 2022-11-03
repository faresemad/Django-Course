from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.post_details, name='post_details'),
    path('<int:id>/update', views.post_update, name='post_update'),
    path('<int:id>/delete', views.post_delete, name='post_delete'),
    path('create/', views.post_create, name='post_create'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
