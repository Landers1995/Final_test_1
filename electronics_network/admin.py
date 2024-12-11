from django.contrib import admin

from electronics_network.models import Factory, RetailChain, Entrepreneur


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        'name',
        "email",
        'country',
        'city',
        'street',
        'house_number',
        'create_time',
    )
    list_filter = ('city',)


@admin.register(RetailChain)
class RetailChainAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        'name',
        "email",
        'country',
        'city',
        'street',
        'house_number',
        'provider_factory',
        'provider_dept',
        'create_time',
    )
    list_filter = ('city',)


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        'name',
        "email",
        'country',
        'city',
        'street',
        'house_number',
        'provider_factory',
        'provider_retail_chain',
        'provider_dept',
        'create_time',
    )
    list_filter = ('city',)
