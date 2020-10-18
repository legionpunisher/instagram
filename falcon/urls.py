from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^accounts/profile/', views.add_profile, name='add_profile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),