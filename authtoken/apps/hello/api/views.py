from rest_framework import views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


User = get_user_model()

class HelloWorldAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        # Get user
        user = User.objects.all().first()
        # Get token
        token = Token.objects.filter(user=user)
        # Validate if token exist
        if token.exists():
            # If exist, return token
            token = token.first()
            data = {
                'message': 'Not create!',
                'token': token.key
            }
            return Response(data)
            
        else:# If not exist, then create new token user
            token = Token.objects.create(user=user)       
            data = {
                'message': 'Create!',
                'token': token.key
            }
            return Response(data)
    



