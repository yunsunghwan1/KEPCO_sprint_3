from django.shortcuts import render
from django.http import HttpResponse 
from mainapp.map.map_view_people import Map_View
from mainapp.data.data_view import Data_View
from django.http import JsonResponse



def index(request) : 
    # return render(request,"mainapp/index_sample.html",{})
    return render(request,"mainapp/index.html",{})

## 전력 사용
def Population_power(request) : 
    ### 클래스 생성시키기
    input_data  = request.GET.get('vals', '2012')
    map_view = Map_View(input_data)
    data_view = Data_View()
    picture_1 = "<img src='/static/mainapp/data_graph_img/fig.png' style='display: block; width: 100%; height: 100%;'>"
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    return render(request,"mainapp/map/Population_PowerPlant.html",
                  {"map_html" : map_html, 
                   "input_data" : input_data,
                   "picture_1" : picture_1
                   
                   
                   })

# test용 문제
def Population_power(request) : 
    ### 클래스 생성시키기
    input_data  = request.GET.get('vals', '2012')
    map_view = Map_View(input_data)
    data_view = Data_View()
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    return render(request,"mainapp/map/test.html",{"map_html" : map_html, "input_data" : input_data})


def Population_PowerPlant(request) : 
    ### 클래스 생성시키기
    input_data  = request.GET.get('vals', '2012')
    map_view = Map_View(input_data)
    data_view = Data_View()
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    return render(request,"mainapp/map/Population_PowerPlant.html",{"map_html" : map_html, "input_data" : input_data})

def Population_company(request) : 
    ### 클래스 생성시키기
    input_data  = request.GET.get('vals', '2012')
    map_view = Map_View(input_data)
    data_view = Data_View()
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    return render(request,"mainapp/map/Population_company.html",{"map_html" : map_html, "input_data" : input_data})

def Population_PowerPlant_type(request) : 
    ### 클래스 생성시키기
    input_data  = request.GET.get('vals', '2012')
    map_view = Map_View(input_data)
    data_view = Data_View()
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    return render(request,"mainapp/map/Population_PowerPlant_type.html",{"map_html" : map_html, "input_data" : input_data})

def Population_consumption(request) : 
    ### 클래스 생성시키기
    input_data  = request.GET.get('vals', '2012')
    map_view = Map_View(input_data)
    data_view = Data_View()
    picture_1 = "/static/mainapp/data_graph_img/popular/1.png"
    picture_2 = "/static/mainapp/data_graph_img/popular/2.png"
    picture_3 = "/static/mainapp/data_graph_img/popular/3.png"
    picture_4 = "/static/mainapp/data_graph_img/popular/4.png"
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    return render(request,"mainapp/map/Population_consumption.html",
                  {"map_html" : map_html, 
                   "input_data" : input_data,
                   "picture_1" : picture_1,
                   "picture_2" : picture_2,
                   "picture_3" : picture_3,
                   "picture_4" : picture_4,
                   })



def load_view1(request) :
    return render(request,"mainapp/data_map/busan_map_population_visualization.html",{})

# def load_view2(request) :
#     return render(request,
#                   "nonmodelapp/jquery_load/load_view2.html",
#                   {})

# def load_view3(request) :
#     return render(request,
#                   "nonmodelapp/jquery_load/load_view3.html",
#                   {})
