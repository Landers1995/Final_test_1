from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from electronics_network.models import Factory, RetailChain, Entrepreneur
from users.models import User


class ElectronicsNetworkCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@example.com', is_active=True)
        self.factory = Factory.objects.create(name="Завод1",
            email="zavod1@mail.ru",
            country="Россия",
            city="Москва",
            street="Новая Басманная",
            house_number="2/1 стр. 1",
            product_name="Станок",
            product_model=1,
            product_date="2024-12-13",
            provider_dept=2000.00,
            create_time="2024-12-13T09:57:33.996845Z",)
        self.retail_chain = RetailChain.objects.create(name="Розница1",
            email="retail1@mail.ru",
            country="Россия",
            city="Казань",
            street="Ленина",
            house_number="5",
            product_name="Станок",
            product_model=1,
            product_date="2024-12-13",
            provider_dept=30000.00,
            create_time="2024-12-13T09:57:33.996845Z",
            provider_factory=self.factory)
        self.entrepreneur = Entrepreneur.objects.create(name="ИП1",
            email="entrepreneur1@mail.ru",
            country="Россия",
            city="Тверь",
            street="Гагарина",
            house_number="16",
            product_name="Станок",
            product_model=1,
            product_date="2024-12-13",
            provider_dept=40000.00,
            create_time="2024-12-13T09:57:33.996845Z",
            provider_factory=self.factory,
            provider_retail_chain=self.retail_chain)
        self.client.force_authenticate(user=self.user)

    def test_factory_retrieve(self):
        url = reverse('electronics_network:factory-retrieve', args=(self.factory.pk,))
        responce = self.client.get(url)
        data = responce.json()
        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.factory.name
        )

    def test_retail_chain_retrieve(self):
        url = reverse('electronics_network:retail-retrieve', args=(self.retail_chain.pk,))
        responce = self.client.get(url)
        data = responce.json()
        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.retail_chain.name
        )

    def test_entrepreneur_retrieve(self):
        url = reverse('electronics_network:entrepreneur-retrieve', args=(self.entrepreneur.pk,))
        responce = self.client.get(url)
        data = responce.json()
        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.entrepreneur.name
        )

    def test_factory_create(self):
        url = reverse('electronics_network:factory-create')
        data = {
            'name': "Завод2",
            'email': "zavod2@mail.ru",
            'country': "Россия",
            'city': "Казань",
            'street': "Ленина",
            'house_number': "5",
            'product_name': "Станок",
            'product_model': 1,
            'product_date': "2024-12-13",
            'provider_dept': 20000.00
        }
        responce = self.client.post(url, data)

        self.assertEqual(
            responce.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Factory.objects.all().count(), 2
        )

    def test_retail_chain_create(self):
        url = reverse('electronics_network:retail-create')
        data = {
            'name': "Сеть2",
            'email': "retail2@mail.ru",
            'country': "Россия",
            'city': "Тверь",
            'street': "Гагарина",
            'house_number': "15",
            'product_name': "Станок",
            'product_model': 1,
            'product_date': "2024-12-13",
            # 'provider_factory': self.factory,
            'provider_dept': 20000.00
        }
        responce = self.client.post(url, data)

        self.assertEqual(
            responce.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            RetailChain.objects.all().count(), 2
        )

    def test_factory_update(self):
        url = reverse('electronics_network:factory-update', args=(self.factory.pk,))
        data = {
            'name': "Завод3",
            'email': "zavod3@mail.ru"
        }
        responce = self.client.patch(url, data)
        data = responce.json()
        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name', 'email'), 'Завод3', 'zavod3@mail.ru'
        )

    def test_factory_delete(self):
        url = reverse('electronics_network:factory-destroy', args=(self.factory.pk,))

        responce = self.client.delete(url)
        self.assertEqual(
            responce.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Factory.objects.all().count(), 0
        )

    def test_factory_list(self):
        url = reverse('electronics_network:factory-list')
        responce = self.client.get(url)
        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )

    def test_retail_chain_list(self):
        url = reverse('electronics_network:retail-list')
        responce = self.client.get(url)
        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )

    def test_entrepreneur_list(self):
        url = reverse('electronics_network:entrepreneur-list')
        responce = self.client.get(url)
        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )

