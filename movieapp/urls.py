from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('save/', saveToDB, name='save'),
    path("movieapi/",MovieViewset.as_view()),
]
