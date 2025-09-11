
# Create your views here.
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView, Request

from user.infrastructure.models import UserModel
from user.utils.jwtUtils import get_tokens_for_user


class LoginView(APIView):
    def post(self, request: Request)-> Response:
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not (username or email) or not password:
            return Response(
                {"error": "Please provide username/email and password"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            if email:
                user = UserModel.objects.get(email=email)
            else:
                user = UserModel.objects.get(email=username)  
        except UserModel.DoesNotExist:
            return Response({"error": "Invalid credentials"},
                            status=status.HTTP_401_UNAUTHORIZED)

        if not check_password(password, user.password):
            return Response({"error": "Invalid credentials"}, 
                            status=status.HTTP_401_UNAUTHORIZED)

        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)

