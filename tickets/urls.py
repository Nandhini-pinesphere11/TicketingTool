from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create-ticket/',views.CreateTicket,name="create-ticket"),
    path('all-ticket/',views.AllTicket,name="all-ticket"),
    path('dashcards/',views.Dashcards,name="dashcards")

]
