from django.shortcuts import render, redirect
from order.models import Order
from book.models import Book
import datetime


def orders_list(request):
    if request.user.role != 1:
        return redirect("/")

    orders = Order.get_all()
    return render(request, "orders_list.html", {"orders": orders})


def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders_list.html", {"orders": orders})


def create_order(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = Book.get_by_id(book_id)

        plated_end_at = datetime.datetime.now() + datetime.timedelta(days=14)

        Order.create(request.user, book, plated_end_at)

        return redirect("/orders/my/")

    books = Book.get_all()
    return render(request, "create_order.html", {"books": books})


def close_order(request, order_id):
    if request.user.role != 1:
        return redirect("/")

    order = Order.get_by_id(order_id)

    if order:
        order.update(end_at=datetime.datetime.now())

    return redirect("/orders/")