from rest_framework.serializers import ModelSerializer
from electronics_network.models import Factory, RetailChain, Entrepreneur


class UpdateProviderDeptMixin:
    """Данный метод не позводяет менять поле provider_dept с помощью API интерфейса """
    def update(self, instance, validated_data):
        validated_data.pop('provider_dept', None)
        return super().update(instance, validated_data)


class FactorySerializer(UpdateProviderDeptMixin, ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"


class RetailChainSerializer(UpdateProviderDeptMixin, ModelSerializer):
    class Meta:
        model = RetailChain
        fields = "__all__"


class EntrepreneurSerializer(UpdateProviderDeptMixin, ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = "__all__"
