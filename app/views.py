from django.shortcuts import render
from app.models import Album


def album_list(request):
    albums = Album.objects.all()
    return render(request, "album_list.html", {"albums": albums})


def album_detail(request, id):
    album = Album.objects.get(id=id)
    return render(request, "album_detail.html", {"album": album})


def new_song(request):
    pass
