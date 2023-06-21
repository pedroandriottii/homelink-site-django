from django.urls import path
from .views import home, loginView, productList, about, services
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', about, name='about'),
    path('servicos/', services, name='services'),
    path('login/', loginView, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', productList, name='dashboard'),

]