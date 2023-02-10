from django.shortcuts import render, get_object_or_404
from .models import Genre, Ebook
from django.db.models import Q  # New



def homePage(request):
    ebooks = Ebook.objects.all().order_by('-postDate')[:4]
    return render(request, "book/home.html", {
        'ebooks': ebooks
    })

def bookDetail(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    return render(request, "book/book-detail.html", {
        'ebook': ebook
    })

def allBooks(request):
    ebooks = Ebook.objects.all().order_by('-postDate')
    return render(request, "book/all-books.html", {
        'ebooks': ebooks
    })

def allGenres(request):
    genres = Genre.objects.all()
    return render(request, "book/genres.html", {
        'genres': genres
    })

def genreDetails(request, slug=None):
    genre = None
    genres = Genre.objects.all()
    ebooks = Ebook.objects.all().order_by('-postDate')
    if slug:
        genre = get_object_or_404(Genre, slug=slug)
        ebooks = ebooks.filter(genre=genre)
    return render(request, "book/genre-detail.html", {
        'genre': genre,
        'genres': genres,
        'ebooks': ebooks
    })

def searchBook(request):
    return render(request, "book/search.html")

def searchResults(request):
    searchBook = request.GET.get('search')
    if searchBook:
        ebooks = Ebook.objects.filter(Q(title__icontains=searchBook) & Q(description__icontains=searchBook))
    else:
        ebooks = Ebook.objects.all().order_by("-postDate")

    return render(request, "book/search-results.html", {
        'ebooks': ebooks,
    })
