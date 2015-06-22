from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def timeshow(request):
    now = datetime.datetime.now()
    return HttpResponse(now)
