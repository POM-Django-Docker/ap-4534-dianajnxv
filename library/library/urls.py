"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""library URL Configuration"""
from django.contrib import admin
from django.urls import path
from authentication import views as auth_views
from book import views as book_views
from author import views as author_views
from order import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/register/', auth_views.register_view, name='register'),
    path('auth/login/', auth_views.login_view, name='login'),
    path('auth/logout/', auth_views.logout_view, name='logout'),

    path('user/', auth_views.user_list, name='user_list'),
    path('user/<int:user_id>/', auth_views.user_detail, name='user_detail'),

    path('authors/', author_views.author_list, name='author_list'),
    path('authors/create/', author_views.create_author, name='create_author'),
    path('authors/delete/<int:author_id>/', author_views.delete_author, name='delete_author'),

    path('books/', book_views.books_list, name='books_list'),
    path('books/<int:book_id>/', book_views.book_detail, name='book_detail'),
    path('books/filter/', book_views.books_filter, name='books_filter'),
    path('books/user/<int:user_id>/', book_views.books_by_user, name='books_by_user'),

    path('orders/', order_views.orders_list, name='orders_list'),
    path('orders/my/', order_views.my_orders, name='my_orders'),
    path('orders/create/', order_views.create_order, name='create_order'),
    path('orders/close/<int:order_id>/', order_views.close_order, name='close_order'),
]