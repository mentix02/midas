from django.urls import path, include

urlpatterns = [
    path('v1/', include('backend.api.v1')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
