from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),

    ### 전력 사용
    path('Population_power/', views.Population_power),

    ##### test 용
    path('test/', views.Population_power),



    path('Population_PowerPlant/', views.Population_PowerPlant),
    path('Population_company/', views.Population_company),
    path('Population_PowerPlant_type/', views.Population_PowerPlant_type),
    path('Population_consumption/', views.Population_consumption),


    ### 비동기 사진 보기  
    path('Population_PowerPlant_type/load_view1/', views.load_view1),

]
