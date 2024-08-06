from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Autor, Album
from album_manager.forms import AlbumForm, AutorForm
# Create your views here.

def index(request):
    albums = Album.objects.order_by('album_name')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'albums': albums}, request))

def autors_list(request):
    autors = Autor.objects.order_by('first_name')
    template = loader.get_template('autors_list.html')
    return HttpResponse(template.render({'autors': autors}, request))
    

def album(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def autor(request, autor_id):
    autor = get_object_or_404(Autor, pk = autor_id)
    template = loader.get_template('display_autor.html')
    context = {
        'autor': autor
    }
    return HttpResponse(template.render(context, request))

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()
    
    return render(request, 'add_album.html', {'form': form})





def add_autor(request):
    if request.method =='POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AutorForm()
    return render(request, 'add_autor.html', {'form':form})




def edit_album(request, id):
    album = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album)

    return render(request, 'add_album.html', {'form': form})


def edit_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk = autor_id) 
    if request.method =='POST':
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'add_autor.html', {'form':form})
    


def delete_album(request, id):
    album = get_object_or_404(Album, pk = id)
    album.delete()
    return redirect("album_manager:index")
    
    

def delete_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk = autor_id)
    autor.delete()
    return redirect("album_manager:index")