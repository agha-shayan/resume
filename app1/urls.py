
from django.urls import path,include
from app1.views import *
urlpatterns = [
    path('',index_view),
    path("inner-page.html",inner_page)
]