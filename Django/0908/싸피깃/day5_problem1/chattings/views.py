from django.shortcuts import render, redirect

from chattings.forms import ChatForm
from .models import Chat

# Create your views here.
def index(request):
    chattings = Chat.objects.all()
    context = {
        'chattings': chattings,
    }
    return render(request, 'chattings/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chattings:index')
    else:
        form = ChatForm()
    context = {
        'form': form,
    }
    return render(request, 'chattings/create.html', context)

def detail(request, pk):
    chatting = Chat.objects.get(pk=pk)
    context = {
        'chatting': chatting,
    }
    return render(request, 'chattings/detail.html', context)