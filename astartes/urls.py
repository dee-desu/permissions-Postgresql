from django.urls import path
from .views import MarineListView,MarineDetailView,PostListView,PostDetailView

urlpatterns=[
    path('',MarineListView.as_view(),name='marine_list'),
    path('<int:pk>',MarineDetailView.as_view(),name='marine_detail'),

    path('posts/',PostListView.as_view(),name='Post_list'),
    path('posts/<int:pk>',PostDetailView.as_view(),name='Post_detail'),

    
]