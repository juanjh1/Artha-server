from django.urls import path

from rank.views import RankView

urlpatterns = [
    path('', RankView.as_view() , name='rank'),
]
