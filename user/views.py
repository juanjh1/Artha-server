from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView, Request

from user.infrastructure.models import UserModel


class LoginView(APIView):
    
    def post(self, request: Request)-> Response:
        
        from django.contrib.auth.hashers import check_password

        from user.application.serializer import LoginSerializer
        from user.utils.jwtUtils import get_tokens_for_user

        serializer : LoginSerializer = LoginSerializer(data = request.data)
        
        serializer.is_valid(raise_exception=True)
        
        username : str | None = serializer.validated_data.get("username")
        email    : str | None = serializer.validated_data.get("email")
        password : str = serializer.validated_data.get("password")
        
        try:
            
            user : UserModel = UserModel.\
            validate_user_identifiers_not_exist(email, username)
        
        except Http404 as e:
            
            return Response(
                            {
                                "error": 
                                e.__str__()
                            }, 
                            status=status.HTTP_404_NOT_FOUND
            )

        if not check_password(password, user.password):
            
            return Response(
                            {
                                "error": 
                                "Invalid credentials"
                            }, 
                            status=status.HTTP_401_UNAUTHORIZED
            )

        tokens = get_tokens_for_user(user)

        return Response(tokens, status=status.HTTP_200_OK)


class RegisterView(APIView):
    
    def post(self, request: Request)-> Response:
        
        from user.application.serializer import RegisterSerializer
        
        serializer : RegisterSerializer  = RegisterSerializer(data = request.data)
        
        serializer.is_valid(raise_exception=True)

        username : str = serializer.validated_data.get("username")
        email    : str = serializer.validated_data.get("email")
        password : str = serializer.validated_data.get("password")
        
        if UserModel.validate_user_identifiers_not_exist(email, username):

            return Response({"message": "Request already processed"}, status=200) 

        try:
            
            UserModel.objects.create_user(username, email, password)
        
        except ValueError as e:
            
            return Response(
                            {
                                "error": 
                                e.__str__()
                            }, 
                            status=status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_200_OK)



class LogoutView(APIView):
    
      permission_classes = [IsAuthenticated]
