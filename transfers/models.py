from __future__ import unicode_literals
from profiles.models import *
from django.db import models
# Create your models here.
class Transfert(models.Model):
     STATUT_CHOICES=(
       ('ENVOYE','ENVOYE'),   
       ('RECU','RECU')
     )

     last_namesender=models.CharField(max_length=50,verbose_name=(u'Nom de l expediteur'))
     first_namesender=models.CharField(max_length=50,verbose_name=(u'Prenom de l expediteur'))
     montant=models.IntegerField(verbose_name=(u'Montant'))
     datedepot=models.DateTimeField(verbose_name=(u'date du depot'),auto_now_add=True)
     villesender=models.CharField(max_length=50,blank=True,null=True,verbose_name=(u'ville de de l expediteur'))
     MTCN=models.CharField(max_length=12,blank=True, null=True,verbose_name=(u'MTCN'),unique=True)
     commission=models.IntegerField(blank=True, null=True)
     last_namereceiver=models.CharField(max_length=50,verbose_name=(u'Last Name'))
     first_namereceiver=models.CharField(max_length=50,verbose_name=(u'Prenom du destinataire'))
     cni=models.CharField(max_length=50,blank=True, null=True,verbose_name=(u'Carte National Identite'))
     datereceiver=models.DateTimeField(blank=True,null=True,verbose_name=(u'Reicever Date') )
     guichet_sender=models.ForeignKey(Guichet, blank=True,null=True) 
     user_sender=models.ForeignKey(User,blank=True, null=True)
     guichet_receiver=models.ForeignKey(Guichet,blank=True, null=True, related_name='guichet_receiver') 
     villereceiver=models.CharField(max_length=50,blank=True,null=True,verbose_name=(u'ville du destinataire'))
     adressereceiver=models.CharField(max_length=50,blank=True,null=True,verbose_name=(u'adresse du         destinataire'))
     fonenumber=models.CharField(max_length=12,blank=True, null=True,verbose_name=(u'Telephone'))
     user_receiver=models.ForeignKey(User,blank=True, null=True, related_name='user_receiver')
     statut=models.CharField(max_length=12,default="ENVOYE",choices=STATUT_CHOICES)




class Tarif(models.Model):
     limit_inferior=models.IntegerField(verbose_name=(u'limite inferieure'))
     limit_superior=models.IntegerField(verbose_name=(u'limite inferieure'))
     montant=models.IntegerField()


     
