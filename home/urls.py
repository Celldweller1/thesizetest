from . import views
from django.urls import path

urlpatterns =[
    path("",views.ScanView.as_view()),
    path("test",views.test),
    path("testapi",views.testApi)
]