from django.http import HttpResponse


def index_views(request):
    return HttpResponse("hello git")