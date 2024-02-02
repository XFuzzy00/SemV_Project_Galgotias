from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.main_render, name="main_render"),
    path('stocks/', views.stocks_render, name="stocks_render"),
    path("about-us/", views.about_us_render, name="about_us_render"),
    path("hire-a-broker/", views.hire_a_broker, name="hire_a_broker"),
    path("bitcoin/", views.bitcoin_render, name="bitcoin_render"),
    path("ethereum/", views.Ethereum_render, name="ethereum_render"),
    path("bnb/", views.bnb_render, name="bnb_render"),
]