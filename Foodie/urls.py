# To link the urls to the views
from django.urls import path
from . import views # . means current directory
from django.urls import include 

from django.urls import path
from . import views

app_name = 'Foodie' # This is the namespace for the app

urlpatterns = [
    path('', views.index, name='index'),
    path('foods/', views.index, name='index'),  # This makes `food/` point to `index`
    path('items/',views.items, name='items'), # This makes `food/items/` point to `items`
    path('render2/', views.render2 , name='render2'), # This makes `food/render2/` point to `render2`
    path('<int:item_id>/', views.detail, name='detail'),

]