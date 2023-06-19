from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    messages.success(request, "Kamu berhasil keluar!")
    return redirect('/')

