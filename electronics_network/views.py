from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from electronics_network.permissions import IsActive
from electronics_network.serializer import FactorySerializer, RetailChainSerializer, EntrepreneurSerializer
from electronics_network.models import Factory, RetailChain, Entrepreneur


class FactoryCreateAPIView(generics.CreateAPIView):
    serializer_class = FactorySerializer
    permission_classes = [IsActive]


class FactoryListAPIView(generics.ListAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    permission_classes = [IsActive]


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class FactoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class FactoryDestroyAPIView(generics.DestroyAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class RetailChainCreateAPIView(generics.CreateAPIView):
    serializer_class = RetailChainSerializer
    permission_classes = [IsActive]


class RetailChainListAPIView(generics.ListAPIView):
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    permission_classes = [IsActive]


class RetailChainRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()
    permission_classes = [IsActive]


class RetailChainUpdateAPIView(generics.UpdateAPIView):
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()
    permission_classes = [IsActive]


class RetailChainDestroyAPIView(generics.DestroyAPIView):
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()
    permission_classes = [IsActive]


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    serializer_class = EntrepreneurSerializer
    permission_classes = [IsActive]


class EntrepreneurListAPIView(generics.ListAPIView):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    permission_classes = [IsActive]


class EntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsActive]


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsActive]


class EntrepreneurDestroyAPIView(generics.DestroyAPIView):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsActive]

