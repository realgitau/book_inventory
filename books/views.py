from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'books/index.html', {})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'books/book_search.html', {'books': books})

def book_filter(request):
    genre = request.GET.get('genre')
    books = Book.objects.filter(genre=genre)
    return render(request, 'books/book_filter.html', {'books': books})

# populating the database
def populate_books():
    books_data = [
        {
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'genre': 'Fiction'
        },
        {
            'title': 'To Kill a Mockingbird',
            'author': 'Harper Lee',
            'genre': 'Fiction'
        },
        {
            'title': '1984',
            'author': 'George Orwell',
            'genre': 'Science Fiction'
        },
        {
            'title': 'Pride and Prejudice',
            'author': 'Jane Austen',
            'genre': 'Romance'
        },
        {
            'title': 'The Catcher in the Rye',
            'author': 'J.D. Salinger',
            'genre': 'Fiction'
        }
    ]

    for book in books_data:
        book = Book.objects.create(title=book['title'], author=book['author'], genre=book['genre'])
        book.save()

    return len(books_data)
