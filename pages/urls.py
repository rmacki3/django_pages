#from django.urls import path
#from .views import HomePageView, AboutPageView

#urlpatterns = [
#    path('about/', AboutPageView.as_view(), name='about'),
#    path('', HomePageView.as_view(), name='home'),
#]

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('', views.home_page, name='home'),

]
