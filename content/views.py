from django.shortcuts import render

from content.models import *
from content.serializers import *
from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date,timedelta
from django.core.mail import EmailMessage
from DRFBoilerPlate import local_settings
import calendar



class Model1ViewSet(viewsets.ModelViewSet):
    serializer_class = Model1Serializer
    permission_classes=[
         permissions.IsAuthenticated
    ]

    #if necessary
    # def get_queryset(self):
    #     return self.request.user.models1.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class Model2ViewSet(viewsets.ModelViewSet):
    serializer_class = Model2Serializer
    permission_classes=[
         permissions.IsAuthenticated
    ]

    #if necessary
    # def get_queryset(self):
    #     return self.request.user.models2.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)




#APIVIEW Examples

# class MarkAllReaded(APIView):
#     permission_classes=[
#          permissions.IsAuthenticated
#     ]
#     serializer_class=NotificationsSerializer
#     def post(self,request):
#         self.request.user.notifications.filter(readed=False).update(readed=True)
#         return Response(status=status.HTTP_200_OK )   

# class MarkReaded(APIView):
#     permission_classes=[
#          permissions.IsAuthenticated
#     ]
#     serializer_class=NotificationsSerializer
#     def post(self,request):
#         self.request.user.notifications.filter(id=request.data.get('id')).update(readed=True)
#         queryset=self.request.user.notifications.filter(id=request.data.get('id'))
#         serializer = self.serializer_class(queryset,many=True)
#         return Response(serializer.data )   



#SEND MAIL
# class SendMailView(APIView):
#     def post(self,request):
#         user=self.request.user
#         invoices= user.invoices.filter(id=request.data.get('id'))
#         if(invoices.__len__()==1):
#             invoice=invoices[0]
#             if(user.company_name!=None):
#                 subject = f'Invoice, {user.company_name}'
#             else:
#                 subject = 'Invoice'
#             if(user.default_message!=None):
#                 body=user.default_message
#             else:
#                 body = f'Thank you for your business, Please submit via Direct Deposit, Check or EFS Check. For billing information please contact us at {user.email}' 
#             to = invoice.customer.email 
#             mail = EmailMessage(subject, body, local_settings.EMAIL_HOST_USER, [to])  
#             if(invoice.load.confirmation!=None and invoice.load.confirmation!=''):
#                 mail.attach(invoice.load.confirmation.name, invoice.load.confirmation.read())
#             if(invoice.load.bol!=None and invoice.load.bol!=''):    
#                 mail.attach(invoice.load.bol.name, invoice.load.bol.read())
#             mail.attach(request.data.get('invoice').name, request.data.get('invoice').read())
#             ix=mail.send()
#             return Response(ix)  
#         return Response(status=status.HTTP_404_NOT_FOUND,data={"msg":"Invoice not found"})
