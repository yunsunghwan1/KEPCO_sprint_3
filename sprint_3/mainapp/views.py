from django.shortcuts import render
from django.http import HttpResponse 
from mainapp.map.map_view import Map_View
from mainapp.data.data_view import Data_View
def index(request) : 
    # return render(request,"mainapp/index_sample.html",{})
    return render(request,"mainapp/index.html",{})

def Population_PowerPlant(request) : 
    ### 클래스 생성시키기
    map_view = Map_View()
    data_view = Data_View()
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    ### 스타벅스 데이터프레임 받아오기
    map_data = map_view.getDataFrame()
    return render(request,"mainapp/map/Population_PowerPlant.html",{"map_html" : map_html,
                   ### to_html() : <table>태그로 변화해줌
                   "map_data" : map_data.to_html()})

def Population_company(request) : 
    ### 클래스 생성시키기
    map_view = Map_View()
    data_view = Data_View()
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    ### 스타벅스 데이터프레임 받아오기
    map_data = map_view.getDataFrame()
    return render(request,"mainapp/map/Population_company.html",{"map_html" : map_html,
                   ### to_html() : <table>태그로 변화해줌
                   "map_data" : map_data.to_html()})


def Population_PowerPlant_type(request) : 
    ### 클래스 생성시키기
    map_view = Map_View()
    data_view = Data_View()
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    ### 스타벅스 데이터프레임 받아오기
    map_data = map_view.getDataFrame()
    return render(request,"mainapp/map/Population_PowerPlant_type.html",{"map_html" : map_html,
                   ### to_html() : <table>태그로 변화해줌
                   "map_data" : map_data.to_html()})


def Population_consumption(request) : 
    ### 클래스 생성시키기
    map_view = Map_View()
    data_view = Data_View()
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    ### 스타벅스 데이터프레임 받아오기
    map_data = map_view.getDataFrame()
    return render(request,"mainapp/map/Population_consumption.html",{"map_html" : map_html,
                   ### to_html() : <table>태그로 변화해줌
                   "map_data" : map_data.to_html()})
