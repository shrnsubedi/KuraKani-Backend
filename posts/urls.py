from django.urls import path
from .views import PostList, PostDetail, GetUser

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('getuser/', GetUser.as_view())
]
