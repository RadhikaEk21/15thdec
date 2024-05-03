from django.urls import path
from .import views

urlpatterns=[
    path("sample_msg/",views.sample_msg),
    path("register/",views.register),
    path('vew_details/',views.view_reg),
    path('delete/(?P<pk>\d+)/',views.delete_data, name='delete_row'),
    path('updt/(?P<pk>\d+)/',views.update_data, name='updt'),
    path('std_api/',views.student_view.as_view())
]