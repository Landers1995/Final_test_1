from django.db import models


NULLABLE = {"blank": True, "null": True}


class Factory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', help_text='Назавание завода')
    email = models.CharField(max_length=150, verbose_name='Электронная почта', help_text='Электронная почта завода')
    country = models.CharField(max_length=150, verbose_name='Страна', help_text='Страна, где расположен завод')
    city = models.CharField(max_length=150, verbose_name='Город', help_text='Город, где расположен завод')
    street = models.CharField(max_length=150, verbose_name='Улица', help_text='Улица, где расположен завод')
    house_number = models.CharField(max_length=50, verbose_name='Номер дома', help_text='Номер дома, где расположен завод')
    product_name = models.CharField(max_length=150, verbose_name='Продукт', help_text='Назавание продукта завода', **NULLABLE)
    product_model = models.CharField(max_length=150, verbose_name='Модель продукта', help_text='Модель продукта завода', **NULLABLE)
    product_date = models.DateField(max_length=50, verbose_name='Дата выхода продукта', help_text='Дата выхода продукта завода', **NULLABLE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи о заводе')

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        self.name


class RetailChain(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', help_text='Назавание розничной сети')
    email = models.CharField(max_length=150, verbose_name='Электронная почта', help_text='Электронная почта розничной сети')
    country = models.CharField(max_length=150, verbose_name='Страна', help_text='Страна, где расположена розничная сеть')
    city = models.CharField(max_length=150, verbose_name='Город', help_text='Город, где расположена розничная сеть')
    street = models.CharField(max_length=150, verbose_name='Улица', help_text='Улица, где расположена розничная сеть')
    house_number = models.CharField(max_length=50, verbose_name='Номер дома', help_text='Номер дома, где расположена розничная сеть')
    product_name = models.CharField(max_length=150, verbose_name='Продукт', help_text='Назавание продукта розничной сети', **NULLABLE)
    product_model = models.CharField(max_length=150, verbose_name='Модель продукта', help_text='Модель продукта розничной сети', **NULLABLE)
    product_date = models.DateField(max_length=50, verbose_name='Дата выхода продукта', help_text='Дата выхода продукта розничной сети', **NULLABLE)
    provider_factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name="Завод-поставщик", **NULLABLE)
    provider_dept = models.DecimalField(max_digits=20, decimal_places=2, **NULLABLE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи о розничной сети')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        self.name


class Entrepreneur(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', help_text='Назавание индивидуального предпринимателя')
    email = models.CharField(max_length=150, verbose_name='Электронная почта', help_text='Электронная почта индивидуального предпринимателя')
    country = models.CharField(max_length=150, verbose_name='Страна', help_text='Страна, где расположен индивидуальный предприниматель')
    city = models.CharField(max_length=150, verbose_name='Город', help_text='Город, где расположен индивидуальный предприниматель')
    street = models.CharField(max_length=150, verbose_name='Улица', help_text='Улица, где расположен индивидуальный предприниматель')
    house_number = models.CharField(max_length=50, verbose_name='Номер дома', help_text='Номер дома, где расположен индивидуальный предприниматель')
    product_name = models.CharField(max_length=150, verbose_name='Продукт', help_text='Назавание продукта индивидуального предпринимателя', **NULLABLE)
    product_model = models.CharField(max_length=150, verbose_name='Модель продукта', help_text='Модель продукта индивидуального предпринимателя', **NULLABLE)
    product_date = models.DateField(max_length=50, verbose_name='Дата выхода продукта', help_text='Дата выхода продукта индивидуального предпринимателя', **NULLABLE)
    provider_factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name="Завод-поставщик", **NULLABLE)
    provider_retail_chain = models.ForeignKey(RetailChain, on_delete=models.CASCADE, verbose_name="Розничная сеть-поставщик", **NULLABLE)
    provider_dept = models.DecimalField(max_digits=20, decimal_places=2, **NULLABLE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи об индивидуальном предпринимателе')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    def __str__(self):
        self.name