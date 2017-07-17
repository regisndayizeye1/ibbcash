from django.conf.urls import url

from . import views

app_name = 'transfers'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),

     url(r'^$', views.addtransfer, name='addtransfer'),
     url(r'^paytransfer/$', views.paytransfer, name='paytransfer'),
     url(r'^validetransfer/$', views.validetransfer, name='validetransfer'),
     url(r'^index/$', views.index, name='index'),
     url(r'^listetransferpayes/$', views.listetransferpayes, name='listetransferpayes'),
     url(r'^updateTransfer/(?P<pk>\d+)/$', views.updateTransfer, name='updateTransfer'),

###################class baseviewgenerique#########################""
     url(r'^createvieutransfer/$', views.createvieutransfer.as_view(), name='createvieutransfer'),

     # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
      #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
     # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
