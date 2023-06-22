from django.urls import path
from .views import PostDetailApiView,PostListViewApi, UpvotePostView, CommentAPIView, UserPostApiView


urlpatterns =[
    path('',PostDetailApiView.as_view()),
    path('<int:pk>/', PostDetailApiView.as_view()),
    path('<int:pk>/upvote/', UpvotePostView.as_view()),
    path('<int:pk>/comment/',CommentAPIView.as_view()),
    path('<username>/',UserPostApiView.as_view())



]