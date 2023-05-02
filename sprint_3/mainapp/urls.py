from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('Population_PowerPlant/', views.Population_PowerPlant),
    path('Population_company/', views.Population_company),
    path('Population_PowerPlant_type/', views.Population_PowerPlant_type),
    path('Population_consumption/', views.Population_consumption),
    #  map update문
    # path('update_view/', views.update_view),


]
