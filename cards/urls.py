from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name = 'catalog'),
    path('<int:card_id>/', views.get_card_by_id, name = 'card_id'),
    path('<slug:slug>/', views.get_category_by_name, name = 'slug')
    
]