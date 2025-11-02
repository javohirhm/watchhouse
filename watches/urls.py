from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('watch/<int:watch_id>/', views.watch_detail, name='watch_detail'),
    path('watch/<int:watch_id>/order/', views.order_watch, name='order_watch'),
]
