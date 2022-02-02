from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Olá mundo. Você está no indice da aplicação de enquetes.</h1>")