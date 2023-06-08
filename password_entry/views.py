from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import PasswordEntry
from .forms import PasswordEntryForm

#PASSWWORD MANAGEMENT CRUD FUNCTIONALITIES

@login_required
def password_list(request):
    passwords = PasswordEntry.objects.filter(user=request.user)
    return render(request, 'password_list.html', {'passwords': passwords})

@login_required
def password_create(request):
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user
            password_entry.save()
            return redirect('password_list')
    else:
        form = PasswordEntryForm()
    return render(request, 'password_create.html', {'form': form})

@login_required
def password_detail(request, pk):
    password_entry = get_object_or_404(PasswordEntry, pk=pk, user=request.user)
    return render(request, 'password_detail.html', {'password_entry': password_entry})
    
    
@login_required
def password_update(request, pk):
    password_entry = get_object_or_404(PasswordEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST, instance=password_entry)
        if form.is_valid():
            form.save()
            return redirect('password_list')
    else:
        form = PasswordEntryForm(instance=password_entry)
    return render(request, 'password_update.html', {'form': form, 'password_entry': password_entry})


@login_required
def password_delete(request, pk):
    password_entry = get_object_or_404(PasswordEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        password_entry.delete()
        return redirect('password_list')
    return render(request, 'password_delete.html', {'password_entry': password_entry})



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})


