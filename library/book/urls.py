from django.contrib import admin
from django.urls import path,include
from .views import BookApiView

urlpatterns = [
    path('',BookApiView.as_view()),
    path('<int:id>/',BookApiView.as_view())
]
