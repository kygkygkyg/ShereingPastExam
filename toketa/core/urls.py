from django.contrib import admin
from django.urls import path

from core.views import index, sign_io # 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index.home), # My page
    path('sign_up/', sign_io.sign_up), # sign up
    path('sign_in/', sign_io.sign_in), # sign in
    path('sign_out/', sign_io.sign_out), # sign out
]
