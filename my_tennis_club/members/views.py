from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import PhotoAlbum, Photo
from django.template import loader
from .forms import PhotoForm
def album_detail(request, album_id):
    album = get_object_or_404(PhotoAlbum, id=album_id)
    photos = Photo.objects.filter(album=album)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            template = loader.get_template('album_detail.html')
            return HttpResponse(template.render({'album': album, 'photos': photos, 'form': form}, request))
            #return redirect('album_detail', album_id=album_id)
    else:
        form = PhotoForm(initial={'album': album})
    return render(request, 'album_detail.html', {'album': album, 'photos': photos, 'form': form})
