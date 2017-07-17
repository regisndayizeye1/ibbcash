from django.shortcuts import render
from django.db.models import Q
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from transfers.forms import *
from transfers.models import *
import random,string
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def calculcios(montant):
    tarif=Tarif.objects.all()
    cios=0
    for t in tarif:
           if t.limit_inferior< montant and montant<= t.limit_superior :
              cios =t.montant
    return cios

def addtransfer(request):  
 
    if request.method=='POST':
       montant =int(request.POST['montant'])
       user=request.user
       guichet=request.user.guichet
    
       trs=Transfert.objects.create(MTCN=mtcngenerate(),last_namesender=request.POST['last_namesender'],first_namesender=request.POST['first_namesender'],last_namereceiver=request.POST['last_namereceiver'],first_namereceiver=request.POST['first_namereceiver'], montant=montant,commission=calculcios(montant),user_sender=user,guichet_sender=guichet)
       return render(request, 'transfers/addtransfer.html',{'trs':trs})
    else:
      form=TransferForm()       
      return render(request, 'transfers/addtransfer.html',{'form':form})
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

def paytransfer(request):
    if request.method=='POST':
       mtcn =request.POST['MTCN']
       transfer=Transfert.objects.get(Q(MTCN=mtcn) & Q(statut="ENVOYE"))
       if transfer:
          return render(request, 'transfers/paytransfer.html',{'transfer':transfer})
       else:
            return render(request, 'transfers/paytransfer.html',{'form':form})
    else:
        form=MtcnForm()       
        return render(request, 'transfers/paytransfer.html',{'form':form})

#valider les transfers
def validetransfer(request):
    if request.method=='POST':
       user =request.user
       guichet=request.user.guichet
       transfer= Transfert.objects.update(statut='RECU',datereceiver=timezone.now(),guichet_receiver=guichet, user_receiver=user )
       return render(request, 'transfers/validetransfer.html',{'transfer':transfer})

    else:
        form=TransferForm()       
        return render(request, 'transfers/paytransfer.html',{'form':form})

def transferdetail(request, transfer_id):
    transfer = get_object_or_404(Transfer, pk=transfer_id)
    return render(request, 'transfers/transferdetail.html', {'transfer': transfer})


def updateTransfer(request,pk):
    transfer=Transfert.objects.get(pk=pk)
    form =ReceiveForm(request.POST or None,instance=transfer)
    user=request.user
    guichet=request.user.guichet
    if request.method=='POST':
       trs=Transfert.objects.get(pk=pk)
       trs.cni=request.POST['cni']
       trs.datereceiver=timezone.now()
       trs.statut="RECU"
       trs.user_receiver=user
       trs.guichet_receiever=guichet
       trs.save()
       return render(request,'transfers/validetransfer.html',{'trs': trs})
    else:
      return render(request,'transfers/validetransfer.html',{'form': form})

def index(request):
    transfer= Transfert.objects.filter(statut='ENVOYE')
    return render(request,'transfers/index.html',{'transfer': transfer})

def listetransferpayes(request):
    transfers= Transfert.objects.filter(statut='RECU')
    return render(request,'transfers/index.html',{'transfers': transfers})
####################################################################################################
    ######################### #les vieux generiques#########################
class createvieutransfer(CreateView):
      form_class=TransferForm
      template_name='transfers/createvieutransfer.html'
      context_object_name = "transfert"
      
      def form_valid(self,form):
          instance=form.save(commit=False)
          instance.MTCN=mtcngenerate()
          instance.user_sender=self.request.user
          instance.guichet_sender=self.request.user.guichet
          instance.commission=calculcios(instance.montant)
          instance.save()

      def get_success_url(self):
        return reverse('transfers:addtransfer')
















