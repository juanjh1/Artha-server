from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.views import APIView, Request, Response

from rank.application.seralizer import RankSerializer
from rank.infrastructure.models import Rank


class RankView(APIView):
     
    model = Rank
    paginate_by = 10

    def post (self, request: Request) -> Response:

        print(request.data)
       
        serializer: RankSerializer = RankSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        data:dict[str, str|None|int] = serializer.validated_data  

        if RankView.model.rank_name_exist(str(data['name'])):
              
            return Response({"message": "Request already processed"}, status=200) 
        
        try:
            
            Rank.objects.create(**data)
        
        except ValueError as e:

            return Response(
                            {
                                "error": 
                                e.__str__()
                            }, 
                            status=status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_200_OK)
    
    def get(self, request: Request) -> Response:
        
        pag: Paginator = Paginator(
                                   RankView.model.get_all_ranks(),
                                   RankView.paginate_by
        )

        page_number : str | None = request.query_params.get('page')
        
        page_obj = pag.get_page(page_number)
        
        serializer = RankSerializer(page_obj.object_list, many=True)

        return Response(data={
                            "page": page_obj.number,
                            "total_pages": page_obj.paginator.num_pages,
                            "total_items": page_obj.paginator.count,
                            "results": serializer.data
                        }, 
                        status=status.HTTP_200_OK )

