from django.shortcuts import render, get_object_or_404
from.models import Albums, Song
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

# Create your views here.

'''def index(request):
    all_objects = Album.objects.all()
    html = ''
    for album in all_objects:
        url = "/music/" + str(album.id) + "/"
        html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)
'''
def index(request):
    all_albums = Albums.objects.all()
    return render(request, 'musicapp/index.html', {'all_albums': all_albums
    })
    '''template = loader.get_template('musicapp/index.html')
    return HttpResponse(template.render(context,request))'''


def detail(request, album_id,):
   album = get_object_or_404(Albums, pk = album_id)
   return render(request, 'musicapp/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except (KeyError, Song.DoesNotExist):
         return render(request, 'music/detail.html',{'album': album,
                                                     'error_message': "You did not select a valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'musicapp/detail.html', {'album': album})