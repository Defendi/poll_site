from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("Você está olhando para a pergunta %s." % question_id)

def results(request, question_id):
    response = "Você está vendo os resultados da pergunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na pergunta %s." % question_id)