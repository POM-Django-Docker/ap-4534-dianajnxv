from django.shortcuts import render
from book.models import Book
from order.models import Order


def books_list(request):
    books = Book.get_all()
    return render(request, "books_list.html", {"books": books})


def book_detail(request, book_id):
    book = Book.get_by_id(book_id)
    return render(request, "book_detail.html", {"book": book})


def books_filter(request):
    name = request.GET.get("name")
    books = Book.objects.all()

    if name:
        books = books.filter(name__icontains=name)

    return render(request, "books_list.html", {"books": books})


def books_by_user(request, user_id):
    orders = Order.objects.filter(user_id=user_id)
    books = [order.book for order in orders]

    return render(request, "books_list.html", {"books": books})