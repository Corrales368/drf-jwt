from rest_framework import views
from rest_framework.response import Response


class HelloWorldAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = {
            
        }
        return Response(data)