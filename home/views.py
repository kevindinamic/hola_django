from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("<h1>hola django</h1>")
