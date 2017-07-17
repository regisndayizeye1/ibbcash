from django import forms
from .models import Choice, Question

class QuestionForm(forms.ModelForm):
    def __init__(self,*args,**kargs):
        super(QuestionForm,self).__init__(*args,**kargs)
   
    class Meta:

         model =Question
         fields='__all__'
class ChoiceForm(forms.ModelForm):
    def __init__(self,*args,**kargs):
        super(ChoiceForm,self).__init__(*args,**kargs)
   
    class Meta:

         model =Choice
         fields='__all__'


