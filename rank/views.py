from rest_framework import status
from rest_framework.views import APIView, Request, Response

from rank.application.seralizer import RankSerializer
from rank.infrastructure.models import Rank


class RankView(APIView):
    

    def post (self, request: Request) -> Response:
       
        serializer: RankSerializer = RankSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        name        : str = serializer.validated_data.get('name')
        description : str = serializer.validated_data.get('name')
        color       : str = serializer.validated_data.get('color')
        position    : int = serializer.validated_data.get('position')
        min_score   : int = serializer.validated_data.get('min_score')
        max_score   : int = serializer.validated_data.get('max_score')
        
        if Rank.rank_exist(name):
              
            return Response({"message": "Request already processed"}, status=200) 
        
        try:
            
            Rank.objects.create(
                                name        = name, 
                                color       = color, 
                                position    = position, 
                                min_score   = min_score, 
                                max_score   = max_score,
                                description = description                    
            )
        
        except ValueError as e:

            return Response(
                            {
                                "error": 
                                e.__str__()
                            }, 
                            status=status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_200_OK)

