from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from api.models import BasePath
from api.models import ScreenshotParse
from django.core.management import call_command
from .serializers import ScreenshotParseSerializer
from pathlib import Path


class ScreenShotView(APIView):
    def get(self, request):
        return Response(ScreenshotParseSerializer(ScreenshotParse.objects.all(), many=True).data)

    def post(self, request):
        print(request.data)
        path = request.data['path'].strip()

        base_path = BasePath.load()
        base_path.path = path
        base_path.save()
        print(Path(path))
        try:
            
            assert Path(path).exists() == True
        except AssertionError:
            return Response({"message":"That path does not exist!"}, status=400)

        # try:
        call_command("parse_screenshots")
        return Response({"message":"Success!"})
        # except:
            # return Response({"message":"There was an error :("}, status=500)

class BasePathView(APIView):
    def get(self, request):
        return Response(BasePath.load().path)
