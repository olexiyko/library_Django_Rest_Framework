from django.urls import path,include
from .views import AuthorApiView

urlpatterns = [
    path('',AuthorApiView.as_view()),
    path('<int:id>/',AuthorApiView.as_view())
]
