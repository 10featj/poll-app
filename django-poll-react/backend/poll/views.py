from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PollSerializer
from .models import Poll

import urllib3 
#import PoolManager

class PollView(viewsets.ModelViewSet):
    # http = PoolManager()
    # r = http.request('GET', 'https://www.google.com/', headers = {
    #                     'Accepting-Encoding': 'br'})

    serializer_class = PollSerializer
    queryset = Poll.objects.all()
