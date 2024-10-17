from django.urls import path
from . import views

urlpatterns = [
    path('', views.evaluate_car, name='evaluate_car'),
    path('database/', views.database, name='database'),
    path('about/', views.about, name='about'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('market-changes/', views.market_changes, name='market_changes'),

]
