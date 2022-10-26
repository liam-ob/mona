from django.shortcuts import render
from instascrape import Instascraper
from .models import InstaPhoto
from django.views.generic import TemplateView
# Create your views here.


def index(request):
    context = InstaPhoto.objects.all()
    return render(request, 'home/index.html', context={'context': context})


def refresh(request):
    # ramona = Profile('ramona261', data={'username': 'ramona261'})
    # ramona.scrape()
    #
    # recents = ramona.get_recent_posts()
    # chris_photos = [post for post in recents if not post.is_video]
    #
    # for post in chris_photos:
    #     fname = post.upload_date.strftime("%Y-%m-%d %Hh%Mm")
    #     if InstaPhoto.objects.get(name=fname).exists():
    #         pass
    #     else:
    #         # post.download(f"{fname}.png")
    #         InstaPhoto.objects.create(name=fname, image=post)

    with Instascraper() as insta:
        posts = insta.profile('ramona261').timeline_posts()
        for post in posts:
            fname = post.upload_date.strftime("%Y-%m-%d %Hh%Mm")
            if InstaPhoto.objects.get(name=fname).exists():
                pass
            else:
                # post.download(f"{fname}.png")
                InstaPhoto.objects.create(name=fname, image=post)


    index(request)
