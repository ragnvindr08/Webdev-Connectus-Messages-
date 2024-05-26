from django.urls import path, include
from .views import authView, home
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from .views import messages_view

urlpatterns = [
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),   
    path('registrations/signup.html', authView,name='signup'),
    path('community/', views.community, name='community'), 
    path('messages/', messages_view, name='messages'), #messages url connected siya sa view.py yung messages_view
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

