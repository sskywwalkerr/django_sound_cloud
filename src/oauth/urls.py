from django.urls import path
from .endpoint import views, auth_views

urlpatterns = [
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('google/', auth_views.google_auth),
    path('', auth_views.google_login),
    path('author/', views.AuthorView.as_view({'get': 'list'})),
    path('author/<int:pk>/', views.AuthorView.as_view({'get': 'retrieve'})),
    path('social/', views.SocialLinkView.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}
    )),
]