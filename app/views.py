from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.serializers import *
from rest_framework.response import Response

class ProductCrud(ViewSet):
    def list(self,request):
        ormobjs = Product.objects.all()
        jobj = ProductModelSerializer(ormobjs,many=True)
        return Response(jobj.data)
    def retrieve(self,request,pk):
        ormobj = Product.objects.get(pk=pk)
        jobj = ProductModelSerializer(ormobj)
        return Response(jobj.data)
    def create(self,request):
        jobj = request.data
        ormobj = ProductModelSerializer(data = jobj)
        if ormobj.is_valid():
            ormobj.save()
            return Response({'Inserted':'Successfully'})
        else:
            return Response({'Error':'Please enter valid data'})
    def update(self,request,pk):
        ormobj = Product.objects.get(pk=pk)
        ormobj = ProductModelSerializer(ormobj,data = request.data)
        if ormobj.is_valid():
            ormobj.save()
            return Response({'Updated':'Successfully'})
        else:
            return Response({'Error':'Invalid Data please give valid'})
    def partial_update(self,request,pk):
        ormobj = Product.objects.get(pk=pk)
        ormobj  = ProductModelSerializer(ormobj,data=request.data,partial = True)
        if ormobj.is_valid():
            ormobj.save()
            return Response({'Partial updated':'Successfully'})
        else:
            return Response({'Error':'Please enter valid data'})
    def destroy(self,request,pk):
        ormobj = Product.objects.get(pk=pk).delete()
        return Response({'deleted':'Successfully..'})