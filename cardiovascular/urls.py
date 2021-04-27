from django.urls import include, path

from api import views

from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',views.index,name='api Documentation'),
    path('api/v1/cardio/risk', views.cardio_risk),
    path('api/v2/cardio/risk', views.cardiorisk),
    path('admin/', admin.site.urls),
]