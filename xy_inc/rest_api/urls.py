from django.conf.urls import url
from rest_api import views

urlpatterns = [
    url(r"^POIs/$", views.poi_list),
    url(r"^POIs/(?P<coord_x>[\d]+)/(?P<coord_y>[\d]+)/(?P<distancia>[\d]+)/$", views.search_near)
]