from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
path('',views.project2_index,name='project2_index'),
path('backtest',views.backtest,name='backtest'),
path('result',views.result,name='result'),


# path("language", views.language, name="language"),
# path("about", views.about, name="about"),
# path("contact", views.contact, name="contact"),

]
