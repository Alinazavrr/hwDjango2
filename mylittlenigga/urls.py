from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdList, name='ad_list'),
    path('ad/<int:pk>', views.AdDetail, name='ad_detail'),
    path('ad/create', views.AdCreate, name='ad_create'),
    path('ad/<int:pk>/update', views.AdUpdate, name='ad_update'),
    path('ad/<int:pk>/delete', views.AdDelete, name='ad_delete'),
    path('ad/<int:pk>/comment', views.CommentCreate, name='comment_create'),
]