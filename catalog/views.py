from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""

    num_books = Book.objects.count()
    num_instances = BookInstance.objects.all().count()
    books_with_the = Book.objects.filter(title__regex=r'The.*').count()
    num_genres = Genre.objects.count()
    # Count the number of genres containing 'fiction'
    fiction_genres = Genre.objects.filter(name__icontains='fiction').count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'books_with_the': books_with_the,
        'num_genres': num_genres,
        'fiction_genres': fiction_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    ordering = ['title']

class BookDetailView(generic.DetailView):
    model = Book
