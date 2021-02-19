from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import requests
import datetime
from .serializers import *
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend,FilterSet

from rest_framework import viewsets
# Create your views here.
#OMDB_API_KEY = os.environ['800057eb']
OMDB_API_URL = "http://www.omdbapi.com/"
OMDB_API_TIMEOUT = 5

base_url = "http://www.omdbapi.com/?i=tt3896198&apikey=800057eb"



def RequestLink(request):
    return render(request, 'app/index.html')


def saveToDB(request):
    getdata = requests.get(base_url.format())
    all_data = getdata.json()
    # date = all_data['Released'].split(' ')


    # date = datetime.datetime(int(date[2]), str(date[1]), int(date[0]))

    movie = Movies.objects.create(
        title = all_data['Title'],
        released = datetime.datetime(2017,5,5),
        rated = all_data['Rated'],
        genre =  all_data['Genre'],
        imdbid = all_data['imdbID']
    )

    return JsonResponse({'db': len(Movies.objects.all())})


    if request.method == 'POST':
        ip = request.POST['uip']

        ufilter = request.POST['filter']



       # if ufilter == 'Title':
            
        
        getdata = requests.get(base_url.format())
        all_data = getdata.json()
        
        searched_data = all_data[ufilter]
        print(searched_data)

        if ip.lower() in searched_data.lower():
            data = {
                'title' : all_data['Title'],
                'release_date' : all_data['Released'],
                'rated' : all_data['Rated'],
                'genre' : all_data['Genre'],
                'imdbid' : all_data['imdbID']
            }
            return JsonResponse( {'data': data} )
        else:
            return JsonResponse( {'data': 'not found'} )
    else:
        return render(request, 'app/index.html')


class MovieFilter(FilterSet):
    title = filters.CharFilter('title')
    genre = filters.CharFilter('genre')

class MovieViewset(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class =  MovieSerializer
    filter_backends = [DjangoFilterBackend  ]
    filterset_fields = ['rated','title','released','imdbid','genre']

    # def get_queryset(self):
    #     title = self.request.title
    #     return Movies.objects.filter(title=title)