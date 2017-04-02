from django.http import HttpResponse
from django.template import loader

from .models import Question, PageCount

def index(request):
  row, create = PageCount.objects.get_or_create(page='index')
  row.count += 1
  row.save()
  latest_question_list = Question.objects.order_by('pub_date')[:5]
  template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list': latest_question_list,
    'pagecount': str(row.count),
    }
  return HttpResponse(template.render(context,request))

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
