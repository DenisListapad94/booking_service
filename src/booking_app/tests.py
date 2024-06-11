import unittest
from django.test import TestCase,Client
from .queue import Queue
import random
from .models import Hotel

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
        test_values  = [4,3,2]

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
            value = random.randint(1,10)
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
    def test_hotel_view(self):
        name = "TestHotel"
        stars = 5
        Hotel.objects.create(name=name,stars=stars)
        path = "/booking/hotels"
        client = Client()
        response = client.get(path=path)
        hotels = response.context["hotels"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(hotels),1)
        self.assertEqual(hotels[0].name, name)
        self.assertEqual(hotels[0].stars, stars)
        self.assertEqual(hotels[0].id, 1)





# if __name__ == '__main__':
#     unittest.main()
