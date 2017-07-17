from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$',  views.IndexView.as_view(), name='index'),
    url(r'^addchoice/$', views.addchoice, name='addchoice'),
    url(r'^addquestion/$', views.addquestion, name='addquestion'),
    url(r'^listequestion/$', views.ListQuestionView.as_view(), name='listequestion'),
    url(r'^newquestion/$', views.CreateQuestionView.as_view(), name='newquestion'),
    url(r'^newchoices/$', views.CreateChoiceView.as_view(), name='newchoices'),
    url(r'^updatequestion/(?P<pk>\d+)$',views.UpdateQuestionView.as_view(), name='updatequestion'),
    url(r'^updatechoice/(?P<pk>\d+)/$',views.UpdateChoiceView.as_view(), name='updatechoice'),
    url(r'^deletequestion/(?P<pk>\d+)/$',views.DeleteQuestionView.as_view(),
name='deletequestion'),
    url(r'^deletechoice/(?P<pk>\d+)/$',views.DeleteChoiceView.as_view(),
name='deletechoice'),


    url(r'^listechoice/$', views.ListChoiceView.as_view(), name='listechoice'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
