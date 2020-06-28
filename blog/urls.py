from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('test_full_Django/', views.get_result, name='get_result'),
    path('test_REST_Django/', views.Result_view.as_view()),
#    path('test/', views.Result_view, name='views.Result_view'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
