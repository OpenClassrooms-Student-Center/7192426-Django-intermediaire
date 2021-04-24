from django.contrib import admin
from django.urls import path

import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
]
