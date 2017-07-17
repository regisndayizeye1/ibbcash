from django.conf.urls import url
from . import views
app_name = 'clatransfers'
urlpatterns = [
       url(r'^$', views.createvieutransfer.as_view(), name='createvieutransfer'),
       url(r'^index/$', views.ListeTransfer.as_view(), name='index'),
       url(r'^detailclatransfers/(?P<pk>[0-9]+)/$', views.Listdetail.as_view(), name='detailclatransfers'),
       url(r'^paytransfers/$', views.paytransfers, name='paytransfers'),
       url(r'^TransferPay/(?P<pk>[0-9]+)/$', views.TransferPay.as_view(), name='TransferPay'),

      #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
     # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
