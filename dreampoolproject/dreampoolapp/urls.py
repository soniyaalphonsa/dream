from django.urls import path

from dreampoolapp import views

urlpatterns = [
    path('',views.demo,name='demo')
]