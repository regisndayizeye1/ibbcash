from profiles.models import User
from transfers.models import *
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *



class TransferForm(forms.ModelForm):
    def __init__(self,*args,**kargs):
        super(TransferForm,self).__init__(*args,**kargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.form_id = 'transfer-form'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-3'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Envoyer'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
          Fieldset('sender',
            Field('last_namesender','first_namesender','montant', 'villesender',css_class='same-class'),
          ),
          Fieldset('Receiver',
            Field('last_namereceiver','first_namereceiver',style="color:green;"),
          ),
          )
 
   
    class Meta:

         model =Transfert
         fields =('last_namesender','first_namesender','montant','villesender','last_namereceiver','first_namereceiver')

class MtcnForm(forms.ModelForm):
    def __init__(self,*args,**kargs):
        super(MtcnForm,self).__init__(*args,**kargs)
      
 
    class Meta:

         model =Transfert
         fields =('MTCN',)

class ReceiveForm(forms.ModelForm):
    def __init__(self,*args,**kargs):
        super(ReceiveForm,self).__init__(*args,**kargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['last_namesender'].widget.attrs['readonly'] =True
            self.fields['first_namesender'].widget.attrs['readonly'] =True
            self.fields['montant'].widget.attrs['readonly'] =True
            self.fields['villesender'].widget.attrs['readonly'] =True
            self.fields['last_namereceiver'].widget.attrs['readonly'] =True
            self.fields['first_namereceiver'].widget.attrs['readonly'] =True
            
           
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.form_id = 'transfer-form'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Envoyer'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
           Fieldset('sender',
            Field('last_namesender','first_namesender','montant', 'villesender',css_class='same-class'),
          ),
          Fieldset('Receiver',
            Field('last_namereceiver','first_namereceiver','cni','villereceiver','adressereceiver','fonenumber',style="color:green;"),
          ),
          )
 
   
    class Meta:

         model =Transfert
         fields =('last_namesender','first_namesender','montant','villesender','last_namereceiver','first_namereceiver','cni', 'villereceiver','adressereceiver','fonenumber')





