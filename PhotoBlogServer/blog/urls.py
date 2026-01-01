from django.urls import path 
from . import views
from django.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 

router = routers.DefaultRouter()
router.register('Post', views.BlogImages)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('api_root/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]