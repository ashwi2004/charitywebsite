from main_app import views 
from django.contrib import admin
from django.urls import path, include
from main_app.admin import custom_admin_site

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('donate/', views.donate, name='donate'),
    path('purchase/', views.donate, name='donate'),
    path('congrats/<int:id>/<int:points>/', views.congrats, name='congrats'),
    path('causespage/<int:id>/', views.causespage, name='causespage'),
    path('admin/', admin.site.urls),
    path('available-causes/', views.available_causes, name='available_causes'),
    path('custom-admin/', custom_admin_site.urls),
    path('congrats_page/', views.causespage, name='causespage'),
    path('portfolio/<int:id>/', views.causespage, name='causespage'),
]
