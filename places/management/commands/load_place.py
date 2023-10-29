import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


def upload_images(img_urls, place):

    for index, img_url in enumerate(img_urls):

        response = requests.get(img_url)
        response.raise_for_status()

        image_name = img_url.split('/')[-1]
        image_content = ContentFile(response.content, name=image_name)

        Image.objects.create(image=image_content, place=place, position=index)


class Command(BaseCommand):
    help = 'Автозагрузчик данных из *.json файла'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='*.json url')

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()

        place_description = response.json()
        place, created = Place.objects.get_or_create(title=place_description['title'],
                                                 lat=place_description['coordinates']['lat'],
                                                 lng=place_description['coordinates']['lng'],
                                                 description_long=place_description['description_long'],
                                                 description_short=place_description['description_short'])

        if created:
            upload_images(place_description['imgs'], place)
