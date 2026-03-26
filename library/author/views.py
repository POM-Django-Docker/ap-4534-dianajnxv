from django.shortcuts import render, redirect, get_object_or_404
from .models import Author 

def author_list(request):
    if not request.user.is_authenticated or request.user.role != 1:
        return render(request, 'error.html', {'msg': 'Only for librarians'})
    
    authors = Author.objects.all()
    return render(request, 'authors/list.html', {'authors': authors})

def create_author(request):
    if request.method == 'POST' and request.user.role == 1:
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        Author.objects.create(name=name, surname=surname)
        return redirect('author_list')
    return render(request, 'authors/create.html')

def delete_author(request, author_id):
    if request.user.is_authenticated and request.user.role == 1:
        author = get_object_or_404(Author, id=author_id)
        if not author.books.exists(): 
            author.delete()
    return redirect('author_list')
