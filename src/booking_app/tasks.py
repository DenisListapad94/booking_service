import base64
from django.core.files.base import ContentFile
from celery import shared_task
from .models import Hotel
import requests

@shared_task
def create_photo(data):
    hotel = Hotel(
        name=data['name'],
        stars=data['stars'],
        description=data['description']
    )
    response = requests.post(
        'https://bf.dallemini.ai/generate',
        json={'prompt': hotel.description}
    )
    data = base64.b64decode(response.json()['images'][0])
    hotel.photo = ContentFile(data, name='hello.png')
    hotel.save()