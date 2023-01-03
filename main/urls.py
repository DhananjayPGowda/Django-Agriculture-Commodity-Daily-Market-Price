from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('test',views.test),
    path('admin_pannel',views.admin),
    path('admin_pannel/add',views.admin),
    path('admin_pannel/add_<str:Type>',views.add_data),
    path('/search_market',views.search_market),
    path('/<str:crop>',views.details),
    
    path('/<str:crop>/<str:market>',views.View),
]