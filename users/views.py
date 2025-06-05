from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrácia prebehla úspešne.")
            return redirect('home')  # alebo kam chceš
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
