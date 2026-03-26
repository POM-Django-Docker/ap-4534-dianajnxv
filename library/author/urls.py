from django.urls import path
from . import views

urlpatterns = [

    path('list/', views.author_list, name='author_list'),
    path("create/", views.create_author, name="create_author"),
    path("delete/<int:id>/", views.delete_author, name="delete_author"),

]