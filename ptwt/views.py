import json
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from django.shortcuts import render
from ptwt.models import Tweet

class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ['name', 'message', 'timestamp']

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-timestamp').values()
    serializer_class = TweetSerializer
    
    def list(self, request):
        queryset = Tweet.objects.all().order_by('-timestamp').values()
        serializer = TweetSerializer(queryset, many=True)
        return Response(serializer.data)

def index(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets.html', 
        {
            'tweets_json': json.dumps(TweetSerializer(tweets, many=True).data),
        }
    )