from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactSerializer
from contacts.models import Contact
from django.shortcuts import get_object_or_404



class ContactList(APIView):
    def get(self,request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

class ContactCreate(APIView):
    def post(self,request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ContactDetail(APIView):
    def get(self, request,pk):
        contact = get_object_or_404(Contact, id=pk)

        serializer = ContactSerializer(contact)
        return Response(serializer.data)


class ContactDelete(APIView):
    def delete(self,request,pk):
        contact = get_object_or_404(Contact, id=pk)
        contact.delete()
        return Response({'deleted':True})

class ContactUpdate(APIView):
    def put(self,request,pk):
        contact = get_object_or_404(Contact, id=pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def patch(self,request,pk):
        contact = get_object_or_404(Contact, id=pk)
        serializer = ContactSerializer(contact, data=request.data)


