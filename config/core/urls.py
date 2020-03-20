from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [
    path(
        "",
        room_views.HomeView.as_view(),  #  클래스를 뷰로 변경하는 메소드
        name="home",  # 기본 경로에 rooms->view 파일 안에있는 HomeView 클래스 등록
    ),
]
