from rest_framework import serializers


class RankSerializer(serializers.Serializer):
    
    name        : serializers.CharField
    color       : serializers.CharField
    description : serializers.CharField
    position    : serializers.IntegerField
    min_score   : serializers.IntegerField
    max_score   : serializers.IntegerField

    name      = serializers.CharField(max_length=80, min_length = 3)
    color     = serializers.CharField(max_length=9)
    description = serializers.CharField()
    position  = serializers.IntegerField()
    min_score = serializers.IntegerField()
    max_score = serializers.IntegerField()


    def validate(self, data: dict[str,str]) -> dict[str,str]:
        
        import re
        
        color_reguex = r'^#[A-Za-z0-9]+$'
        color : str | None = data.get("color")
        
        if color is  None or re.match(color_reguex,color) is None:
            
            raise serializers.ValidationError(
                
                'color is void or not is hex'
            
        )

        return data
