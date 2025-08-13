#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.IndexView, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.MenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]