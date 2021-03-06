from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question, Choice, PageCount

def index(request):
  row, create = PageCount.objects.get_or_create(page='index')
  row.count += 1
  row.save()
  latest_question_list = Question.objects.order_by('pub_date')[:5]
  context = {
    'latest_question_list': latest_question_list,
    'pagecount': str(row.count),
    }
  return render(request, 'polls/index.html', context)

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'
  
class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    return render(request, 'polls/detail.html', { 'question': question, 'error_message': "You didn't select a choice.",})
  else:
    selected_choice.votes += 1
    selected_choice.save()
  return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
