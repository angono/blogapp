from django.urls import path
from .views import * 

urlpatterns = [
    path('', post_list_view, name='post-list'),
    path('detail/<str:ids>/', post_detail_view, name='post-detail'),
    path('catg/<str:ids>/', catg_detail_view, name='catg-detail'),
    path('search/post', search_post_view, name='post-search'),

]

