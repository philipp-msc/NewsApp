from django.urls import path
from .views import PostsList, PostDetail, PostsSearch

urlpatterns = [
    path('', PostsList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', PostsSearch.as_view(), name='post_search'),
]