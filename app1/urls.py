from django.urls import path
from .import views

urlpatterns=[
    path("",views.home,name="/"),
    path("audio",views.audio,name="audio"),
    path('blog/', views.PostList.as_view(), name="blog"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
    path("chats",views.chat,name="chat"),
    path('reviewed',views.reviewed,name='revied'),
    path('susuc',views.susc,name='susuc'),
    path("complication",views.complication,name="complication"),
    path("diafacts",views.diafact,name="diafact"),
    path("diet",views.diet,name="diet"),
    path("elderdia",views.elderdia,name="elderdia"),
    path("faq",views.faq,name="faq"),
    path("fitness",views.fitness,name="fitness"),
    path("footcare",views.footcare,name="footcare"),
    path("juvenlie",views.juvenlie,name="juvenlie"),
    path("latestdia",views.latestdia,name="latestdia"),
    path("linkup",views.linkup,name="linkup"),
    path("video",views.video,name="video"),
    path("women",views.women,name="women")
]