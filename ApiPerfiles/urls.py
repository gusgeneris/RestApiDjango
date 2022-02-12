from django.urls import path
from ApiPerfiles import views
urlpatterns = [
    path('helloView/', views.HelloApiView.as_view()),
    ]