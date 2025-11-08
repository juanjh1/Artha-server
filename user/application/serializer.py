from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    
    username : serializers.CharField
    email    : serializers.EmailField
    password : serializers.CharField

    username  = serializers.CharField(max_length=80, min_length = 3, required=False)
    email     = serializers.EmailField(required = False)
    password  = serializers.CharField(required=True)


    def validate(self, data: dict[str,str]) -> dict[str,str]:
        
        username : str | None =  data.get('username')  
        email    : str | None =  data.get('email')
        password : str | None =  data.get('password')
        
        if not( username is None and email is None) and password is None: 

            raise serializers.ValidationError(
                'Please provide username/email and password'
            )

        return data


class RegisterSerializer(serializers.Serializer):
    
    username : serializers.CharField
    email    : serializers.EmailField
    password : serializers.CharField
    
    username  = serializers.CharField(max_length=80, min_length = 3, required=False)
    email     = serializers.EmailField(required = False)
    password  = serializers.CharField(required=True)

    def validate(self, data: dict[str,str]) -> dict[str,str]:
       
        username : str | None =  data.get('username')  
        email    : str | None =  data.get('email')
        password : str | None =  data.get('password')
        
        if not( username is None or email is None) and password is None: 

            raise serializers.ValidationError(
                'Please provide username, email and password'
            )

        return data
