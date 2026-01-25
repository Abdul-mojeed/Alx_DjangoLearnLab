from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book




@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    return HttpResponse("Viewing books")


@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("Adding book")


@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    return HttpResponse("Editing book")


@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    return HttpResponse("Deleting book")
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})
