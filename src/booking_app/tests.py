from base64 import b64encode
from unittest.mock import MagicMock,patch

from django.test import TestCase, Client
from .queue import Queue
import random
from .models import Hotel
import random

from django.test import TestCase, Client, override_settings

from .models import Hotel
from .queue import Queue


# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('FOO'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# TDD

class TestQueue(TestCase):
    def test_queue_exist(self):
        q = Queue(strategy="FIFO")

    def test_exist_strategy_fifo_and_lifo(self):
        with self.assertRaises(TypeError):
            q = Queue(strategy="LFA")

    def test_add_some_value_to_queue(self):
        q = Queue(strategy="FIFO")
        first_value = 4
        q.add(first_value)
        get_value = q.pop()
        self.assertEqual(get_value, first_value)

    def test_add_queue_milti_value(self):
        q = Queue(strategy="FIFO")
        test_values = [4, 3, 2]

        for ind in range(len(test_values)):
            q.add(test_values[ind])

        for ind in range(len(test_values)):
            get_value = q.pop()
            self.assertEqual(get_value, test_values[ind])

    def test_add_value_mega_values(self):
        q = Queue(strategy="FIFO")
        first_value = 44
        q.add(first_value)
        for i in range(20):
            value = random.randint(1, 10)
            q.add(value)

        get_value = q.pop()
        self.assertEqual(get_value, first_value)

    def test_empty_get_value_storage(self):
        q = Queue(strategy="FIFO")
        first_value = 44
        q.add(first_value)
        get_value = q.pop()
        self.assertEqual(get_value, first_value)
        get_value = q.pop()
        self.assertIsNone(get_value)


class TestHotelView(TestCase):
    def setUp(self):
        self.client = Client()
        self.name = "TestHotel"
        self.stars = 5
        self.description = "some description for TestHotel"
        # self.hotel = Hotel.objects.create(
        #     name=self.name,
        #     stars=self.stars,
        #     description = self.description
        # )
    def test_hotel_view(self):
        path = "/booking/hotels"
        response = self.client.get(path=path)
        hotels = response.context["hotels"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0].name, self.name)
        self.assertEqual(hotels[0].stars, self.stars)
        self.assertEqual(hotels[0].id, 1)

    def test_create_hotel_instance(self):
        self.assertEqual(self.hotel.id, 1)
        self.assertEqual(self.hotel.name, self.name)
        self.assertEqual(self.hotel.stars, self.stars)
        self.assertEqual(self.hotel._meta.get_field('name').verbose_name, "название")
        self.assertEqual(self.hotel._meta.get_field('name').max_length, 50)
        self.assertEqual(self.hotel._meta.get_field('name').null, True)
    @patch('booking_app.tasks.requests')
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_create_hotel_form(self,fake_requests):
        img_content = b'12345678'
        fake_response = MagicMock()
        fake_requests.post.return_value = fake_response
        fake_response.json.return_value = {'images': [b64encode(img_content)]}
        path = "/booking/hotels_form_add"
        response = self.client.post(
            path=path,
            data={
                "name": self.name,
                "stars": self.stars,
                "description": self.description,
            })


        hotel = Hotel.objects.get(id=1)

        self.assertEqual(hotel.name, self.name)
        self.assertEqual(hotel.stars, self.stars)
        self.assertEqual(hotel.description, self.description)
        self.assertEqual(hotel.photo.read(),img_content)

    def tearDown(self):
        pass
        # hotels = Hotel.objects.all()
        # for hotel in hotels:
        #     hotel.delete()


        # hotel = Hotel.objects.create(
        #     name=name,
        #     stars=stars,
        #     description=description
        # )
        # self.assertEqual(hotel.id, 1)
        # self.assertEqual(hotel.name, name)
        # self.assertEqual(hotel.stars, stars)

# if __name__ == '__main__':
#     unittest.main()
