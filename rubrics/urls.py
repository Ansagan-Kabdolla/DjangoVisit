from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('where_to_stay/',stay, name='stay'),
    path('gallery',gallery,name = 'gallery'),
    path('where_to_go/',go, name='go'),
    path('where_to_eat/',eat, name='eat'),
    path('where_to_eat/natioanl_foods',national_foods,name='national_foods'),
    path('where_to_eat/type/<slug:slug>',type_eat,name='type_eat'),
    path('where_to_stay/top/<slug:slug>',top_stay,name='top_stay'),
    path('where_to_stay/type/<slug:slug>',type_stay,name='type_stay'),
    path('hotels/<slug:slug>',hotels, name='hotels'),
    path('foods/<slug:slug>',national_foods,name='national_foods'),
    path('events/',events, name='events'),
    path('where_to_eat/<int:pk>',eat_detail,name='eat_detail'),
    path('where_to_go/<int:pk>',go_detail,name='go_detail'),
    path('where_to_stay/<int:pk>',stay_detail,name='stay_detail'),
    path('add_reviews_eat/<int:pk>',AddReviewEat.as_view(),name='add_reviews_eat'),
    path('add_reviews_stay/<int:pk>',AddReviewStay.as_view(),name='add_reviews_stay'),
    path('news',news,name = 'news'),
    path('news/<slug:slug>',news_detail,name='news_detail'),
    path('akmola',akmola,name='akmola'),
    path('akmola/<slug:slug>',akmola_detail,name = 'akmola_detail'),
    path('events',events,name = 'events'),
    path('tours',tours,name='tours'),
    path('tours/<slug:slug>',tours_detail,name='tours_detail'),
    path('tourists',tourists,name='tourists'),
    path('tourists/<slug:slug>',tourists_detail,name='tourists_detail'),
    path('comanda',comanda,name='comanda'),
    path('search', SearchView.as_view(), name='search'),
    path('filtering/',filtering,name='filtering'),
    path('filtering_stay/',filtering_stay,name='filtering_stay'),

    #path('filter_ajax/',filter_ajax,name='filter_ajax'),
    #path('select_lang',select_lang,name='select_lang')
]
