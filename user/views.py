
# Create your views here.
from django.contrib.auth.hashers import check_password
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView, Request

from user.application.serializer import LoginSerializer
from user.infrastructure.models import UserModel
from user.utils.jwtUtils import get_tokens_for_user


class LoginView(APIView):
    
    def post(self, request: Request)-> Response:


        serializer : LoginSerializer= LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        username : str | None = serializer.validated_data.get("username")
        email    : str | None = serializer.validated_data.get("email")
        password : str = serializer.validated_data.get("password")
        
        try:
            user : UserModel = UserModel.validate_user_existence(email, username)
        except Http404 as e:
            return Response(
                            {"error": e.__str__()}, 
                            status=status.HTTP_404_NOT_FOUND
            )

        if not check_password(password, user.password):
            

            return Response(
                            {"error": "Invalid credentials"}, 
                            status=status.HTTP_401_UNAUTHORIZED
            )
        tokens = get_tokens_for_user(user)

        return Response(tokens, status=status.HTTP_200_OK)

