from django.conf.urls import url
from info import views

urlpatterns = [
(url(r'^index/',views.myview,name='myview')),
(url(r'^article/(\d+)/',views.article,name='article')),
(url(r'^login/',views.login,name="login")),
(url(r'^main_page',views.main_page,name="main_page")),
]
