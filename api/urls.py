from django.urls import path
from api import views


urlpatterns = [
    path("screenshots/", views.ScreenShotView.as_view() , name="screenshots"),
    path("base_path/", views.BasePathView.as_view() , name="base_path"),
]
