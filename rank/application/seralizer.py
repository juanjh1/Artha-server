from rest_framework import serializers

from rank.infrastructure.models import Rank


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
    
    class Meta:
        model = Rank
        fields = ["name", "color", "description", "position", "min_score", "max_score"]

    def validate(self, data: dict[str,str]) -> dict[str,str]:
        
        import re
        
        color_reguex = r'^#[A-Za-z0-9]+$'
        
        color       : str | None = data.get("color")
        min_score   : str | None = data.get("min_score")
        max_score   : str | None = data.get("max_score")

        if(min_score is None or max_score is None ) or int(min_score) >= int(max_score):
            
            raise serializers.ValidationError(
                
                'min_score should be minor than max_score'
            )
            
        if color is  None or re.match(color_reguex,color) is None:
            
            raise serializers.ValidationError(
                
                'color is void or not is hex'
            )

        return data
