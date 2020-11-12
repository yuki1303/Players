from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.PostsListView.as_view(), name='post'),
    path('create/', views.CreatePostsView.as_view(), name='create'),
    path('<int:pk>/', views.PostsDetailView.as_view(), name='detail'),
    path('comment/<int:pk>/', views.CommentCreate.as_view(), name='comment'),
    path('<int:pk>/delete/', views.PostsDelete.as_view(), name='delete'),
    path('<int:pk>/comment_delete/', views.CommentDelete.as_view(), name='comment_delete'),
]
