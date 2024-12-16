from django.contrib import admin

from electronics_network.models import Factory, RetailChain, Entrepreneur


@admin.action(description="Очистить поле задолженности")
def cleaned_provider_dept(modeladmin, request, queryset):
    queryset.update(provider_dept=0.00)


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
        'provider_factory',
        'provider_dept',
        'create_time',
    )
    list_filter = ('city',)
    actions = [cleaned_provider_dept]


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
        'provider_retail_chain',
        'provider_dept',
        'create_time',
    )
    list_filter = ('city',)
    actions = [cleaned_provider_dept]


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
        'provider_entrepreneur',
        'provider_dept',
        'create_time',
    )
    list_filter = ('city',)
    actions = [cleaned_provider_dept]

