from django.contrib.auth.decorators import permission_required
from django.shortcuts import HttpResponse


@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    return HttpResponse("Book added successfully")


@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    return HttpResponse("Book updated successfully")


@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    return HttpResponse("Book deleted successfully")

relationship_app.can_add_book
relationship_app.can_change_book
relationship_app.can_delete_book