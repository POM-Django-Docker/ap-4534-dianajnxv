from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        f_name = request.POST.get('first_name', '')
        l_name = request.POST.get('last_name', '')
        m_name = request.POST.get('middle_name', '') 
        role = int(request.POST.get('role', 0))
        
        if not CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                first_name=f_name,
                last_name=l_name,
                middle_name=m_name,
                role=role,
                is_active=True
            )
            return redirect('login')
            
    return render(request, 'auth/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            print(f"DEBUG: User {email} logged in!")
            return redirect('author_list')
        else:
            print("DEBUG: Login failed - invalid credentials")
            
    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def user_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    users = CustomUser.objects.all()

    return render(request, 'users/list.html', {'users': users})


def user_detail(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')

    user = get_object_or_404(CustomUser, id=user_id)

    return render(request, 'users/detail.html', {'user': user})
