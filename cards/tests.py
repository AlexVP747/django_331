from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
class CardsAppTests(TestCase):
# """Тестирование приложения Cards."""
  def setUp(self):
# Клиент для тестирования
    self.client = Client()
def test_app_loads(self):
# """Проверка, что приложение загружается и главная страница доступна."""
# Давайте подробно разберем, как работают тесты в приведенном примере без использования кода:
# Настройка Тестового Клиента
# Тестирование Доступности Приложения
# Тестирование Маршрутов
# Общие Принципы Тестирования
# В целом, эти тесты помогают обеспечить надежность работы веб-приложения, подтверждая, что его основные
# функции и маршруты доступны и работают как ожидается. Это является ключевым аспектом разработки качественного
# программного обеспечения.
# Сдача задания
# Критерии проверки 👌
  response = self.client.get('/cards/catalog/')
  self.assertEqual(response.status_code, 200)
  self.assertContains(response, "Каталог карточек")
def test_card_route(self):
  # """Проверка маршрута для получения карточки по ID."""
    response = self.client.get('/cards/catalog/1/')
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Карточка 1")
def test_category_route(self):
# """Проверка маршрута для получения карточек по категории."""
    response = self.client.get('/cards/catalog/some-category-slug/')
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Категория some-category-slug")
