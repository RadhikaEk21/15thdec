from django.urls import path
from.import views
urlpatterns = [
    path('home/',views.home),
    path('login/',views.user_login),
    path('success/',views.success),
    path('sing_up/',views.user_signup),
    path('reset',views.Resethome,name='reset'),
    path('passwordreset',views.resetPassword,name="passwordreset") 
]