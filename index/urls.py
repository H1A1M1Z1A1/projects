from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns=[
path('',views.index, name='index'),
# path('multi_language',views.multi_language, name='multi_language'),


# path("language", views.language, name="language"),
# path("about", views.about, name="about"),
# path("contact", views.contact, name="contact"),

]
