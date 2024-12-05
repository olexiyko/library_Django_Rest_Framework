from django.urls import path
from .views import OrderApiView

urlpatterns=[
   path('',OrderApiView.as_view()),
   path('<int:id>/',OrderApiView.as_view())

]