from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', searchView, name='search'),
    path('anime_images/', ImagesView.as_view(), name='images'),
    path('about/', aboutView, name='about'),
    path('contact', contactView, name='contact'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/delete/', DeleteProfileView.as_view(), name='delete_profile'),
    path('publication/', publicationView, name='publication'),
]