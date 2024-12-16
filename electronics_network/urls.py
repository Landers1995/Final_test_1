from electronics_network.apps import ElectronicsNetworkConfig
from django.urls import path

from electronics_network.views import FactoryCreateAPIView, FactoryListAPIView, FactoryRetrieveAPIView, \
    FactoryUpdateAPIView, FactoryDestroyAPIView, RetailChainCreateAPIView, RetailChainListAPIView, \
    RetailChainRetrieveAPIView, RetailChainUpdateAPIView, RetailChainDestroyAPIView, EntrepreneurCreateAPIView, \
    EntrepreneurListAPIView, EntrepreneurRetrieveAPIView, EntrepreneurUpdateAPIView, EntrepreneurDestroyAPIView

app_name = ElectronicsNetworkConfig.name

urlpatterns = [
    path('factory/create/', FactoryCreateAPIView.as_view(), name='factory-create'),
    path('factory/', FactoryListAPIView.as_view(), name='factory-list'),
    path('factory/<int:pk>/', FactoryRetrieveAPIView.as_view(), name='factory-retrieve'),
    path('factory/update/<int:pk>/', FactoryUpdateAPIView.as_view(), name='factory-update'),
    path('factory/delete/<int:pk>/', FactoryDestroyAPIView.as_view(), name='factory-destroy'),

    path('retail/create/', RetailChainCreateAPIView.as_view(), name='retail-create'),
    path('retail/', RetailChainListAPIView.as_view(), name='retail-list'),
    path('retail/<int:pk>/', RetailChainRetrieveAPIView.as_view(), name='retail-retrieve'),
    path('retail/update/<int:pk>/', RetailChainUpdateAPIView.as_view(), name='retail-update'),
    path('retail/delete/<int:pk>/', RetailChainDestroyAPIView.as_view(), name='retail-destroy'),

    path('ep/create/', EntrepreneurCreateAPIView.as_view(), name='entrepreneur-create'),
    path('ep/', EntrepreneurListAPIView.as_view(), name='entrepreneur-list'),
    path('ep/<int:pk>/', EntrepreneurRetrieveAPIView.as_view(), name='entrepreneur-retrieve'),
    path('ep/update/<int:pk>/', EntrepreneurUpdateAPIView.as_view(), name='entrepreneur-update'),
    path('ep/delete/<int:pk>/', EntrepreneurDestroyAPIView.as_view(), name='entrepreneur-destroy'),
]