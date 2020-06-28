from django.urls import include, path
from . import views
from machina import urls as machina_urls

urlpatterns = [
    path('', views.hi, name='home-page'),
    path('play/', views.play, name='play-page'),
    # path('forum/', views.forum, name='forum-page'),
    path('forum/', include(machina_urls)),
    path('store/', views.store, name='store-page'),
    path('checkout/', views.check, name='checkout-page')
]