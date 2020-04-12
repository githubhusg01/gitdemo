from django.http import HttpResponse


def index_views(request):
    return HttpResponse("hello git！")

def index_views2(request):
    return HttpResponse("hello git2！")