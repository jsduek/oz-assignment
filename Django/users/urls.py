from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path("", views.Users.as_view()), # api/v1/users
    path("myinfo", views.MyInfo.as_view()), # api/v1/users/myinfo
    
    # Authentication
    path("getToken", obtain_auth_token), # DRF token
    path("login", views.Login.as_view()), # Django Session login 
    path("logout", views.Logout.as_view()), # Django Session logout

    # JWT Authentication
    path("login/jwt", views.JWTLogin.as_view()), # Django Session JWTLogin
    path("login/jwt/info", views.UserDetailView.as_view()), 

    # Simple JWT Authentication
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNTI3NDY2MiwiaWF0IjoxNzM0MDY1MDYyLCJqdGkiOiI5MTgyYmEyMDRhMzg0ODkyOTFiMGZhMDJmMzRkZGQ2NSIsInVzZXJfaWQiOjF9.VbGI_5TgkmMWLBaQ5pHKvZd5w0DpCLPFsQV7_7vTpek",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0MDY4NjYyLCJpYXQiOjE3MzQwNjUwNjIsImp0aSI6Ijc4M2YzMDQ1M2U5NjRiZTg4YzNhOThlOTRiNGNiODcwIiwidXNlcl9pZCI6MX0.KLB0i5IoPehTV23s2ftxQ8313YhVsJ3GtmuAYXLckXc"
# }