from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader
import pytube


def index(request):
    return HttpResponse("Hello World")


def title(request, url):
    video_title = pytube.YouTube(url).title
    thumbnail = pytube.YouTube(url).thumbnail_url
    template = loader.get_template('download.html')
    context = {
        'video_title': video_title,
        'url': url,
        'thumbnail': thumbnail,
    }
    return HttpResponse(template.render(context, request))


def download(request, url):
    return FileResponse(
        open(pytube.YouTube(url).streams.get_highest_resolution().download(
            skip_existing=True), 'rb'),
        as_attachment=True, filename="vid.mp4"
    )
