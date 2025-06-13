from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def redirect_if_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper

@redirect_if_authenticated
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(email=email, password=password)
            return redirect('login')
        else:
            return render(request, 'core/register.html', {'error': 'Email already registered'})
    return render(request, 'core/register.html')

@redirect_if_authenticated
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redirect ke halaman home setelah login
        else:
            return render(request, 'core/login.html', {'error': 'Invalid email or password'})
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
