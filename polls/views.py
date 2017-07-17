"""
from django.shortcuts import render
from .models import Question
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Choice, Question
from django.views import generic

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import *
from django.utils import timezone
from .models import Choice, Question
from .forms import QuestionForm,ChoiceForm
#creation d'une question
class CreateQuestionView(CreateView):
      model = Question
      fields='__all__'
      template_name = 'newquestion.html'
 
      def get_success_url(self):
        return reverse('polls:listequestion')

      def get_context_data(self,**kwargs):
         context = super(CreateQuestionView, self).get_context_data(**kwargs)
         context['action'] = reverse('polls:newquestion')
         return context

class CreateChoiceView(CreateView):
      model = Choice
      fields='__all__'
      template_name = 'polls/newchoices.html'
 
      def get_success_url(self):
        return reverse('polls:listechoice')

def get_context_data(self,**kwargs):
        context = super(UpdateChoiceView, self).get_context_data(**kwargs)
        context['action'] = reverse('polls:updatechoice',kwargs={'pk': self.get_object().id})
        return context
#modifier une question et un choix
class UpdateQuestionView(UpdateView):
      model = Question
      fields='__all__'
      template_name = 'polls/updatequestion.html'
 
      def get_success_url(self):
        return reverse('polls:listequestion')

      def get_context_data(self,**kwargs):
        context = super(UpdateQuestionView, self).get_context_data(**kwargs)
        context['action'] = reverse('polls:updatequestion',kwargs={'pk': self.get_object().id})
        return context


class UpdateChoiceView(UpdateView):
      model = Choice
      fields='__all__'
      template_name = 'polls/updatechoice.html'
 
      def get_success_url(self):
        return reverse('polls:listechoice')

      def get_context_data(self,**kwargs):
        context = super(UpdateChoiceView, self).get_context_data(**kwargs)
        context['action'] = reverse('polls:updatechoice', kwargs={'pk': self.get_object().id})
        return context

#supprimer une question et un choix
class DeleteQuestionView(DeleteView):
      model = Question
      fields='__all__'
      template_name = 'polls/deletequestion.html'
 
      def get_success_url(self):
        return reverse('polls:listequestion')

class DeleteChoiceView(DeleteView):
      model = Choice
      fields='__all__'
      template_name = 'polls/deletechoice.html'
 
      def get_success_url(self):
        return reverse('polls:listechoice')


def addquestion(request):
    if request.method=='POST':

       form=QuestionForm(request.POST)
       if form.is_valid():
          form.save()
          return render(request, 'polls/index.html')


    else:
        form=QuestionForm()
    return render(request, 'polls/addquestion.html',{'form':form})

def addchoice(request):
     if request.method=='POST':

        form=ChoiceForm(request.POST)
        if form.is_valid():
           form.save()
           return render(request, 'polls/index.html')
     else:
          form=ChoiceForm()
     return render(request, 'polls/addchoise.html',{'form':form})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class ListQuestionView(generic.ListView):
    template_name = 'polls/listequestion.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.all() 

class ListChoiceView(generic.ListView):
    template_name = 'polls/listechoice.html'
    context_object_name = 'choice_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Choice.objects.all() 


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
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
 
 
def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


 
