from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('ebook/all/', views.allBooks, name='allBooks'),
    path('genre/all/', views.allGenres, name='allGenres'),
    path('genre/<slug:slug>/', views.genreDetails, name='genreDetails'),
    path('ebook/<int:pk>/', views.bookDetail, name='bookDetail'),
    path('search/', views.searchBook, name='searchBook'),
    path('search/book/list/', views.searchResults, name='searchResults'),
]