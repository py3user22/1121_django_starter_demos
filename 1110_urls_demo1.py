# app2_1107jg  urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
]

#app3_1107jg

app_name='app3_1107jg'      # defines the application namespace
                            # so that this app > views are identified by it

urlpatterns = [
    path('', views.index, name='index'),
]

#app_1107jg

app_name='app_1107jg'

urlpatterns = [
    #path('', views.home, name="home"),
    path('dishes/<str:dish>', views.menuitems),
]


#app_1106jg
#app4_1110jg

app_name='app4_1110jg'

urlpatterns = [
    path('', views.home, name="home"),
]

#demoapp/urls.py

app_name='demoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]

#newapp/urls.py

app_name='newapp'

urlpatterns = [
    path('', views.index, name='index'),
]

#-----------------
#project/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demoapp.urls', namespace='demoapp')),
    path('newdemo/', include('newapp.urls')),
]
