from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from .models import MyURL


def index(request):
    return HttpResponse("Xin chào, đây là hệ thống rút gọn link của công ty X. Tôi có thể giúp gì cho bạn")


def list_url(request):
    my_urls = MyURL.objects.all()
    template = '<a href="/url-shortener/detail/{alias}/">/url-shortener/{alias}</a> --> {url}<br/>'
    value = ""
    for my_url in my_urls:
        value += template.format(alias=my_url.alias, url=my_url.url)
    return HttpResponse(value)


def detail(request, alias):
    try:
        my_url = MyURL.objects.get(alias=alias)
    except MyURL.DoesNotExist:
        raise Http404("alias does not exist")
    return redirect(my_url.url)
