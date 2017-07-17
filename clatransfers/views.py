from django.shortcuts import render
from django.db.models import Q
from django.views.generic import *
from django.core.urlresolvers import reverse
from transfers.forms import *
from transfers.models import *
import random,string
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect

def calculcios(montant):
    tarif=Tarif.objects.all()
    cios=0
    for t in tarif:
           if t.limit_inferior< montant and montant<= t.limit_superior :
              cios =t.montant
    return cios

#generer un code MTCN
def mtcngenerate():
       rand_str= lambda n:"".join([random.choice(string.uppercase) for i in xrange(n)])
       r=rand_str(10)
       s=str(timezone.now()).replace(":","").replace("-","").replace(" ","").replace(".","").replace("+","")
       value=r+s
       value_digits=""
       for x in value:
           ord_value=ord(x)
           if 48<=ord_value<=57: # 0-9
              value_digits +=x
           elif 65<= ord_value<=90: # A-Z
              value_digits += str(ord_value-55)
           else:
               raise ValidationError(_('%s is not a valid charcter for MTCN.')%x)
       val=int(value_digits)
       cd=int(98-(val % 97))
       mtcn=value_digits[:9]+str(cd)
       return mtcn

#Transfer de l'argent
class Listdetail(DetailView):
   model = Transfert
   template_name='clatransfers/detailclatransfers.html'
   context_object_name = "transfert"

   
class ListeTransfer(ListView):
      model = Transfert
      template_name='clatransfers/index.html'
      context_object_name = "transfer"
      
      def get_success_url(self):
        return reverse('clatransfers:index')
      def get_queryset(self):
        return Transfert.objects.filter(statut="ENVOYE").order_by('-datedepot')

      def get_context_data(self,**kwargs):
        context = super(ListeTransfer, self).get_context_data(**kwargs)
        context['action'] = reverse('clatransfers:index')
        return context
class ListeTransferRecu(ListView):
      model = Transfert
      template_name='clatransfers/indexrecu.html'
      context_object_name = "transfer"
      
      def get_success_url(self):
        return reverse('clatransfers:indexrecu')
      def get_queryset(self):
        return Transfert.objects.filter(statut="RECU").order_by('-datereceiver')

      def get_context_data(self,**kwargs):
        context = super(ListeTransferRecu, self).get_context_data(**kwargs)
        context['action'] = reverse('clatransfers:indexrecu')
        return context


class createvieutransfer(CreateView):
      model = Transfert
      fields=('last_namesender','first_namesender','montant','villesender','last_namereceiver','first_namereceiver')
      template_name='clatransfers/clapaytransfers.html'
      context_object_name = "transfert"
      
      def form_valid(self,form):
          instance=form.save(commit=False)
          instance.MTCN=mtcngenerate()
          instance.user_sender=self.request.user
          instance.guichet_sender=self.request.user.guichet
          instance.commission=calculcios(instance.montant)
          instance.save()
          return HttpResponseRedirect(self.get_success_url())
         
      def get_success_url(self):
        return reverse('clatransfers:index')

      def get_context_data(self,**kwargs):
        context = super(createvieutransfer, self).get_context_data(**kwargs)
        context['action'] = reverse('clatransfers:createvieutransfer')
        return context


def paytransfers(request):
    if request.method=='POST':
       mtcn =request.POST['MTCN']
       transfer=Transfert.objects.get(MTCN=mtcn) 
       if transfer:
          return render(request, 'clatransfers/paytransfers.html',{'transfer':transfer})
       else:
            return render(request, 'clatransfers/paytransfers.html',{'form':form})
    else:
        form=MtcnForm()       
        return render(request, 'clatransfers/paytransfers.html',{'form':form})

class TransferPay(UpdateView):
      model = Transfert
      form_class=ReceiveForm
      template_name='clatransfers/TransferPay.html'

      def form_valid(self,form):
          instance=form.save(commit=False)
          instance.statut="RECU"
          instance.user_receiver=self.request.user
          instance.guichet_receiver=self.request.user.guichet
          instance.save()
          return HttpResponseRedirect(self.get_success_url())
         
      def get_success_url(self):
        return reverse('clatransfers:indexrecu')

      def get_context_data(self,**kwargs):
        context = super(TransferPay, self).get_context_data(**kwargs)
        context['action'] = reverse('clatransfers:index')
        return context

    #########create pdf en djangop########################""


      
