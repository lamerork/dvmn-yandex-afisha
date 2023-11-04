from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from places.models import Place


def show_index(request):
    template = loader.get_template('index.html')
    context = {}
    context['json'] = {
      "type": "FeatureCollection",
      "features": []
    }

    places = Place.objects.all()

    features = []

    for place in places:
        feature = {
             'type': 'Feature',
             'geometry': {
                 'type': 'Point',
                 'coordinates': [place.lng, place.lat]
             },
             'properties': {
                 'title': place.title,
                 'place_id': place.id,
                 'detailsUrl': reverse('place_detail', kwargs={'id': place.id})
             }
        }
        features.append(feature)

    context['json']['features'] = features

    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def show_detail(request, id):
    place = get_object_or_404(Place, pk=id)

    place_serialized = {
         'title': place.title,
         'imgs': [image.image.url for image in place.images.all()],
         'short_description': place.short_description,
         'long_description': place.long_description,
         'coordinates': {
             'lng': place.lng,
             'lat': place.lat
         }
     }
    return JsonResponse(place_serialized, json_dumps_params={'indent': 4, 'ensure_ascii': False, })
