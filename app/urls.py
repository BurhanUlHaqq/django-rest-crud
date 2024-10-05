# urls.py

from django.urls import path
from .views import (
    AuthorListCreateView,
    AuthorRetrieveUpdateDestroyView,
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    ProfileListCreateView,
    ProfileRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Author URLs
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),

    # Book URLs
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    # Profile URLs
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),
]

